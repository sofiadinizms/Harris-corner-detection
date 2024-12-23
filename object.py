import cv2
import matplotlib.pyplot as plt


config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model =cv2.dnn_DetectionModel(frozen_model, config_file)
classLabels = []
file_name = 'labels.txt'
with open(file_name, 'rft') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
print(classLabels)