import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton
import serial.tools.list_ports

print ("Mi proyecto de control serial")

# Se crea sub-clase para hacer que el combo box pueda actualizar puertos al dar clic.
class ComboBoxConActualizacion(QComboBox):
     def __init__(self, parent=None):
        super().__init__(parent)

     def showPopup(self):
        """Sobrescribe el showPopup para actualizar puertos cada vez que el combo box se despliegue"""
        self.actualizar_puertos_com()  # Actualizar la lista de puertos antes de abrir el combo
        super().showPopup()  # Llamar a la función original para mostrar el popup

     def actualizar_puertos_com(self):
        """Actualiza la lista de puertos COM disponibles."""
        puertos = serial.tools.list_ports.comports()
        self.clear()  # Limpiar el combo box antes de agregar los nuevos puertos
        for puerto in puertos:
            self.addItem(puerto.device)

# Se crea una sub-clase que hereda de QMainWindow.
class VentanaSencilla(QMainWindow):
    def __init__(self):                                       # "init" es un método de inicialización (constructor) que se ejecuta al instanciar una clase.
        super().__init__()                                    # Función que usualmente se utiliza para herencias de clases en Python.

        # Ventana principal.                              
        self.setWindowTitle("Control de velocidad serial")    # Título de la ventana.
        self.setGeometry(200, 200, 400, 300)                  # Posición y tamaño (x, y, ancho, alto)

        # Leyenda de texto para selector de puertos.
        self.label = QLabel("Puertos COM disponibles:", self) #Al añadir self a los parámetros de la función indicamos que el objeto de la clase VentanaSencilla es su padre.
        self.label.move(20, 20)
        self.label.adjustSize()
        
        # ComboBox (selector de varias opciones).
        self.combo_box = ComboBoxConActualizacion(self)                    #Este es un atributo.
        self.combo_box.setGeometry(50, 50, 200, 30)         # Posición y tamaño (x, y, ancho, alto)
        # Conectar el evento de abrir el combo box al método de actualización de puertos
        #self.combo_box.showPopup = self.actualizar_puertos_com

        # Botón booleano para iniciar conexión.
        self.boton_booleano = QPushButton("Iniciar conexión.", self)
        self.boton_booleano.setGeometry (50, 100, 200, 30)

# Configurar la aplicación
app = QApplication(sys.argv)                                # Necesario para cualquier aplicación PyQt
ventana = VentanaSencilla()                                 # Se crea una instancia de la clase "VentanaSencilla".
ventana.show()                                              # Mostrar la ventana principal (método).

# Ejecutar el bucle principal
sys.exit(app.exec())