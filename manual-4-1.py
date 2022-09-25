from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_preview_configuration()

for k, v in config.items():
    print(f"{k}: {v}")
 
# picam2.configure(config)
# picam2.start()
