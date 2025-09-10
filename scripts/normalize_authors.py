#!/usr/bin/env python3
"""
批量规范作者展示：
- 读取 knowledge_base 下所有 .md（排除 index.md）
- 解析 YAML Front Matter 中的 author（支持单个或数组）
- 在文档第一个 H1 标题行之后插入或更新一行："> 作者：xxx"
- 若已存在作者展示行则跳过
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
KB = BASE / 'knowledge_base'

FRONT_MATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def parse_authors(meta_text: str):
    # 提取 author 字段（允许数组或字符串）
    # 简单解析：先找以 author: 开头的行，取整行，再判断是否为数组
    author_lines = [line for line in meta_text.splitlines() if line.strip().startswith('author:')]
    if not author_lines:
        return []
    line = author_lines[0]
    value = line.split(':', 1)[1].strip()
    # 去掉首尾空白与引号
    value = value.strip()
    if value.startswith('[') and value.endswith(']'):
        # 解析数组，按逗号分割
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(',')]
        # 去掉包裹引号
        cleaned = [p.strip('"\'') for p in parts]
        return [a for a in cleaned if a]
    else:
        # 单个作者
        single = value.strip('"\'')
        return [single] if single else []


def ensure_author_line(content: str, authors: list[str]) -> str:
    if not authors:
        return content
    lines = content.splitlines()
    # 找第一个 H1 标题行（以 # 开头且至少一个空格）
    h1_index = None
    for i, line in enumerate(lines):
        if line.startswith('# '):
            h1_index = i
            break
    if h1_index is None:
        return content
    # 检查下一非空行是否已是作者行
    j = h1_index + 1
    while j < len(lines) and lines[j].strip() == '':
        j += 1
    if j < len(lines) and lines[j].strip().startswith('> 作者：'):
        # 已存在则不改动
        return content
    # 插入作者行在标题下一行
    display = ','.join(authors)
    insert_line = f"> 作者：{display}"
    # 在 h1 后插入一个空行和作者行，保持简洁
    new_lines = lines[:h1_index+1] + [insert_line, ''] + lines[h1_index+1:]
    return '\n'.join(new_lines) + ('\n' if content.endswith('\n') else '')


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False
    meta = m.group(1)
    authors = parse_authors(meta)
    if not authors:
        return False
    new_text = ensure_author_line(text, authors)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main():
    changed = 0
    for md in KB.rglob('*.md'):
        if md.name == 'index.md':
            continue
        if process_file(md):
            changed += 1
            print(f"更新作者展示: {md.relative_to(KB)}")
    print(f"完成。更新文件数: {changed}")


if __name__ == '__main__':
    main() 