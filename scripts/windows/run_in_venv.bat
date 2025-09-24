@echo off
chcp 65001 > nul

echo 🔌 在虛擬環境中啟動應用程式...
echo ======================================================

REM 檢查虛擬環境是否存在並啟動
if exist "..\..\venv\Scripts\activate.bat" (
    echo ✅ 啟動虛擬環境...
    call ..\..\venv\Scripts\activate.bat
    
    echo 📊 虛擬環境資訊:
    echo 當前 Python 路徑: 
    where python
    echo 當前 pip 版本:
    pip --version
    echo.
    
    echo 🌐 啟動 Streamlit 應用程式...
    echo 應用程式將在瀏覽器中開啟 http://localhost:8501
    echo.
    echo 使用 Ctrl+C 停止應用程式
    echo ======================================================
    
    cd ..\..
    streamlit run app.py
    
    echo.
    echo 🔌 停用虛擬環境...
    deactivate
    
) else (
    echo ❌ 錯誤: 虛擬環境不存在。
    echo 💡 請先執行 setup_venv.bat 建立虛擬環境
)

pause