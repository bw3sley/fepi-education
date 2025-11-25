# WESLEY BERNARDES (020321)

from machine import Pin, I2C, PWM
import ssd1306
import dht
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sensor = dht.DHT22(Pin(12))

pino_servo = PWM(Pin(4))
pino_servo.freq(50)

led_azul = Pin(14, Pin.OUT)     # < 18°C
led_verde = Pin(27, Pin.OUT)    # 18°C a 28°C
led_vermelho = Pin(26, Pin.OUT) # > 28°C
led_amarelo = Pin(25, Pin.OUT)  # Bomba ligada

def acionar_bomba(angulo):
    duty = int((angulo / 18 + 2.5) * 65536 / 100)
    pino_servo.duty_u16(duty)

def atualizar_leds_temperatura(temp):
    if temp < 18:
        led_azul.on()
        led_verde.off()
        led_vermelho.off()
        clima = "Frio"
    elif 18 <= temp <= 28:
        led_azul.off()
        led_verde.on()
        led_vermelho.off()
        clima = "Ideal"
    else:
        led_azul.off()
        led_verde.off()
        led_vermelho.on()
        clima = "Quente"

    return clima

def ler_dados():
    sensor.measure()
    umidade = sensor.humidity()
    temperatura = sensor.temperature()
    
    if umidade < 30:
        acionar_bomba(90)
        estado_bomba = "Forte"
        led_amarelo.on()
    elif umidade < 60:
        acionar_bomba(60)
        estado_bomba = "Moderada"
        led_amarelo.on()
    else:
        acionar_bomba(0)
        estado_bomba = "Desligada"
        led_amarelo.off()
    
    clima = atualizar_leds_temperatura(temperatura)
    
    print(f"Umidade: {umidade:.1f}% | Temperatura: {temperatura:.1f}°C | Bomba: {estado_bomba} | Clima: {clima}")
    
    oled.fill(0)
    oled.text("Umid: {:.1f}%".format(umidade), 0, 0)
    oled.text("Temp: {:.1f}C".format(temperatura), 0, 15)
    oled.text("Bomba: " + estado_bomba, 0, 30)
    oled.text("Clima: " + clima, 0, 45)
    oled.show()

while True:
    ler_dados()
    time.sleep(5)