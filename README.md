# User Inyerface Cracker
一個用程式暴力破解並速通 [User Inyerface](https://userinyerface.com/) 的有趣小工具，通過腳本自動控制 Chrome 來速通它。

## 環境要求
- Python
- Chrome
- Windows（系統管理員權限）

## 使用方式
### 1. 下載檔案
```bash
git clone https://github.com/Chuen666666/user_inyerface_cracker.git
cd user_inyerface_cracker
```

### 2. 下載 Python 依賴
```bash
pip install -r requirements.txt
```

### 3. 執行檔案
- 建議使用管理員權限來執行 `main.py`，執行程式後，它會自動建立一個新的 Chrome 頁面，待它自然開始跑即可
- 第一次執行程式時，有一定概率失敗（卡在某步驟不動），關掉 Chrome 和程式（使用 <kbd>Ctrl</kbd> <kbd>C</kbd>）後，重新執行 `main.py` 即可
- 腳本執行完後，輸入法被切成英打為正常現象，腳本開始前無需理會目前在哪個輸入法
- 不出意外的話，過關時間應該可以壓在 7 秒內