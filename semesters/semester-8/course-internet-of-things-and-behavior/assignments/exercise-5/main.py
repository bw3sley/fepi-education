# WESLEY BERNARDES (020321) e LUCAS GERALDO (019790)

from machine import Pin, I2C, PWM, ADC
import ssd1306
import dht
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

dht22 = dht.DHT22(Pin(12))

mq2 = ADC(Pin(34))
mq2.atten(ADC.ATTN_11DB)

servo = PWM(Pin(4))
servo.freq(50)

def set_servo_angle(angle_deg: int) -> int:
    angle = max(0, min(180, int(angle_deg)))

    duty_percent = (angle / 18.0) + 2.5
    duty_u16 = int(duty_percent * 65536 / 100)
    servo.duty_u16(duty_u16)

    return angle

led_verde    = Pin(27, Pin.OUT)
led_amarelo  = Pin(25, Pin.OUT)
led_vermelho = Pin(26, Pin.OUT)

def configurar_leds(qualidade: str):
    led_verde.off(); led_amarelo.off(); led_vermelho.off()

    if qualidade == "Boa":
        led_verde.on()
    elif qualidade == "Moderada":
        led_amarelo.on()
    else:
        led_vermelho.on()

def classificar_ar_e_acao(gas_adc: int):
    if gas_adc < 2000:
        return "Boa", 0
    elif gas_adc < 3000:
        return "Moderada", 30
    else:
        return "Ruim", 90

def mostrar_display_oled(temp_c, umid_pct, gas_adc, qualidade, servo_deg):
    oled.fill(0)
    oled.text("Temp: {:.1f}C".format(temp_c), 0, 0)
    oled.text("Umid: {:.1f}%".format(umid_pct), 0, 12)
    oled.text("Gas: {}".format(gas_adc), 0, 24)
    oled.text("Ar: {}".format(qualidade), 0, 36)
    oled.text("Servo: {}deg".format(servo_deg), 0, 48)
    oled.show()

def main():
    set_servo_angle(0)

    while True:
        dht22.measure()
        temp = dht22.temperature()
        umid = dht22.humidity()

        gas = mq2.read()

        qualidade, alvo = classificar_ar_e_acao(gas)
        angulo = set_servo_angle(alvo)
        configurar_leds(qualidade)

        print("Temp: {:.1f}C  Umid: {:.1f}%  Gas: {}  Qualidade: {}  Servo: {}deg".format(
            temp, umid, gas, qualidade, angulo
        ))

        mostrar_display_oled(temp, umid, gas, qualidade, angulo)

        time.sleep(5)

main()
