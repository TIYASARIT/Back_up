# This code actually extracts all the frames from a video
import cv2
import os
# from PIL import Image

cam = cv2.VideoCapture('/home/ts4781/Downloads/IMG_7787.mp4')
current_frame = 0

try:
    if not os.path.exists('/home/ts4781/Data_3D Gaussian/Data'):
        os.makedirs('/home/ts4781/Data_3D Gaussian/Data')
except OSError:
    print ('Error: Creating directory of data')
  
path = '/home/ts4781/Data_3D Gaussian/Data'
while True:
    ret, frame = cam.read()
    if ret == False:
        cam.release()
        break
    current_frame = current_frame + 1 
    cv2.imwrite(f"{path}/{current_frame}.jpg",frame)
    print('Creating... frame '+ str(current_frame))
cam.release()
cv2.destroyAllWindows()
