#!/usr/bin/env python3
"""
腾讯云静态网站托管部署脚本
功能：自动构建并准备部署文件
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, 
                              capture_output=True, text=True, check=True)
        print(f"✅ {cmd}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {cmd}")
        print(f"错误信息: {e.stderr}")
        sys.exit(1)

def build_site():
    """构建MkDocs网站"""
    print("🔨 开始构建MkDocs网站...")
    
    # 1. 同步文档
    print("📄 同步文档...")
    run_command("python3 scripts/sync_docs.py")
    
    # 2. 安装依赖
    print("📦 安装依赖...")
    run_command("python3 -m pip install -r requirements.txt")
    
    # 3. 构建网站
    print("🏗️ 构建网站...")
    run_command("python3 -m mkdocs build --clean")
    
    print("✅ 网站构建完成！")

def prepare_deploy():
    """准备部署文件"""
    print("📦 准备部署文件...")
    
    site_dir = Path("site")
    if not site_dir.exists():
        print("❌ site目录不存在，请先构建网站")
        sys.exit(1)
    
    # 检查关键文件
    required_files = ["index.html", "assets/"]
    for file in required_files:
        if not (site_dir / file).exists():
            print(f"❌ 缺少必要文件: {file}")
            sys.exit(1)
    
    print("✅ 部署文件准备完成！")
    print(f"📁 输出目录: {site_dir.absolute()}")
    print(f"📊 文件数量: {len(list(site_dir.rglob('*')))}")

def main():
    """主函数"""
    print("=" * 60)
    print("🚀 腾讯云静态网站托管部署准备")
    print("=" * 60)
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        print("❌ 需要Python 3.7或更高版本")
        sys.exit(1)
    
    # 构建网站
    build_site()
    
    # 准备部署
    prepare_deploy()
    
    print("\n🎉 部署准备完成！")
    print("\n📋 下一步操作：")
    print("1. 登录腾讯云控制台")
    print("2. 开通静态网站托管服务")
    print("3. 连接Gitee仓库")
    print("4. 配置构建命令和输出目录")
    print("5. 启用自动部署")

if __name__ == "__main__":
    main()
