# this program blinks an LED on Arduino pin 13 for a second
import pyfirmata
import time

pin = 13              # pin on the Arduino to be used
port = '/dev/ttyACM0'  # com port for Arduino  
board = pyfirmata.Arduino(port)  # creates Arduino board object variable
board.digital[pin].write(1)   # writes high voltage value to pin, LED on
time.sleep(5)                 # sleeps for a second
board.digital[pin].write(0)   # writes low voltage value to pin, LED off