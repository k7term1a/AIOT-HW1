#!/bin/bash

# 設定 UTF-8 編碼
export LANG=zh_TW.UTF-8

echo "🔧 建立 Python 虛擬環境..."
echo "======================================================"

# 檢查是否安裝了 Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ 錯誤: 找不到 Python。請先安裝 Python。"
    exit 1
fi

# 優先使用 python3，如果沒有則使用 python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

echo "📦 Python 版本:"
$PYTHON_CMD --version

# 切換到上層目錄
cd ../..

# 刪除現有的虛擬環境（如果存在）
if [ -d "venv" ]; then
    echo "🗑️ 刪除現有虛擬環境..."
    rm -rf venv
fi

# 建立新的虛擬環境
echo "🚀 建立新的虛擬環境..."
$PYTHON_CMD -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ 錯誤: 虛擬環境建立失敗。"
    exit 1
fi

echo "✅ 虛擬環境建立成功！"

# 啟動虛擬環境
echo "🔌 啟動虛擬環境..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ 錯誤: 虛擬環境啟動失敗。"
    exit 1
fi

echo "✅ 虛擬環境已啟動！"

# 升級 pip
echo "📊 升級 pip..."
pip install --upgrade pip

# 安裝依賴項
if [ -f "requirements.txt" ]; then
    echo "📦 安裝專案依賴項..."
    pip install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "❌ 錯誤: 依賴項安裝失敗。"
        exit 1
    fi
    
    echo "✅ 所有依賴項安裝完成！"
else
    echo "⚠️  警告: 找不到 requirements.txt 檔案。"
fi

echo ""
echo "🎉 虛擬環境設定完成！"
echo "======================================================"
echo "💡 使用說明:"
echo "   1. 啟動虛擬環境: source venv/bin/activate"
echo "   2. 執行應用程式: streamlit run app.py"
echo "   3. 停止虛擬環境: deactivate"
echo "======================================================"

# 回到 scripts 目錄
cd scripts/linux