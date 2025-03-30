import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel

print ("Mi proyecto")

# Se crea una clase que hereda de QMianWindow.
class VentanaSencilla(QMainWindow):
    def __init__(self):                                     # "init" es un método de inicialización que se ejecuta al instanciar una clase.
        super().__init__()
        self.setWindowTitle("Control de velocidad serial")  # Título de la ventana.
        self.setGeometry(200, 200, 400, 300)                # Posición y tamaño (x, y, ancho, alto)

         # Crear un ComboBox
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 50, 200, 30)  # Posición y tamaño (x, y, ancho, alto)

        # Añadir elementos al ComboBox
        self.combo_box.addItems(["Opción 1", "Opción 2", "Opción 3"])

# Configurar la aplicación
app = QApplication(sys.argv)                                # Necesario para cualquier aplicación PyQt
ventana = VentanaSencilla()                                 # Se crea una instancia de la clase "VentanaSencilla".
ventana.show()                                              # Mostrar la ventana principal (método).

# Ejecutar el bucle principal
sys.exit(app.exec())