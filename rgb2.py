# importamos la libreria GPIO
import RPi.GPIO as GPIO
# desactivamos mensajes de error
GPIO.setwarnings(False)
# guardamos en una variable los pines GPIO que usaremos
led_pinR=23
led_pinG=24
led_pinB=25
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# indicamos que los puertos GPIO son de salida de corriente
GPIO.setup(led_pinR,GPIO.OUT)
GPIO.setup(led_pinG,GPIO.OUT)
GPIO.setup(led_pinB,GPIO.OUT)
# guardamos en una variable el valor de PWM para los GPIO
pwm_ledR=GPIO.PWM(led_pinR,500)
pwm_ledG=GPIO.PWM(led_pinG,500)
pwm_ledB=GPIO.PWM(led_pinB,500)
# iniciamos el led con longitud de pulso 0 para los GPIO
pwm_ledR.start(0)
pwm_ledG.start(0)
pwm_ledB.start(0)
# definimos una función que actualiza el pulso de los GPIO
def Led_On(duty_s_R,duty_s_G,duty_s_B):
    pwm_ledR.ChangeDutyCycle(int(duty_s_R))
    pwm_ledG.ChangeDutyCycle(int(duty_s_G))
    pwm_ledB.ChangeDutyCycle(int(duty_s_B))
# bucle que nos pide los valores de pulso de los GPIO
# y llama a la función para actualizar los colores del LED
while (True):
    # introducimos los valores de pulso para cada GPIO
    duty_s_R=input("Enter brightness R (0 to 100):")
    duty_s_G=input("Enter brightness G (0 to 100):")
    duty_s_B=input("Enter brightness B (0 to 100):")
    # llamamos a la función para actualizar el LED
    Led_On(duty_s_R,duty_s_G,duty_s_B)
    # esta linea indica que hay que hacer Intro para volver
    # a poner los valores
    input("Pulse Intro para introducir nuevos valores...")
