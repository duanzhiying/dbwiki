import os
import re
import sys

def validate_filenames():
    """验证文件名是否符合规范"""
    patterns = {
        '1_sql_pitfalls': r'^(syntax|logic|performance)_.+_.{3,15}\.md$',
        '2_enterprise_cases': r'^[a-z]+_.+_.{3,15}\.md$',
        '3_avoidance_guides': r'^[a-z]+_.+_.{3,15}\.md$',
        '4_excellent_labs': r'^lab\d*_.+_.{3,15}\.md$',
        '5_course_designs': r'^[a-z]+_.+_.{3,15}\.md$'
    }
    
    errors = []
    for root, dirs, files in os.walk("knowledge_base"):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                folder = os.path.basename(root)
                
                if folder in patterns:
                    if not re.match(patterns[folder], file):
                        errors.append(f"❌ 文件命名错误: {path} 不符合 {folder} 模块的命名规范")
    
    return errors

def validate_metadata():
    """验证元数据是否完整"""
    required_fields = ['doc_type', 'title', 'concepts', 'author', 'date']
    errors = []
    
    for root, dirs, files in os.walk("knowledge_base"):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # 检查元数据块是否存在
                        if "<!--" not in content or "doc_type:" not in content:
                            errors.append(f"❌ 元数据缺失: {path} 缺少元数据块")
                            continue
                        
                        # 检查必需字段
                        for field in required_fields:
                            if f"{field}:" not in content:
                                errors.append(f"❌ 元数据不完整: {path} 缺少 {field} 字段")
                except Exception as e:
                    errors.append(f"❌ 文件读取失败: {path} - {str(e)}")
    
    return errors

if __name__ == "__main__":
    filename_errors = validate_filenames()
    metadata_errors = validate_metadata()
    all_errors = filename_errors + metadata_errors
    
    if all_errors:
        print("\n验证发现错误:")
        for error in all_errors:
            print(error)
        sys.exit(1)
    else:
        print("✅ 所有文件符合命名规范和元数据标准")
        sys.exit(0)
