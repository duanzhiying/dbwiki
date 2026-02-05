#!/usr/bin/env python3
"""
下载文档中的图片到assets目录
"""

import os
import re
import requests
from pathlib import Path

# 文档路径
doc_path = Path('/Users/kidzying/Documents/紫金学院/教改项目实施/dbwiki/knowledge_base/raw_docs/Java 连接 MySQL Workbench 教程.md')

# 图片保存目录
assets_dir = Path('/Users/kidzying/Documents/紫金学院/教改项目实施/dbwiki/knowledge_base/assets/images/4_excellent_labs/java_mysql')
assets_dir.mkdir(parents=True, exist_ok=True)

# 读取文档内容
with open(doc_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有图片链接
image_pattern = r'!\[(.*?)\]\((.*?)\)'
images = re.findall(image_pattern, content)

print(f"找到 {len(images)} 张图片")

# 下载图片
for i, (alt_text, url) in enumerate(images, 1):
    try:
        # 生成文件名
        if alt_text and alt_text.endswith('.png'):
            filename = alt_text
        else:
            filename = f'image_{i:02d}.png'
        
        # 下载图片
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 保存图片
        save_path = assets_dir / filename
        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ 下载成功: {filename}")
        
    except Exception as e:
        print(f"❌ 下载失败: {url} - {str(e)}")

print(f"\n图片已保存到: {assets_dir}")
