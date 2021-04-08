#include <Servo.h>
const int nbrServos = 4;
Servo ser[nbrServos];
int incoming[3];


void setup() {
   Serial.begin(9600);
  ser[0].attach(8); /*MIDDLE*/
  ser[1].attach(11);  /*RIGHT*/
  ser[2].attach(6);  /*CRANE*/
  ser[3].attach(4);/*LEFT */
}

void loop() {
while(Serial.available()>=4) {
  for (int i =0; i <4; i++){
    incoming[i] = Serial.read();
  }
  ser[0].write(incoming[0]);
  ser[1].write(incoming[1]);
  ser[2].write(incoming[2]);
  ser[3].write(incoming[3]);
  
}

}
