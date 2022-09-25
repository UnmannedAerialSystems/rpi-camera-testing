
```
sudo apt install -y python3-picamera2
sudo apt install -y python3-opencv
sudo apt install -y opencv-data
pip3 install tflite-runtime
sudo apt install -y ffmpeg
```

Followed the example code here: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

3.4 _The NULL preview is in fact started automatically whenever the camera system is started (picam2.start()) if no preview is yet running, which is why alternative preview windows must be started earlier._
