#include <stdlib.h>
//se hace el mapeo de los pines al shield.
const int stepX = 2;
const int dirX = 5;
//const int stepY = 3;
//const int dirY  = 6;
//const int stepZ = 4;
//const int dirZ  = 7;
const int enPin = 8;
//const int limitx = 9;
//const int limity = 10;

int Tiempo = 1000;
int i = 0;

void setup() {
  //Declaraciòn de salidas e inicializaciòn.
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW);
  digitalWrite(dirX, HIGH);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //Los pulsos serán de 500 a 1000 microsegundos.
 //if (Serial.available() > 0) {
  //  i = Serial.parseInt();
    // Signo positivo implica sentido antihorario.
  //  if (i > 0) {
  //    digitalWrite(dirX, HIGH);
  //    if (i > 2000) { i = 2000; }
  //    if (i < 450) { i = 450; }
  //  }

  

    // Signo negativo implica sentido horario.
  //  if (i < 0) {
  //    digitalWrite(dirX, LOW);
  //    if (i <= -2000) { i = -2000; }
  //    if (i >= -450) { i = -450; }
  //    i = i * -1;
//    }

//    //Signo neutro (cero) implica que el motor detendrá su marcha.
//    Tiempo = i;
//    Serial.println(Tiempo);
//  }

//  if (Serial.available() == 0)
//      {i = 1000;}

//  if (Tiempo != 0) {
    //Pulsos de control al motor.
    digitalWrite(stepX, HIGH);
    delayMicroseconds(Tiempo);

    digitalWrite(stepX, LOW);
    delayMicroseconds(Tiempo);
//  }
}