# ros-yolov8-predict
Python 3 script for a ROS 2 node that subscribes to an image topic and then publishes the predictions.

## Getting Started
### Prerequisites
In order to run the ROS node, [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) needs to be installed in your Python environment. To install the package and its dependencies with PIP:
```bash
pip install ultralytics
```

### Installation
1. Clone the repo into the _src_ folder of your ROS Catkin workspace.
   ```bash
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Build this package in your Catkin workspace. In your workspace directory:
   ```bash
   catkin_make
   ```

## Usage
Before starting the node, make sure that images are first being published to the ROS topic `/flir_camera/image_raw/compressed`.

To run the node:
```
rosrun yolo_predict predict.py
```

The predictions of these images will be published as images to the topic `yolo_prediction/compressed`.
