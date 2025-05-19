#include <Arduino.h>
const int stepX = 2;
const int dirX = 5;
const int enPin = 8;

unsigned long tiempo_anterior = 0;
unsigned long tiempo_acumulado = 0;
unsigned int intervalo_bajo = 800;
unsigned int intervalo_alto = 800;
bool pulso = true;

void setup() {
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(dirX, HIGH);   // Establece la dirección de giro
  digitalWrite(enPin, LOW);   // Habilita el driver (LOW = habilitado)
}

void loop() {
  unsigned long tiempo_actual = micros();
    
  if(pulso == true)
    {
      if(tiempo_acumulado < intervalo_alto)
        { 
          tiempo_acumulado = tiempo_acumulado + (tiempo_actual - tiempo_anterior);
          digitalWrite(stepX, HIGH);
          delayMicroseconds(5);
        }
      else if (tiempo_acumulado >= intervalo_alto)
        {
          tiempo_acumulado = 0;
          pulso = false;
        }     
    }
  else if (pulso == false)
    {
      if(tiempo_acumulado < intervalo_bajo)
        {
          digitalWrite(stepX, LOW);
          delayMicroseconds(5);
        }
      else if (tiempo_acumulado >= intervalo_bajo)
        {
          tiempo_acumulado = 0;
          pulso = true;
        }
    }
}
