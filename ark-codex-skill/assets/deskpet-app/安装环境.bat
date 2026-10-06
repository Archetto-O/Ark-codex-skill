@echo off
chcp 65001 >nul
cd /d "%~dp0"
python setup_runtime.py
if errorlevel 1 (
  echo 安装失败。请确认已安装Python 3.10或更高版本，并已将python加入PATH。
  pause
  exit /b 1
)
echo 安装完成，双击启动桌宠.bat即可运行。
pause
