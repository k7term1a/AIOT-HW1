@echo off
chcp 65001 > nul

echo 🔧 建立 Python 虛擬環境...
echo ======================================================

REM 檢查是否安裝了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤: 找不到 Python。請先安裝 Python。
    pause
    exit /b 1
)

echo 📦 Python 版本:
python --version

REM 刪除現有的虛擬環境（如果存在）
if exist "..\..\venv" (
    echo 🗑️ 刪除現有虛擬環境...
    rmdir /s /q ..\..\venv
)

REM 建立新的虛擬環境
echo 🚀 建立新的虛擬環境...
cd ..\..
python -m venv venv

if %errorlevel% neq 0 (
    echo ❌ 錯誤: 虛擬環境建立失敗。
    pause
    exit /b 1
)

echo ✅ 虛擬環境建立成功！

REM 啟動虛擬環境
echo 🔌 啟動虛擬環境...
call venv\Scripts\activate.bat

if %errorlevel% neq 0 (
    echo ❌ 錯誤: 虛擬環境啟動失敗。
    pause
    exit /b 1
)

echo ✅ 虛擬環境已啟動！

REM 升級 pip
echo 📊 升級 pip...
python -m pip install --upgrade pip

REM 安裝依賴項
if exist "requirements.txt" (
    echo 📦 安裝專案依賴項...
    pip install -r requirements.txt
    
    if %errorlevel% neq 0 (
        echo ❌ 錯誤: 依賴項安裝失敗。
        pause
        exit /b 1
    )
    
    echo ✅ 所有依賴項安裝完成！
) else (
    echo ⚠️  警告: 找不到 requirements.txt 檔案。
)

echo.
echo 🎉 虛擬環境設定完成！
echo ======================================================
echo 💡 使用說明:
echo    1. 啟動虛擬環境: venv\Scripts\activate.bat
echo    2. 執行應用程式: python -m streamlit run app.py
echo    3. 停止虛擬環境: deactivate
echo ======================================================

cd scripts\windows
pause