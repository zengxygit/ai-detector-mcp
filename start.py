#!/usr/bin/env python3
"""
启动脚本 - 快速启动MCP服务器
"""

import os
import sys
import subprocess
import platform

def main():
    """主函数"""
    print("=" * 60)
    print("AI内容检测 - MCP服务器启动器")
    print("=" * 60)
    
    # 检查Python版本
    if sys.version_info < (3, 8):
        print("错误: 需要Python 3.8或更高版本")
        sys.exit(1)
    
    print(f"Python版本: {sys.version}")
    print(f"操作系统: {platform.system()}")
    
    # 检查依赖
    print("\n检查依赖...")
    try:
        import mcp
        import fastapi
        import uvicorn
        print("✓ 所有依赖已安装")
    except ImportError as e:
        print(f"✗ 缺少依赖: {e}")
        print("\n请运行以下命令安装依赖:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # 启动服务器
    print("\n启动MCP服务器...")
    print("-" * 60)
    
    try:
        os.chdir('server')
        subprocess.run([
            sys.executable, '-m', 'uvicorn',
            'mcp_server:mcp',
            '--host', '0.0.0.0',
            '--port', '8000',
            '--reload'
        ])
    except KeyboardInterrupt:
        print("\n\n服务器已关闭")
        sys.exit(0)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
