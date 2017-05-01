#define o tempo que o led ficara aceso ou apagado
time = 2
pin_default = 12
 
#Define biblioteca da GPIO
import RPi.GPIO as GPIO
 
#Define biblioteca de tempo
import time                           
GPIO.setmode(GPIO.BOARD)
 
#Define o pino 12 da placa como saida
GPIO.setup(pin_default, GPIO.OUT)
 
#rotina para acender o led
def acendeled(pin_led = pin_default):
    GPIO.output(pin_led, 1)
    return
 
#rotina para apagar o led
def apagaled(pin_led = pin_default):
    GPIO.output(pin_led, 0)
    return
 
#Inicia loop
while(1):      
  #Acende o led
  acendeled()
  #Aguarda  segundo
  time.sleep(time)
  #apaga o led
  apagaled()
  #Aguarda meio segundo e reinicia o processo
  time.sleep(time)
