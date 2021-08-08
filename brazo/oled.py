#Import the library for controlling the OLED screen and delay time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

#Instantiate the object used to control the OLED
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

#Write the text "ROBOT" at the position (0, 20) on the OLED scren
while True:
    with canvas(device) as draw:
        for i in range(0,127,4):
            for j in range(0,63,4):
                    draw.text((i,j),".",fill="white")
        #time.sleep(1)
        for i in range(0,127,4):
            for j in range(0,63,4):
                    draw.text((i,j),"X",fill="white")

# while True:
    # time.sleep(1000)
