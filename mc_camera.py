from mcpi import minecraft
import RPi.GPIO as gpio
import time


mc = minecraft.Minecraft.create()

def my_callback(self):
    global camera
    if camera == True:
        mc.camera.setNormal()
        camera  = False
    else:
        mc.camera.setFollow(mc.getPlayerEntityIds())
        camera = True

camera = False

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.add_event_detect(17, gpio.RISING, callback=my_callback, bouncetime =200)
try:
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

gpio.cleanup()
