# s1120461_Final_Project
# YZU 智慧校園：YOLOv8 滅火器偵測系統

本專題為元智大學「電腦視覺與影像處理概論」期末專題，使用 YOLOv8 模型進行校園滅火器之偵測。

## 系統環境與安裝指令
請確保您的電腦已安裝 Python 3.11 版本，並執行以下指令安裝所需套件：
`pip install ultralytics`

## 如何執行預測 (Inference)
1. 將測試影片放入專案目錄下。
2. 開啟 `predict.py`，確認影片檔名與路徑正確。
3. 於終端機執行以下指令：
`python predict.py`
程式將自動讀取 `best.pt` 權重，並輸出畫上邊界框的影片至 `runs/detect/` 資料夾中。

## 資料集來源
* 開源資料集：本專案結合了 [Roboflow Fire Extinguisher Dataset](https://universe.roboflow.com/nehalwork/fire-extinguisher-rw3ce) 進行混合訓練，以提升遠距離物件偵測能力。
