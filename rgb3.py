import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def main():
    rojo()
    verde()
    azul()
    
def rojo():
    GPIO.setup(23, GPIO.OUT)
    rojo = GPIO.PWM(23, 100)
    rojo.start(0)
    
    for i in range(100,-1,-1):
        rojo.ChangeDutyCycle(100 - i)
        time.sleep(0.02) 
    for i in range(1,100,+1):
        rojo.ChangeDutyCycle(100 - i)
        time.sleep(0.02)  
        
    print("Ciclo rojo completo")
    
def verde():
    GPIO.setup(24, GPIO.OUT)
    verde = GPIO.PWM(24, 100)
    verde.start(0) 
    
    for i in range(100,-1,-1):
        verde.ChangeDutyCycle(100 - i)
        time.sleep(0.02) 
    for i in range(1,100,+1):
        verde.ChangeDutyCycle(100 - i)
        time.sleep(0.02)  
        
    print('Ciclo verde completo')
    
def azul():
    GPIO.setup(25, GPIO.OUT)
    azul = GPIO.PWM(25, 100)
    azul.start(0)   
    
    for i in range(100,-1,-1):
        azul.ChangeDutyCycle(100 - i)
        time.sleep(0.02) 
    for i in range(1,100,+1):
        azul.ChangeDutyCycle(100 - i)
        time.sleep(0.02)  
        
    print('Ciclo azul completo')
    
main()
