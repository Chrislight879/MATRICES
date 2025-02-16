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
        self.ui.btnCalcularResta.clicked.connect(self.restar)

    def restar(self):
        # MATRIZ A
        A = [
            [float(self.ui.txtMaResta11.text()), float(self.ui.txtMaResta12.text()), float(self.ui.txtMaResta13.text())],
            [float(self.ui.txtMaResta21.text()), float(self.ui.txtMaResta22.text()), float(self.ui.txtMaResta23.text())],
            [float(self.ui.txtMaResta31.text()), float(self.ui.txtMaResta32.text()), float(self.ui.txtMaResta33.text())],
        ]
        
        B = [
            [float(self.ui.txtMbResta11.text()), float(self.ui.txtMbResta12.text()), float(self.ui.txtMbResta13.text())],
            [float(self.ui.txtMbResta21.text()), float(self.ui.txtMbResta22.text()), float(self.ui.txtMbResta23.text())],
            [float(self.ui.txtMbResta31.text()), float(self.ui.txtMbResta32.text()), float(self.ui.txtMbResta33.text())],
        ]
        
        # MATRIZ B
        Mres = [
            [A[i][j] - B[i][j] for j in range(3)] for i in range(3)
        ]
        
        # IMPRIMIR MATRIZ RESPUESTA
        self.ui.txtMresResta11.setText(str(Mres[0][0]))
        self.ui.txtMresResta12.setText(str(Mres[0][1]))
        self.ui.txtMresResta13.setText(str(Mres[0][2]))
        self.ui.txtMresResta21.setText(str(Mres[1][0]))
        self.ui.txtMresResta22.setText(str(Mres[1][1]))
        self.ui.txtMresResta23.setText(str(Mres[1][2]))
        self.ui.txtMresResta31.setText(str(Mres[2][0]))
        self.ui.txtMresResta32.setText(str(Mres[2][1]))
        self.ui.txtMresResta33.setText(str(Mres[2][2]))


        # CREAR LA APLICACION Y MOSTRARLA
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    myapp = form()
    myapp.show()
    sys.exit(app.exec_()) 

    
    