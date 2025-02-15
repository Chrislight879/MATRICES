from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
import logo_rc
from form import * #ARCHIVO DEL FORMULARIO CREADO

class form(QMainWindow):

    def __init__(self):  
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    


        # CREAR LA APLICACION Y MOSTRARLA
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    myapp = form()
    myapp.show()
    sys.exit(app.exec_()) 

    
    