# 🐍 虛擬環境使用指南

## 為什麼使用虛擬環境？

虛擬環境是 Python 開發的最佳實踐，它可以：
- 🔒 **隔離依賴項**：避免不同專案間的套件版本衝突
- 🧹 **保持系統乾淨**：不會污染全域 Python 環境
- 📦 **精確重現環境**：確保在不同機器上有一致的執行環境
- 🚀 **提升開發效率**：避免「在我的電腦上沒問題」的情況

## 🚀 快速開始

### Windows 用戶

1. **建立虛擬環境**
   ```cmd
   setup_windows.bat
   ```
   或者：
   ```cmd
   scripts\windows\setup_venv.bat
   ```
   這個腳本會：
   - 建立名為 `venv` 的虛擬環境
   - 升級 pip 到最新版本
   - 安裝 requirements.txt 中的所有依賴項

2. **執行應用程式**
   ```cmd
   run_windows.bat
   ```
   或者：
   ```cmd
   scripts\windows\run_in_venv.bat
   ```
   或者手動操作：
   ```cmd
   # 啟動虛擬環境
   venv\Scripts\activate.bat
   
   # 執行應用程式
   streamlit run app.py
   
   # 停止虛擬環境 (可選)
   deactivate
   ```

### Linux/Mac 用戶

1. **建立虛擬環境**
   ```bash
   bash setup_linux.sh
   ```
   或者：
   ```bash
   bash scripts/linux/setup_venv.sh
   ```

2. **執行應用程式**
   ```bash
   bash run_linux.sh
   ```
   或者：
   ```bash
   bash scripts/linux/run_in_venv.sh
   ```
   或者手動操作：
   ```bash
   # 啟動虛擬環境
   source venv/bin/activate
   
   # 執行應用程式
   streamlit run app.py
   
   # 停止虛擬環境 (可選)
   deactivate
   ```

## 🔧 詳細操作說明

### 檢查虛擬環境狀態
當虛擬環境啟動時，命令列前會顯示 `(venv)`：
```
(venv) C:\your\path> 
```

### 查看已安裝的套件
```bash
pip list
```

### 安裝新套件 (在虛擬環境中)
```bash
pip install package_name
```

### 更新 requirements.txt
如果你安裝了新套件，記得更新 requirements.txt：
```bash
pip freeze > requirements.txt
```

### 重新建立虛擬環境
如果虛擬環境損壞，可以刪除並重新建立：

**Windows:**
```cmd
rmdir /s /q venv
scripts\setup_venv.bat
```

**Linux/Mac:**
```bash
rm -rf venv
bash scripts/setup_venv.sh
```

## 🎯 自動化執行

如果你想要最簡單的體驗，直接使用：
- Windows: `setup_windows.bat` 然後 `run_windows.bat`
- Linux/Mac: `bash setup_linux.sh` 然後 `bash run_linux.sh`

這些腳本會自動：
1. 檢查虛擬環境是否存在
2. 如果不存在，自動建立
3. 啟動虛擬環境
4. 檢查並安裝依賴項
5. 執行應用程式

## 🚨 常見問題

### Q: 執行 setup_venv 時出現權限錯誤
**A:** 在 Windows 上，可能需要以管理員身分執行命令提示字元。

### Q: Python 找不到指令
**A:** 確保 Python 已正確安裝並加入到 PATH 環境變數中。

### Q: 虛擬環境啟動失敗
**A:** 檢查 Python 版本是否支援 venv 模組（Python 3.3+）。

### Q: 套件安裝失敗
**A:** 嘗試升級 pip：
```bash
python -m pip install --upgrade pip
```

### Q: 如何完全移除虛擬環境
**A:** 直接刪除 `venv` 資料夾即可：
```bash
# Windows
rmdir /s /q venv

# Linux/Mac  
rm -rf venv
```

## 💡 最佳實踐建議

1. **總是使用虛擬環境**：即使是簡單的專案也建議使用
2. **不要將虛擬環境加入版本控制**：`venv/` 已在 `.gitignore` 中
3. **定期更新依賴項**：保持套件的安全性和相容性
4. **使用明確的版本號**：在 requirements.txt 中指定確切版本
5. **專案結束後清理**：刪除不再需要的虛擬環境

---

**🎉 現在你可以在隔離且乾淨的環境中享受 Python 開發了！**