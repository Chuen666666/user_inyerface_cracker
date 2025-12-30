# User Inyerface Cracker
一個用程式暴力破解並速通 [User Inyerface](https://userinyerface.com/) 的有趣小工具，通過腳本自動控制 Chrome 來速通它。

## 環境要求
- Python（3.9~3.12）
- Google Chrome
- Windows 10/11（不支援 Docker/WSL/Linux/macOS）

> 執行程式時，視窗焦點需在自動執行的 Chrome 上，建議執行完程式後就不要點擊滑鼠，直至程式結束

## 使用方式
### 1. 下載檔案
```bash
git clone https://github.com/Chuen666666/user_inyerface_cracker.git
cd user_inyerface_cracker
```

### 2. 安裝 Python 依賴
```bash
pip install -r requirements.txt
```

### 3. 執行檔案
- 建議使用管理員權限來執行 `main.py`，執行程式後，它會自動建立一個新的 Chrome 頁面，待它自然開始跑即可
- 第一次執行程式時，有一定概率失敗（卡在某步驟不動），關掉 Chrome 和程式（使用 <kbd>Ctrl</kbd> <kbd>C</kbd>）後，重新執行 `main.py` 即可
- 腳本執行完後，輸入法被切成英打為正常現象，腳本開始前無需理會目前在哪個輸入法
- 不出意外的話，過關時間應該可以壓在 6~7 秒內
- 程式結束後，可按下 <kbd>Enter</kbd>（視窗焦點無所謂）來自動關閉 Chrome 視窗