from machine import Pin
import utime
led = Pin(25, Pin.OUT)
buzzer = Pin(22, Pin.OUT)
sensor = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
exception=False
def blink():
    led.toggle()
    buzzer.toggle()    
def stop():
    led.off()
    buzzer.off()
while True:
    if sensor.value() == 1:
        blink()
        stop()
    if sensor.value() == 0:
        stop()
