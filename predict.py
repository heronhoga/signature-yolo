from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict("https://ultralytics.com/assets/signature-s.mp4", save=True)