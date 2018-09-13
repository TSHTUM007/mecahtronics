try:
    from pyfirmata import Arduino , util
except:
    import pip
    pip.main(['install','pyfirmata'])   # install pyfirmata # do not worry about this it is just how we do this in linux



import time                # module to tell clock time

redled_pin1 = 11           #we connect to the pins for communication between arduino and computer
orangeled_pin2 = 12
blueled_pin3 = 13          # pin on the Arduino to be used
port = '/dev/ttyACM0'  # com port for Arduino  
board = Arduino(port)  # creates Arduino board object variable


board.digital[pin1].write(1)   # writes high voltage value to pin, LED_red on
time.sleep(1)                  # sleeps for 1 second
board.digital[pin].write(0)    # turn off led_red

board.digital[pin2].write(1)   # writes high voltage value to pin, LED_orange on
time.sleep(1)                  # sleeps for 1 second
board.digital[pin2].write(0)		# turn off led_orange

board.digital[pin3].write(1)   # writes high voltage value to pin, LED_green on
time.sleep(1)                  # sleeps for 1 second
board.digital[pin3].write(0)   # turn off led_red
