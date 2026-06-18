from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('yolov8n.pt') 

    print(" 啟動訓練引擎")
    results = model.train(
    data='Roboflow_Dataset/data.yaml', 
    epochs=50,
    imgsz=640,
    device=0,
    batch=16,
    project='Final_Project',            
    name='s1120461_run2'                
)
    
    print(" 訓練結束！")