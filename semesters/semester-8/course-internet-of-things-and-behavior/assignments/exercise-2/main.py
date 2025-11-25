from machine import Pin, I2C
import dht
import time
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sensor = dht.DHT22(Pin(13))

led_green = Pin(27, Pin.OUT)
led_yellow = Pin(26, Pin.OUT)
led_red = Pin(25, Pin.OUT)

while True:
    sensor.measure()

    temp = sensor.temperature()
    umid = sensor.humidity()

    print("Temp: {:.1f} C | Umid: {:.1f} %".format(temp, umid))
    
    led_green.off()
    led_yellow.off()
    led_red.off()

    oled.fill(0)  # limpa
    oled.text("Monitor Temp", 0, 0)
    oled.text("Temp: {:.1f} C".format(temp), 0, 16)
    oled.text("Umid: {:.1f} %".format(umid), 0, 32)

    if temp <= 20:
        led_green.on()
        faixa = "FAIXA: VERDE"
    elif temp > 40:
        led_red.on()
        faixa = "FAIXA: VERM."
    elif temp > 30:
        faixa = "FAIXA: AMAR."
        led_yellow.on()

    oled.text(faixa, 0, 48)
    oled.show()