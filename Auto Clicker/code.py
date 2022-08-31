import usb_hid, time
import board, digitalio
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
led=digitalio.DigitalInOut(board.GP25)
led.direction=digitalio.Direction.OUTPUT

led.value=False

n=0
time.sleep(5)
while n<1000:
    mouse.click(Mouse.LEFT_BUTTON)
    led.value=True
    n+=1
    time.sleep(0.02)
    led.value=False