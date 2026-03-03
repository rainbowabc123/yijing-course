@echo off
echo 正在启动易经课程管理系统...
echo.

cd /d "%~dp0"

REM 检查是否安装了 streamlit
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo 正在安装 Streamlit...
    pip install streamlit
)

echo.
echo 管理系统已启动！
echo 浏览器会自动打开管理界面
echo 如果没有自动打开，请访问：http://localhost:8501
echo.
echo 按 Ctrl+C 可以关闭管理系统
echo.

streamlit run course_manager.py
