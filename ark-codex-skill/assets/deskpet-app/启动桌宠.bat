@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\pythonw.exe" (
  echo 请先运行安装环境.bat。
  pause
  exit /b 1
)
start "" ".venv\Scripts\pythonw.exe" "main.py"
