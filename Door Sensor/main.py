from machine import Pin
import utime
led = Pin(25, Pin.OUT)
buzzer = Pin(22, Pin.OUT)
sensor = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
def blink():
    led.toggle()
    buzzer.toggle()    
def stop():
    led.off()
    buzzer.off()
while True:
    val1= sensor.value()
    utime.sleep(0.01)
    val2= sensor.value()
    if val1 and not val2:
        print("Door Closed")
    elif not val1 and val2:
        blink()
        utime.sleep(2)
        stop()
