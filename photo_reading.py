import time 
import pyfirmata

ledred = 13
ledblue = 12
photo = 5


port = '/dev/ttyACM1'  # com port for Arduino  
board = pyfirmata.Arduino(port)  # creates Arduino board object variable
it = pyfirmata.util.Iterator(board)
it.start()
board.analog[photo].enable_reporting()
while True:
    value = board.analog[photo].read()
    if not value is None:
       
        o=open("readings.txt","a")
        timestamp = time.strftime("%H:%M:%S %d %m %Y") 
        o.write(str(value) + "\t" + timestamp + '\n')
        o.close()
        
        print(value,timestamp) 
        
        if value < 0.05:
            board.digital[ledblue].write(1) 
            board.digital[ledred].write(0)
    
        else:
            board.digital[ledred].write(1) 
            board.digital[ledblue].write(0)
        time.sleep(30)