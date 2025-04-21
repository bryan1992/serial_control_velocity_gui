import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton
from serial import Serial
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
    def __init__(self):                                       
        super().__init__()                                    

        # Inicialización de variables.
        self.serial_port = None
        self.conectado = False
        self.boton_estado = False
        
        # Ventana principal.                              
        self.setWindowTitle("Control de velocidad serial")    
        self.setGeometry(200, 200, 400, 300)                  

        self.crear_widgets()
        self.conectar_senales()
                        
    def crear_widgets(self):

        # Etiqueta de Combo box.
        self.label = QLabel("Puertos COM disponibles:", self)
        self.label.move(10, 20)
        self.label.adjustSize()

        # Combo box.
        self.combo_box = ComboBoxConActualizacion(self)
        self.combo_box.setGeometry(10, 50, 200, 30)

        # Botón booleano para iniciar conexión.
        self.start_session = QPushButton("Desconectado", self)
        self.start_session.setGeometry (10, 100, 200, 30)

        #Indicador de estado de puerto.
        self.estatus = QLabel("No conectado", self)
        self.estatus.move(10, 130)

    def conectar_senales(self):
        self.start_session.clicked.connect(self.abrir_o_cerrar)

    def abrir_o_cerrar(self):
        if not self.conectado:
            self.abrir_puerto()
            self.start_session.setText("Conectado.")
        else:
            self.cerrar_puerto()
            self.start_session.setText("Desconectado.")
    
    def abrir_puerto(self):
        puerto_seleccionado = self.combo_box.currentText()
        try:
             self.serial_port = Serial(
                   port = puerto_seleccionado,
                   baudrate = 9600,
                   bytesize = 8,
                   parity = 'N',
                   stopbits = 1,
                   timeout = 1
              )
             if self.serial_port.is_open:
                 self.conectado = True
                 self.estatus.setText ("Conectado")
                
             else:
                 self.estatus.setText("No se pudo abrir el puerto")
        except Exception as e:
             self.estatus.setText(f"Error: {e}")
             print(f"Error: {e}")

    def cerrar_puerto(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.conectado = False
            self.estatus.setText("Desconectado.")

# Configurar la aplicación
app = QApplication(sys.argv)                                # Necesario para cualquier aplicación PyQt
ventana = VentanaSencilla()                                 # Se crea una instancia de la clase "VentanaSencilla".
ventana.show()                                              # Mostrar la ventana principal (método).

# Ejecutar el bucle principal
sys.exit(app.exec())