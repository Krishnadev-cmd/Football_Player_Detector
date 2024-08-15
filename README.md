# YOLOv10 Video Object Detection

This script performs object detection on a video using a YOLOv10 model. It annotates each frame with bounding boxes and labels, and displays the annotated video in real-time.

## Features

- **Object Detection**: Uses a YOLOv10 model to detect objects in each frame of the video.
- **Annotations**: Draws bounding boxes and labels around detected objects.
- **Real-time Display**: Shows the annotated video frame by frame.

## Installation

To run this script, you need to have Python and the required packages installed. Follow these steps to set up your environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/yolov10-video-object-detection.git
    cd yolov10-video-object-detection
    ```

2. **Install the required packages**:
    ```bash
    pip install opencv-python numpy ultralytics supervision
    ```

3. **Download YOLOv10 Model Weights**:
    - Ensure you have the YOLOv10 model weights (`best.pt`) in the specified path:
      ```
      C:/Krishnadev/Projects/YOLO_V10/YOLO_V10_1/YOLO_V10/runs/detect/train/weights/best.pt
      ```

## Usage

1. **Prepare your video file**:
    - Place your video file (`videoplayback.mp4`) in the working directory or update the `video_path` variable in the script to point to your video file.

2. **Run the script**:
    ```bash
    python detect_objects.py
    ```

   The script will:
    - Load the YOLOv10 model.
    - Open and read the video file frame by frame.
    - Perform object detection on each frame.
    - Annotate the frame with bounding boxes and labels.
    - Display the annotated video in a new window.

3. **Exit the video display**:
    - Press `q` while the video window is active to exit the video display.

## Dependencies

- `opencv-python`: For video processing and display.
- `numpy`: For numerical operations.
- `ultralytics`: For YOLOv10 model.
- `supervision`: For frame annotation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or suggestions, please contact [your-email@example.com].

