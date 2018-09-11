int trigger_pin = 11;

int echo_pin = 10;



int time;

int distance; 

// Motor A
 
int enA = 9;
int in1 = 8;
int in2 = 7;
 
// Motor B
 
int enB = 3;
int in3 = 4;
int in4 = 5;



void setup ( ) {

        Serial.begin (9600); 

        pinMode (trigger_pin, OUTPUT); 

        pinMode (echo_pin, INPUT);

        pinMode(enA, OUTPUT);
        pinMode(enB, OUTPUT);
        pinMode(in1, OUTPUT);
        pinMode(in2, OUTPUT);
        pinMode(in3, OUTPUT);
        pinMode(in4, OUTPUT);
 




}




void loop ( ) {

    digitalWrite (trigger_pin, HIGH);

    delayMicroseconds (5);

    digitalWrite (trigger_pin, LOW);

    time = pulseIn (echo_pin, HIGH);

    distance = (time * 0.034) / 2;


    analogWrite(enA, 200);
    analogWrite(enB, 200);

              
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
   
    // Set speed to 200 out of possible range 0~255
   

    // Turn on motor B
   
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
   
    // Set speed to 200 out of possible range 0~255
   
    

   
 

    

  if (distance <= 20) 

        {



  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);  
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);

  analogWrite(enA, 0);
  analogWrite(enB, 100);

  delay(1000);

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);  
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);

  analogWrite(enA, 200);
  analogWrite(enB, 200);

       
        }

  else {
    


    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);  
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);


  } 

  }
