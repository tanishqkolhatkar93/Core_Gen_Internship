import cv2
from ultralytics import YOLO
import json
from datetime import datetime

# 1. Load Pre-trained YOLOv8 Model
# It detects 80 classes by default, including Cell Phone and Eyeglasses (Specs)
model = YOLO('yolov8n.pt') 

# Define your specific target labels (COCO mapping)
# Note: 'Pen' and 'Pencil' are often detected as 'toothbrush' or 'remote' in base COCO.
# For high accuracy on Pens/Pencils, a custom-tuned weight is usually best.
TARGET_LABELS = {
    'cell phone': 'Mobile',
    'eyeglasses': 'Chasma (Specs)',
    'Pen': 'Pen/Pencil (Visual Proxy)', # Closest base COCO class
    'remote': 'Pen/Pencil (Visual Proxy)'
}

def start_detection():
    cap = cv2.VideoCapture(0) # Open Webcam
    print(" AI System: Active. Press 'q' to exit.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break

        # 2. Run Inference (Stream mode for real-time speed)
        results = model(frame, stream=True, conf=0.3)

        report_data = []

        for r in results:
            annotated_frame = r.plot() # Draws boxes automatically
            
            for box in r.boxes:
                class_id = int(box.cls)
                label = model.names[class_id]
                
                # 3. Label-based Reporting Logic
                timestamp = datetime.now().strftime("%H:%M:%S")
                confidence = float(box.conf)
                
                # Check if it's one of your target items
                display_label = TARGET_LABELS.get(label, label)
                
                report_entry = {
                    "time": timestamp,
                    "item": display_label,
                    "confidence": f"{confidence:.2f}"
                }
                report_data.append(report_entry)

        # 4. Display Real-time Video
        cv2.imshow("Object Detection - Master Thesis Project", annotated_frame)
        
        # Print detected items to console for reporting
        if report_data:
            print(f"Report Update: {report_data}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_detection()