# ros-yolov8-predict
Python 3 script for a ROS node that subscribes to an image topic and then publishes the predictions.

## Getting Started
### Prerequisites
In order to run the ROS node, [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) needs to be installed in your Python environment. To install the package and its dependencies with PIP:
```
pip3 install ultralytics
```

### Installation
1. Clone the repo into the _src_ folder of your ROS Catkin workspace.
   ```
   git clone https://github.com/MikaelSkog/ros-yolov8-predict.git
   ```
2. Build this package in your Catkin workspace. In your workspace directory, execute
   ```
   catkin_make
   ```

## Usage
Before starting the node, make sure that images are being published to the ROS topic `/flir_camera/image_raw/compressed`.

To run the node, execute the following command:
```
rosrun yolo_predict <path_to_model>
```
where `<path_to_model>` specifies the path of the model.

The predictions of these images will be published as images to the topic `yolo_prediction/compressed`.
