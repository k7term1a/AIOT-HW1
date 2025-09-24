# 線性迴歸分析 - CRISP-DM 方法論實作

## 📋 專案概述

這是一個使用 CRISP-DM 方法論實作的線性迴歸分析專案，提供互動式網頁介面讓使用者調整模型參數並即時查看結果。

### 🎯 專案目標
- 實作完整的 CRISP-DM 六階段方法論
- 建立互動式線性迴歸模型 (y = ax + b)
- 提供參數調整功能 (斜率 a、截距 b、噪音等級、資料點數量)
- 使用 Streamlit 建立 Web 應用程式
- 支援 Docker 容器化部署

## 🔄 CRISP-DM 方法論實作

### 1. 商業理解 (Business Understanding)
- **目標**: 建立並分析線性關係模型
- **成功標準**: 建立良好擬合的線性迴歸模型
- **商業問題**: 能否透過線性關係預測 y 值？

### 2. 資料理解 (Data Understanding)
- 資料摘要統計
- 相關性分析
- 資料分佈視覺化
- 資料品質檢查

### 3. 資料準備 (Data Preparation)
- 缺失值檢查
- 資料型態驗證
- 訓練/測試資料分割
- 資料分佈分析

### 4. 建模 (Modeling)
- 簡單線性迴歸模型
- 參數估計
- 模型訓練與預測

### 5. 評估 (Evaluation)
- R² 決定係數
- RMSE 均方根誤差
- 殘差分析
- 模型效能視覺化

### 6. 部署 (Deployment)
- 互動式 Web 應用程式
- 即時參數調整
- Docker 容器化支援

## 🚀 快速開始

### 🐍 推薦方法：使用 Python 虛擬環境

虛擬環境可以避免套件衝突，是最佳實踐方式。

#### Windows 用戶：
1. **建立並設定虛擬環境**
   ```cmd
   setup_windows.bat
   ```
   或者：
   ```cmd
   scripts\windows\setup_venv.bat
   ```

2. **在虛擬環境中執行應用程式**
   ```cmd
   run_windows.bat
   ```
   或者：
   ```cmd
   scripts\windows\run_in_venv.bat
   ```
   或者手動操作：
   ```cmd
   venv\Scripts\activate.bat
   streamlit run app.py
   ```

#### Linux/Mac 用戶：
1. **建立並設定虛擬環境**
   ```bash
   bash setup_linux.sh
   ```
   或者：
   ```bash
   bash scripts/linux/setup_venv.sh
   ```

2. **在虛擬環境中執行應用程式**
   ```bash
   bash run_linux.sh
   ```
   或者：
   ```bash
   bash scripts/linux/run_in_venv.sh
   ```
   或者手動操作：
   ```bash
   source venv/bin/activate
   streamlit run app.py
   ```

### 方法二：自動設定執行

這些腳本會自動檢查並建立虛擬環境：

1. **Windows 用戶**
   ```cmd
   setup_windows.bat
   scripts\windows\run.bat
   ```

2. **Linux/Mac 用戶**
   ```bash
   bash setup_linux.sh
   bash scripts/linux/run.sh
   ```

### 方法三：本地執行（不建議）

1. **安裝依賴項**
   ```bash
   pip install -r requirements.txt
   ```

2. **運行應用程式**
   ```bash
   streamlit run app.py
   ```

3. **開啟瀏覽器**
   ```
   http://localhost:8501
   ```

### 方法四：Docker 部署

1. **建立 Docker 映像**
   ```bash
   docker build -t linear-regression-app .
   ```

2. **運行容器**
   ```bash
   docker run -p 8501:8501 linear-regression-app
   ```

3. **使用 Docker Compose**
   ```bash
   docker-compose up -d
   ```

## 📱 功能特色

### 🎛️ 互動式參數控制
- **斜率 (a)**: -10.0 到 10.0
- **截距 (b)**: -50.0 到 50.0
- **噪音等級**: 0.0 到 10.0
- **資料點數量**: 50 到 500

### 📊 視覺化圖表
- 迴歸擬合圖
- 殘差分析圖
- 預測值 vs 實際值
- 殘差分佈直方圖

### 📈 效能指標
- 訓練集 R²
- 測試集 R²
- 訓練集 RMSE
- 測試集 RMSE

### 🔮 即時預測
- 輸入 X 值進行即時預測
- 顯示預測值與真實值比較

## 📁 專案結構

```
hw1/
├── app.py                    # 主要應用程式 (完整 CRISP-DM 實作)
├── requirements.txt          # Python 依賴項
├── Dockerfile               # Docker 容器化設定
├── docker-compose.yml       # Docker Compose 配置
├── README.md               # 完整專案說明文件
├── VENV_GUIDE.md           # 虛擬環境詳細指南
├── 0_devlog.md             # 開發日誌與變更記錄
├── setup_windows.bat       # Windows 快速環境設定
├── setup_linux.sh          # Linux/Mac 快速環境設定
├── run_windows.bat          # Windows 快速執行
├── run_linux.sh            # Linux/Mac 快速執行
├── scripts/                # 腳本檔案目錄
│   ├── windows/            # Windows 專用腳本
│   │   ├── setup_venv.bat  # 虛擬環境建立腳本
│   │   ├── run.bat         # 自動執行腳本
│   │   └── run_in_venv.bat # 虛擬環境執行腳本
│   ├── linux/              # Linux/Mac 專用腳本
│   │   ├── setup_venv.sh   # 虛擬環境建立腳本
│   │   ├── run.sh          # 自動執行腳本
│   │   └── run_in_venv.sh  # 虛擬環境執行腳本
│   └── tests/              # 測試腳本
│       ├── test_app.py     # 應用程式測試
│       ├── test_lines.py   # 線條顯示測試
│       └── quick_test.py   # 快速功能驗證
├── .gitignore              # Git 忽略清單 (含虛擬環境)
└── venv/                   # Python 虛擬環境 (執行後產生)
```

## 🛠️ 技術棧

- **前端**: Streamlit
- **後端**: Python
- **機器學習**: scikit-learn
- **資料處理**: Pandas, NumPy
- **視覺化**: Matplotlib, Seaborn
- **容器化**: Docker, Docker Compose

## 📊 模型說明

### 數學模型
```
y = ax + b + ε
```
其中：
- `a`: 斜率參數
- `b`: 截距參數
- `ε`: 高斯噪音 (均值=0, 標準差=noise_level)

### 評估指標

1. **R² 決定係數**
   ```
   R² = 1 - (SS_res / SS_tot)
   ```

2. **均方根誤差 (RMSE)**
   ```
   RMSE = √(Σ(y_true - y_pred)² / n)
   ```

## 🎓 使用說明

1. **調整參數**: 使用左側邊欄的滑桿調整模型參數
2. **生成資料**: 點擊「Generate New Data」按鈕生成新的資料集
3. **查看結果**: 檢視 CRISP-DM 各階段的分析結果
4. **互動預測**: 在部署階段輸入 X 值進行預測

## 📝 開發紀錄

詳細的開發過程和變更記錄請參考 `0_devlog.md` 檔案。

## 🤝 貢獻

歡迎提出問題和建議！

## 📄 授權

此專案為學術用途。

---

**作者**: HW1 Linear Regression Project  
**日期**: 2025-09-24  
**版本**: 1.0.0