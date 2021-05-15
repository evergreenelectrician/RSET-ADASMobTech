# LeylandVehicleDetection

Basic algorithm


It comprises of object detection with computer vision and a radar system to detect the traffic ahead of the vehicle and warn the driver on the possibility of a collision.
The system uses YOLO algorithm which is an object detection pipeline based on Neural Network.
The camera mounted in front of the vehicle collects the real time traffic in front of the vehicle and this data is then processed and is given to the system where YOLO frame object detection as a regression problem to spatially separated bounding boxes and associated class probabilities , A single neural network predicts bounding boxes and class probabilities directly thus enabling us to predict if the vehicle in front is in the collision course.

The system also uses RADAR in order to make more accurate predictions , as during night time there is a chance of failure for visual computation.
The radar detects the distance between the truck and the vehicle in front of it , Thus alerting the driver in case it leads to collision.
