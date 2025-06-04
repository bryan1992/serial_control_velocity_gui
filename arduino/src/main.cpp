#include <Arduino.h>
const int stepX = 2;
const int dirX = 5;
const int enPin = 8;

unsigned long tiempoAnterior = micros();
unsigned long tiempoActual = 0;
unsigned long tiempoToggle = 0;
unsigned long intervalo = 0;
unsigned long ultimoPrint;
unsigned long ultimoSerial = 0;
int valor = 0;
bool pulso = true;
bool clienteActivo;
String serialBuffer;

void setup() {
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(dirX, HIGH);   // Establece la dirección de giro
  digitalWrite(enPin, LOW);   // Habilita el driver (LOW = habilitado)

  Serial.begin(9600);
  delay(200);
  Serial.println("Iniciando...");
  Serial.print("La velocidad actual es: ");
  Serial.println(intervalo);
  ultimoPrint = millis();
}

void loop() {

  // Impresión periódica de intervalo.
  if (Serial && (millis() - ultimoPrint >= 2000))
    {
      Serial.print("La velocidad actual es: ");
      Serial.println(valor);
      ultimoPrint = millis();
    }
  
  // Control de motor.
  tiempoActual = micros();
  if (tiempoActual - tiempoAnterior >= intervalo)
    {
      tiempoAnterior = tiempoActual;
      tiempoToggle = tiempoActual;
      pulso = !pulso;

      // Pulso de dirección.
      if (valor >= 0)
        {
          digitalWrite(dirX, HIGH);
        }
      else
        {
          digitalWrite(dirX, LOW);
        }

      // Pulso de movimiento.
      if (valor != 0)
        {
          digitalWrite(stepX, pulso);
        }      
    }

  // Comunicación serial.
  while (Serial.available() > 0)
  {
    char c = Serial.read();
    if (c == '\n')
      {
        valor = serialBuffer.toInt();
        intervalo = abs(valor);
        Serial.println(valor);
        serialBuffer = "";
        ultimoSerial = millis();
        clienteActivo = true;
      }
    else if (isDigit(c) || (c == '-'))
      {
        serialBuffer += c; // Concatenar caracteres en buffer, antes de recibir \n.
      }
  } 

  if ((millis() - ultimoSerial) > 5000)
    {
      clienteActivo = false;
    }
}