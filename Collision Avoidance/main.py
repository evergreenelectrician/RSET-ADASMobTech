from moviepy.editor import VideoFileClip
from yolo_pipeline import *
from lane import *


def pipeline_yolo(img):

    img_undist, img_lane_augmented, lane_info = lane_process(img)
    output = vehicle_detection_yolo(img_undist, img_lane_augmented, lane_info)

    return output

if __name__ == "__main__":

    video_output = 'examples/1_YOLO.mp4'
    clip1 = VideoFileClip("examples/1.mp4").subclip(3,15)
    clip = clip1.fl_image(pipeline_yolo)
    clip.write_videofile(video_output, audio=False)


