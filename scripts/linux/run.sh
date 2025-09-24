#!/bin/bash

# 線性迴歸 CRISP-DM 專案啟動腳本

echo "🚀 啟動線性迴歸 CRISP-DM 分析應用程式..."
echo "======================================================"

# 優先使用 python3，如果沒有則使用 python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ 錯誤: 找不到 Python。請先安裝 Python。"
    exit 1
fi

# 檢查虛擬環境是否存在
if [ ! -f "venv/bin/activate" ]; then
    echo "🔧 虛擬環境不存在，正在建立..."
    bash setup_venv.sh
    if [ $? -ne 0 ]; then
        echo "❌ 錯誤: 虛擬環境建立失敗。"
        exit 1
    fi
else
    echo "✅ 找到虛擬環境"
fi

# 啟動虛擬環境
echo "🔌 啟動虛擬環境..."
source venv/bin/activate

# 檢查是否存在 requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo "❌ 錯誤: 找不到 requirements.txt 檔案。"
    exit 1
fi

# 檢查依賴項是否已安裝
echo "📦 檢查依賴項..."
if ! pip list | grep -q streamlit; then
    echo "� 安裝依賴項..."
    pip install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "❌ 錯誤: 依賴項安裝失敗。"
        exit 1
    fi
fi

echo "✅ 依賴項檢查完成。"
echo ""

# 啟動 Streamlit 應用程式
echo "🌐 啟動 Streamlit 應用程式..."
echo "應用程式將在瀏覽器中開啟 http://localhost:8501"
echo ""
echo "使用 Ctrl+C 停止應用程式"
echo "======================================================"

streamlit run app.py

# 停用虛擬環境
deactivate