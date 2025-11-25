from machine import Pin, I2C
import ssd1306

import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

temperaturas = [5, 15, 20, 30]

def mensagem_por_temp(temp):
    if temp < 10:
        return "Muito Frio!"
    elif 10 <= temp <= 25:
        return "Temperatura\nAgradavel!"
    else:
        return "Muito Quente!"

while True:
    for temp in temperaturas:
        paddingY = 16

        oled.fill(0)
        oled.text("Temp: {}°C".format(temp), 0, 0)


        for linha in mensagem_por_temp(temp).split("\n"):
            oled.text(linha, 0, paddingY)
            paddingY += 12

        oled.show()

        time.sleep(2)