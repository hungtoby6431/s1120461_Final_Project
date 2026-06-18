from ultralytics import YOLO

if __name__ == '__main__':
    # 1. 載入訓練好的訓練模型
    model = YOLO('runs/detect/Final_Project/s1120461_run2-3/weights/best.pt') 

    # 2. 指定測試影片
    test_video_path = 'test video.MOV' 

    print(" 開始進行影片辨識...")
    
    # 3. 執行預測
    results = model.predict(source=test_video_path, save=True, show=True, conf=0.4)
    
    print(" 預測完畢！請至 runs/detect/predict 資料夾查看影片檔！")