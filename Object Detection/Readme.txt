To Run the Code:
  I. Clone the repo using the repo's HTTPS link: git clone https://github.com/abrahamjerson/yolov4-deepsort.git
  II. Create a conda environment to utilize GPU
        conda env create -f conda-gpu.yml
        conda activate yolov4-gpu
  III. Install the requirements:  
         pip install -r requirements-gpu.txt
  IV. Download the Yolov4-Tiny weights from the link: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
  V. Save Yolov4-Tiny model: python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --model yolov4 --tiny
  VI. Run the model on the Video - "Traffic.mp4":
      python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ./data/Traffic.mp4 --output ./outputs/tiny.avi --tiny
