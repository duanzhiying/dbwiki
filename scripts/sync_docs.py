#!/usr/bin/env python3
"""
数据库课程实验资源平台 - 文档同步脚本
功能：将 knowledge_base 中的内容同步到 docs 目录，供 MkDocs 构建使用
"""

import shutil
import os
import re
from pathlib import Path
from datetime import datetime

def validate_metadata(file_path):
    """验证文档元数据完整性"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含元数据头
        if not content.startswith('---'):
            return False, "缺少元数据头"
        
        # 提取元数据
        metadata_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not metadata_match:
            return False, "元数据格式错误"
        
        metadata = metadata_match.group(1)
        
        # 检查必填字段
        required_fields = ['doc_type', 'title', 'concepts', 'difficulty', 'author', 'date']
        for field in required_fields:
            if f'{field}:' not in metadata:
                return False, f"缺少必填字段: {field}"
        
        return True, "元数据完整"
    
    except Exception as e:
        return False, f"读取文件失败: {str(e)}"

def check_file_naming(file_path):
    """检查文件命名规范"""
    filename = file_path.name
    parent_dir = file_path.parent.name
    
    # 根据目录检查命名规范
    naming_patterns = {
        '1_sql_pitfalls': r'^[a-z_]+.*_[^_]+\.md$',
        '2_enterprise_cases': r'^[a-z_]+.*_[^_]+\.md$',
        '3_avoidance_guides': r'^[a-z_]+.*_[^_]+\.md$',
        '4_excellent_labs': r'^lab\d+.*_[^_]+\.md$',
        '5_course_designs': r'^[a-z_]+.*_[^_]+\.md$'
    }
    
    if parent_dir in naming_patterns:
        pattern = naming_patterns[parent_dir]
        if not re.match(pattern, filename):
            return False, f"文件命名不符合规范: {filename}"
    
    return True, "命名规范正确"

def add_updated_date_to_body(file_path):
    """在正文中添加更新日期（如果缺少）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取元数据
        metadata_start = content.find('---')
        if metadata_start == -1:
            return False, "缺少元数据头"
        
        metadata_end = content.find('---', metadata_start + 3)
        if metadata_end == -1:
            return False, "缺少元数据结束标记"
        
        metadata = content[metadata_start + 3:metadata_end].strip()
        
        # 提取updated字段
        updated_match = re.search(r'updated:\s*(.*?)(?:\n|$)', metadata)
        if not updated_match:
            return False, "缺少updated字段"
        
        updated_date = updated_match.group(1).strip()
        
        # 分割内容
        metadata_part = content[:metadata_end + 3]
        body_part = content[metadata_end + 3:]
        
        # 检查正文中是否有更新日期
        has_date = '更新日期：' in body_part or '更新时间：' in body_part
        
        if not has_date:
            # 在正文开头添加更新日期
            # 找到作者行后添加
            lines = body_part.split('\n')
            new_lines = []
            
            for i, line in enumerate(lines):
                new_lines.append(line)
                # 找到作者行后添加
                if '作者：' in line:
                    new_lines.append(f"> 更新日期：{updated_date}")
                    break
            
            # 重新组合内容
            new_content = metadata_part + '\n'.join(new_lines) + '\n' + '\n'.join(lines[i+1:]) if i < len(lines) - 1 else metadata_part + '\n'.join(new_lines)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True, "添加更新日期成功"
        
        return False, "已存在更新日期"
    
    except Exception as e:
        return False, f"处理失败: {str(e)}"

def sync_to_docs():
    """同步 knowledge_base 到 docs"""
    base_path = Path(__file__).parent.parent
    kb_path = base_path / 'knowledge_base'
    docs_path = base_path / 'docs'
    
    print(f"🔄 开始同步: {kb_path} -> {docs_path}")
    
    # 检查源目录是否存在
    if not kb_path.exists():
        print("❌ 错误: knowledge_base 目录不存在")
        return False
    
    # 需要保留的文件（不在 knowledge_base 中，但需要在 docs 中）
    files_to_preserve = ['contributing.md', 'index.md']
    preserved_files = {}
    
    # 保存需要保留的文件
    if docs_path.exists():
        for file_name in files_to_preserve:
            file_path = docs_path / file_name
            if file_path.exists():
                preserved_files[file_name] = file_path.read_text(encoding='utf-8')
                print(f"💾 保留文件: {file_name}")
    
    # 清空并重建 docs 目录
    if docs_path.exists():
        shutil.rmtree(docs_path)
        print(f"🗑️  清空目录: {docs_path}")
    
    # 复制文件并验证
    shutil.copytree(kb_path, docs_path)
    print(f"📋 复制完成: {kb_path} -> {docs_path}")
    
    # 恢复保留的文件
    for file_name, content in preserved_files.items():
        file_path = docs_path / file_name
        file_path.write_text(content, encoding='utf-8')
        print(f"✅ 恢复文件: {file_name}")
    
    # 在 docs 目录中添加更新日期到正文
    print("\n📋 在正文中添加更新日期...")
    added_count = 0
    skipped_count = 0
    failed_count = 0
    
    for file_path in docs_path.rglob('*.md'):
        if file_path.name in ['index.md', 'contributing.md']:
            skipped_count += 1
            continue
        
        success, message = add_updated_date_to_body(file_path)
        if success:
            added_count += 1
            print(f"✅  {file_path.relative_to(docs_path)}: {message}")
        else:
            failed_count += 1
            print(f"⚠️  {file_path.relative_to(docs_path)}: {message}")
    
    # 验证同步的文件
    validation_results = []
    for file_path in docs_path.rglob('*.md'):
        if file_path.name == 'index.md':
            continue  # 跳过首页
        
        # 检查元数据
        metadata_ok, metadata_msg = validate_metadata(file_path)
        if not metadata_ok:
            validation_results.append(f"⚠️  {file_path.relative_to(docs_path)}: {metadata_msg}")
        
        # 检查命名规范
        naming_ok, naming_msg = check_file_naming(file_path)
        if not naming_ok:
            validation_results.append(f"⚠️  {file_path.relative_to(docs_path)}: {naming_msg}")
    
    # 输出验证结果
    if validation_results:
        print("\n📋 验证结果:")
        for result in validation_results:
            print(result)
    else:
        print("✅ 所有文件验证通过")
    
    print(f"📋 添加完成: 成功 {added_count} 个, 跳过 {skipped_count} 个, 失败 {failed_count} 个")
    print(f"✅ 内容同步完成: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

def main():
    """主函数"""
    print("=" * 50)
    print("数据库课程实验资源平台 - 文档同步工具")
    print("=" * 50)
    
    success = sync_to_docs()
    
    if success:
        print("\n🎉 同步完成！可以运行 'mkdocs build' 构建网站")
    else:
        print("\n❌ 同步失败！请检查错误信息")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())