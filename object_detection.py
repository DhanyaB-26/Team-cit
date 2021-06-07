#Yolov5 installation
%cd yolov5
%pip install -qr requirements.txt  # install dependencies

import torch
from IPython.display import Image, clear_output  # to display images

clear_output()
print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

# unzipping the training model
!unzip "/content/train_data.zip" -d "/content/sample_data"

# Training the model
!python train.py --img 640 --batch 16 --epochs 200 --data custom.yaml --weights yolov5s.pt --nosave --cache
# custom.yaml - the file we customised from coco128.yaml
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
train: ../train_data/images/train/  # 128 images
val: ../train_data/images/val/  # 128 images

# number of classes
nc: 1

# class names
names: [ 'obstacle' ]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# the video detection line
!python detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.35 --source ../train.mp4
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
