#include <Arduino.h>
const int stepX = 2;
const int dirX = 5;
const int enPin = 8;

unsigned long tiempo_anterior = micros();
unsigned long tiempo_actual = 0;
unsigned long tiempo_toggle = 0;
unsigned long tiempo_acumulado = 0;
unsigned long intervalo = 800;
bool pulso = true;

void setup() {
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(dirX, HIGH);   // Establece la dirección de giro
  digitalWrite(enPin, LOW);   // Habilita el driver (LOW = habilitado)

  Serial.begin(9600);
}

void loop() {
  tiempo_actual = micros();
  
  if (tiempo_actual - tiempo_anterior >= intervalo)
    {
      tiempo_anterior = tiempo_actual;
      tiempo_toggle = tiempo_actual;
      pulso = !pulso;
      digitalWrite(stepX, pulso);
    }
}
