# WESLEY BERNARDES (020321) & LUCAS FARIA (019790)

from machine import Pin, I2C, PWM
import dht
import time
import ssd1306
import random

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sensor = dht.DHT22(Pin(14))

pino_servo = PWM(Pin(4))
pino_servo.freq(50)

led_green = Pin(25, Pin.OUT)
led_yellow = Pin(26, Pin.OUT)
led_red = Pin(27, Pin.OUT)

def acionar_bomba(angulo):
    duty = int((angulo / 18 + 2.5) * 65536 / 100)
    pino_servo.duty_u16(duty)

while True:
    sensor.measure()

    # 1 - Configuração inicial e leitura dos sensores

    temp = sensor.temperature() + random.randint(-5, 5)
    umid = sensor.humidity() + random.randint(-5, 5)

    bomba_status = "DESLIGADA"

    led_green.off()
    led_yellow.off()
    led_red.off()

    # 2 - Exibição dos dados no visor LCD SSD1306

    oled.fill(0)
    oled.text("Temp: {:.1f} C".format(temp), 0, 0)
    oled.text("Umid: {:.1f} %".format(umid), 0, 16)

    # 3 - Alertas visuais com LEDs

    if temp >= 20 and temp <= 25:
        led_green.on()
    elif temp >= 26 and temp <= 30:
        led_yellow.on()        
    elif temp > 30 or temp < 20:
        led_red.on()

    # 4 - Refinanndo o sistema de alerta

    if umid < 40 or umid > 70:
        led_yellow.on()
        time.sleep(0.2)
        
        led_yellow.off()
        time.sleep(0.2)

    # 5 - Servo motor e irrigação

    if umid < 30:
        bomba_status = "FORTE"
        acionar_bomba(90)
    elif umid >= 30 and umid < 60:
        bomba_status = "MODERADA"
        acionar_bomba(30)
    elif umid >= 60:
        bomba_status = "DESLIGADA"
        acionar_bomba(0)

    oled.text("Status: {}".format(bomba_status), 0, 32)

    # print("Temp: {:.1f}C | Umid: {:.1f}% | Status: {}".format(temp, umid, bomba_status))

    # 6 - Automação avançada e feedback contínuo

    if temp < 20 or temp > 25:
        print("Saiu da temperatura ideal {}C".format(temp)) 

    if umid < 30 or umid > 70:
        print("Saiu da umidade ideal: {}%".format(umid)) 

    oled.show()

    time.sleep(2)