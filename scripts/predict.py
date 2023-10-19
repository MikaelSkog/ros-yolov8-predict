import rospy
import sensor_msgs.msg
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class Predicter():
    def __init__(self):
        rospy.loginfo('YOLOv8 predicter initialized.')
        self.img_obtained = False # Whether at least one image has been received.
        self.received_img = None  # Last received image.
        self.bridge = CvBridge()

        # Use 'last.pt' for the model weights (located in working dir when running the node).
        model = YOLO('last.pt')

        # Make this node both a subscriber and publisher.
        self.pub = rospy.Publisher('yolo_prediction/compressed', sensor_msgs.msg.CompressedImage, queue_size=0)
        rospy.Subscriber('/flir_camera/image_raw/compressed', sensor_msgs.msg.CompressedImage, self.callback)

        while not rospy.is_shutdown():
            # If at least one image been received.
            if self.img_obtained:
                # Resize the received image to 512 x 512.
                self.received_img = cv2.resize(self.received_img, (512, 512))

                # Predict bounding boxes and segmentation masks with YOLOv8.
                results = model.predict(self.received_img)
                annotated_img = results[0].plot()

                # Publish message of image with predictions.
                msg_to_publish = self.bridge.cv2_to_compressed_imgmsg(annotated_img)
                self.pub.publish(msg_to_publish)

    def callback(self, received_msg):
        # Get image message.
        self.received_img = self.bridge.compressed_imgmsg_to_cv2(received_msg, desired_encoding="rgb8")
        self.img_obtained = True


if __name__ == '__main__':
    rospy.init_node('predict')
    predicter = Predicter()