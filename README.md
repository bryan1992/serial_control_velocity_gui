Proyecto sencillo para controlar la velocidad de un motor a pasos NEMA 17.

El proyecto consta de dos partes de software:

1.- Interfaz gráfica de usuario (escrita en Python): Interfaz que correrá en la PC, desde la cual se enviarán comandos de control al microcontrolador Arduino UNO. Desde aquí, el usuario será capaz de decidir en qué momento el motor debe girar o detenerse, también, desde aquí se podrá cambiar el sentido de giro y la velocidad.

2.- Lógica de controlador de motor (escrita en C++): Lógica de placa Arduino UNO, la cual recibirá comandos provenientes de la interfaz principal de control y la traducirá a pulsos digitales a fin de controlar el motor NEMA 17.