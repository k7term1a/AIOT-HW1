@echo off
chcp 65001 > nul

echo 🚀 啟動線性迴歸 CRISP-DM 分析應用程式...
echo ======================================================

REM 檢查是否安裝了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤: 找不到 Python。請先安裝 Python。
    pause
    exit /b 1
)

REM 檢查虛擬環境是否存在
if not exist "..\venv\Scripts\activate.bat" (
    echo 🔧 虛擬環境不存在，正在建立...
    call setup_venv.bat
    if %errorlevel% neq 0 (
        echo ❌ 錯誤: 虛擬環境建立失敗。
        pause
        exit /b 1
    )
) else (
    echo ✅ 找到虛擬環境
)

REM 啟動虛擬環境
echo 🔌 啟動虛擬環境...
call venv\Scripts\activate.bat

REM 檢查是否存在 requirements.txt
if not exist "requirements.txt" (
    echo ❌ 錯誤: 找不到 requirements.txt 檔案。
    pause
    exit /b 1
)

REM 檢查依賴項是否已安裝
echo 📦 檢查依賴項...
pip list | findstr streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo � 安裝依賴項...
    pip install -r requirements.txt
    
    if %errorlevel% neq 0 (
        echo ❌ 錯誤: 依賴項安裝失敗。
        pause
        exit /b 1
    fi
)

echo ✅ 依賴項檢查完成。
echo.

REM 啟動 Streamlit 應用程式
echo 🌐 啟動 Streamlit 應用程式...
echo 應用程式將在瀏覽器中開啟 http://localhost:8501
echo.
echo 使用 Ctrl+C 停止應用程式
echo ======================================================

streamlit run app.py

REM 停用虛擬環境
deactivate

pause