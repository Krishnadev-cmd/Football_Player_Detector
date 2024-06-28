from collections import defaultdict
import cv2 
import numpy as np
import supervision as sv
from ultralytics import YOLOv10

model = YOLOv10("C:/K/Projects/YOLO_V10/YOLO_V10_1/YOLO_V10/runs/detect/train/weights/best.pt")

# Open the video file
video_path = 'videoplayback.mp4'
cap = cv2.VideoCapture(video_path)

# Create annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLOv10 model on the frame
    results = model(frame_rgb)[0]
    detections = sv.Detections.from_ultralytics(results)

    # Annotate the frame
    annotated_frame = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections)

    # Display the annotated frame
    cv2.imshow('Annotated Video', annotated_frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()