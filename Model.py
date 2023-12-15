from ultralytics import YOLO
import os 


model = YOLO('yolov8n.pt')

data_path = "data"



results = model.train(data = "C:\SCHOOL\Project-3\data\data.yaml", epochs=50, imgsz=900, batch = 12)
