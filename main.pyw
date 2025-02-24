from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
import logo_rc
from fractions import Fraction
from form import * #ARCHIVO DEL FORMULARIO CREADO

class form(QMainWindow):

    def __init__(self):  
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.btnCalcularResta.clicked.connect(self.restar)
        self.ui.btnLimpiarResta.clicked.connect(self.cleanrestar)
        self.ui.btnCalcularSum.clicked.connect(self.sumar)
        self.ui.btnLimpiarSum.clicked.connect(self.cleansuma)
        self.ui.btnCalcularInversa.clicked.connect(self.inversa)
        self.ui.btnLimpiarInversa.clicked.connect(self.cleaninversa)
        self.ui.btnLimpiarMulti.clicked.connect(self.cleanmultiplicar)
        self.ui.btnCalcularMulti.clicked.connect(self.multiplicar)

    def cleanmultiplicar(self):
               #MATRIZ A
        self.ui.txtMaMulti11.clear()
        self.ui.txtMaMulti12.clear()
        self.ui.txtMaMulti13.clear()
        self.ui.txtMaMulti21.clear()
        self.ui.txtMaMulti22.clear()
        self.ui.txtMaMulti23.clear()
        self.ui.txtMaMulti31.clear()
        self.ui.txtMaMulti32.clear()
        self.ui.txtMaMulti33.clear()
        #MATRIZ B
        self.ui.txtMbMulti11.clear()
        self.ui.txtMbMulti12.clear()
        self.ui.txtMbMulti13.clear()
        self.ui.txtMbMulti21.clear()
        self.ui.txtMbMulti22.clear()
        self.ui.txtMbMulti23.clear()
        self.ui.txtMbMulti31.clear()
        self.ui.txtMbMulti32.clear()
        self.ui.txtMbMulti33.clear()
        #MATRIZ RESPUESTA
        self.ui.txtMresMulti11.clear()
        self.ui.txtMresMulti12.clear()
        self.ui.txtMresMulti13.clear()
        self.ui.txtMresMulti21.clear()
        self.ui.txtMresMulti22.clear()
        self.ui.txtMresMulti23.clear()
        self.ui.txtMresMulti31.clear()
        self.ui.txtMresMulti32.clear()
        self.ui.txtMresMulti33.clear()

    def cleanrestar(self):
        #MATRIZ A
        self.ui.txtMaResta11.clear()
        self.ui.txtMaResta12.clear()
        self.ui.txtMaResta13.clear()
        self.ui.txtMaResta21.clear()
        self.ui.txtMaResta22.clear()
        self.ui.txtMaResta23.clear()
        self.ui.txtMaResta31.clear()
        self.ui.txtMaResta32.clear()
        self.ui.txtMaResta33.clear()
        #MATRIZ B
        self.ui.txtMbResta11.clear()
        self.ui.txtMbResta12.clear()
        self.ui.txtMbResta13.clear()
        self.ui.txtMbResta21.clear()
        self.ui.txtMbResta22.clear()
        self.ui.txtMbResta23.clear()
        self.ui.txtMbResta31.clear()
        self.ui.txtMbResta32.clear()
        self.ui.txtMbResta33.clear()
        #MATRIZ RESPUESTA
        self.ui.txtMresResta11.clear()
        self.ui.txtMresResta12.clear()
        self.ui.txtMresResta13.clear()
        self.ui.txtMresResta21.clear()
        self.ui.txtMresResta22.clear()
        self.ui.txtMresResta23.clear()
        self.ui.txtMresResta31.clear()
        self.ui.txtMresResta32.clear()
        self.ui.txtMresResta33.clear()
       
    def restar(self):
        # MATRIZ A
        
       try:
         # MATRIZ A
         A = [
            [float(self.ui.txtMaResta11.text()), float(self.ui.txtMaResta12.text()), float(self.ui.txtMaResta13.text())],
            [float(self.ui.txtMaResta21.text()), float(self.ui.txtMaResta22.text()), float(self.ui.txtMaResta23.text())],
            [float(self.ui.txtMaResta31.text()), float(self.ui.txtMaResta32.text()), float(self.ui.txtMaResta33.text())],
          ]

         # MATRIZ B
         B = [
            [float(self.ui.txtMbResta11.text()), float(self.ui.txtMbResta12.text()), float(self.ui.txtMbResta13.text())],
            [float(self.ui.txtMbResta21.text()), float(self.ui.txtMbResta22.text()), float(self.ui.txtMbResta23.text())],
            [float(self.ui.txtMbResta31.text()), float(self.ui.txtMbResta32.text()), float(self.ui.txtMbResta33.text())],
          ]

          # MATRIZ RESULTADO
         Mres = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

          # IMPRIMIR RESULTADOS
         self.ui.txtMresResta11.setText(str(Mres[0][0]))
         self.ui.txtMresResta12.setText(str(Mres[0][1]))
         self.ui.txtMresResta13.setText(str(Mres[0][2]))
         self.ui.txtMresResta21.setText(str(Mres[1][0]))
         self.ui.txtMresResta22.setText(str(Mres[1][1]))
         self.ui.txtMresResta23.setText(str(Mres[1][2]))
         self.ui.txtMresResta31.setText(str(Mres[2][0]))
         self.ui.txtMresResta32.setText(str(Mres[2][1]))
         self.ui.txtMresResta33.setText(str(Mres[2][2]))
       except ValueError:
         QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos en todos los campos.")
 
    
       
      
    def cleansuma(self):
        #MATRIZ A
        self.ui.txtMaSum11.clear()
        self.ui.txtMaSum12.clear()
        self.ui.txtMaSum13.clear()
        self.ui.txtMaSum21.clear()
        self.ui.txtMaSum22.clear()
        self.ui.txtMaSum23.clear()
        self.ui.txtMaSum31.clear()
        self.ui.txtMaSum32.clear()
        self.ui.txtMaSum33.clear()
        #MATRIZ B
        self.ui.txtMbSum11.clear()
        self.ui.txtMbSum12.clear()
        self.ui.txtMbSum13.clear()
        self.ui.txtMbSum21.clear()
        self.ui.txtMbSum22.clear()
        self.ui.txtMbSum23.clear()
        self.ui.txtMbSum31.clear()
        self.ui.txtMbSum32.clear()
        self.ui.txtMbSum33.clear()
        #MATRIZ RESPUESTA
        self.ui.txtMresSum11.clear()
        self.ui.txtMresSum12.clear()
        self.ui.txtMresSum13.clear()
        self.ui.txtMresSum21.clear()
        self.ui.txtMresSum22.clear()
        self.ui.txtMresSum23.clear()
        self.ui.txtMresSum31.clear()
        self.ui.txtMresSum32.clear()
        self.ui.txtMresSum33.clear()

    def sumar(self):

      try:
       A= [
         [float(self.ui.txtMaSum11.text()), float(self.ui.txtMaSum12.text()), float(self.ui.txtMaSum13.text())],
         [float(self.ui.txtMaSum21.text()), float(self.ui.txtMaSum22.text()), float(self.ui.txtMaSum23.text())],
         [float(self.ui.txtMaSum31.text()), float(self.ui.txtMaSum32.text()), float(self.ui.txtMaSum33.text())],
        ]

       B= [
         [float(self.ui.txtMbSum11.text()), float(self.ui.txtMbSum12.text()), float(self.ui.txtMbSum13.text())],
         [float(self.ui.txtMbSum21.text()), float(self.ui.txtMbSum22.text()), float(self.ui.txtMbSum23.text())],
         [float(self.ui.txtMbSum31.text()), float(self.ui.txtMbSum32.text()), float(self.ui.txtMbSum33.text())],
        ]

       MresSum = [
         [A[i][j]+ B[i][j] for j in range(3)] for i in range(3)
        ]

       self.ui.txtMresSum11.setText(str(MresSum[0][0]))
       self.ui.txtMresSum12.setText(str(MresSum[0][1]))
       self.ui.txtMresSum13.setText(str(MresSum[0][2]))
       self.ui.txtMresSum21.setText(str(MresSum[1][0]))
       self.ui.txtMresSum22.setText(str(MresSum[1][1]))
       self.ui.txtMresSum23.setText(str(MresSum[1][2]))
       self.ui.txtMresSum31.setText(str(MresSum[2][0]))
       self.ui.txtMresSum32.setText(str(MresSum[2][1]))
       self.ui.txtMresSum33.setText(str(MresSum[2][2]))
      except ValueError:
         QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos en todos los campos.")
  

    def cleaninversa(self):
        #MATRIZ A
        self.ui.txtMaInversa11.clear()
        self.ui.txtMaInversa12.clear()
        self.ui.txtMaInversa13.clear()
        self.ui.txtMaInversa21.clear()
        self.ui.txtMaInversa22.clear()
        self.ui.txtMaInversa23.clear()
        self.ui.txtMaInversa31.clear()
        self.ui.txtMaInversa32.clear()
        self.ui.txtMaInversa33.clear()
        #MATRIZ ADJUNTA
        self.ui.txtMadjunInversa11.clear()
        self.ui.txtMadjunInversa12.clear()
        self.ui.txtMadjunInversa13.clear()
        self.ui.txtMadjunInversa21.clear()
        self.ui.txtMadjunInversa22.clear()
        self.ui.txtMadjunInversa23.clear()
        self.ui.txtMadjunInversa31.clear()
        self.ui.txtMadjunInversa32.clear()
        self.ui.txtMadjunInversa11.clear()
        #MATRIZ INVESA RESPUESTA
        self.ui.txtMinversaInversa11.clear()
        self.ui.txtMinversaInversa12.clear()
        self.ui.txtMinversaInversa13.clear()
        self.ui.txtMinversaInversa21.clear()
        self.ui.txtMinversaInversa22.clear()
        self.ui.txtMinversaInversa23.clear()
        self.ui.txtMinversaInversa31.clear()
        self.ui.txtMinversaInversa32.clear()
        self.ui.txtMinversaInversa33.clear()
        #VALOR DEL DETERMINANTE
        self.ui.txtDeterInversa.clear()

    def multiplicar(self):
    # MATRIZ A
     try:
        A = [
         [float(self.ui.txtMaMulti11.text()), float(self.ui.txtMaMulti12.text()), float(self.ui.txtMaMulti13.text())],
         [float(self.ui.txtMaMulti21.text()), float(self.ui.txtMaMulti22.text()), float(self.ui.txtMaMulti23.text())],
         [float(self.ui.txtMaMulti31.text()), float(self.ui.txtMaMulti32.text()), float(self.ui.txtMaMulti33.text())],
        ]

       # MATRIZ B
        B = [
         [float(self.ui.txtMbMulti11.text()), float(self.ui.txtMbMulti12.text()), float(self.ui.txtMbMulti13.text())],
         [float(self.ui.txtMbMulti21.text()), float(self.ui.txtMbMulti22.text()), float(self.ui.txtMbMulti23.text())],
         [float(self.ui.txtMbMulti31.text()), float(self.ui.txtMbMulti32.text()), float(self.ui.txtMbMulti33.text())],
        ]

       # MATRIZ RESULTADO (C = A * B)
        Mres = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(3):
         for j in range(3):
            Mres[i][j] = sum(A[i][k] * B[k][j] for k in range(3))

        # MOSTRAR RESULTADOS EN LA INTERFAZ
        self.ui.txtMresMulti11.setText(str(Mres[0][0]))
        self.ui.txtMresMulti12.setText(str(Mres[0][1]))
        self.ui.txtMresMulti13.setText(str(Mres[0][2]))
        self.ui.txtMresMulti21.setText(str(Mres[1][0]))
        self.ui.txtMresMulti22.setText(str(Mres[1][1]))
        self.ui.txtMresMulti23.setText(str(Mres[1][2]))
        self.ui.txtMresMulti31.setText(str(Mres[2][0]))
        self.ui.txtMresMulti32.setText(str(Mres[2][1]))
        self.ui.txtMresMulti33.setText(str(Mres[2][2]))
     except ValueError:
         QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos en todos los campos.")

    

    def inversa(self):
     try:
        # MATRIZ ORIGINAL con números en fracción
        A = [
            [Fraction(self.ui.txtMaInversa11.text()), Fraction(self.ui.txtMaInversa12.text()), Fraction(self.ui.txtMaInversa13.text())],
            [Fraction(self.ui.txtMaInversa21.text()), Fraction(self.ui.txtMaInversa22.text()), Fraction(self.ui.txtMaInversa23.text())],
            [Fraction(self.ui.txtMaInversa31.text()), Fraction(self.ui.txtMaInversa32.text()), Fraction(self.ui.txtMaInversa33.text())],
        ] 

        # DETERMINANTE (Regla de Sarrus)
        det = (
            A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
          - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
          + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
        )

        # MOSTRAR DETERMINANTE COMO FLOAT
        self.ui.txtDeterInversa.setText(str(float(det)))  

        if det == 0:
            QMessageBox.warning(self, "Error", "No hay inversa, el determinante es 0.")
            return

        # MATRIZ DE COFACTORES
        Cof = [
            [
                (A[1][1] * A[2][2] - A[1][2] * A[2][1]) * (-1) ** (0 + 0),
                (A[1][0] * A[2][2] - A[1][2] * A[2][0]) * (-1) ** (0 + 1),
                (A[1][0] * A[2][1] - A[1][1] * A[2][0]) * (-1) ** (0 + 2),
            ],
            [
                (A[0][1] * A[2][2] - A[0][2] * A[2][1]) * (-1) ** (1 + 0),
                (A[0][0] * A[2][2] - A[0][2] * A[2][0]) * (-1) ** (1 + 1),
                (A[0][0] * A[2][1] - A[0][1] * A[2][0]) * (-1) ** (1 + 2),
            ],
            [
                (A[0][1] * A[1][2] - A[0][2] * A[1][1]) * (-1) ** (2 + 0),
                (A[0][0] * A[1][2] - A[0][2] * A[1][0]) * (-1) ** (2 + 1),
                (A[0][0] * A[1][1] - A[0][1] * A[1][0]) * (-1) ** (2 + 2),
            ],
        ]

        # MATRIZ ADJUNTA (Transpuesta de la matriz de cofactores) convertida a float
        Adj = [[float(Cof[j][i]) for j in range(3)] for i in range(3)]

        # MOSTRAR ADJUNTA COMO FLOAT
        self.ui.txtMadjunInversa11.setText(str(Adj[0][0]))
        self.ui.txtMadjunInversa12.setText(str(Adj[0][1]))
        self.ui.txtMadjunInversa13.setText(str(Adj[0][2]))
        self.ui.txtMadjunInversa21.setText(str(Adj[1][0]))
        self.ui.txtMadjunInversa22.setText(str(Adj[1][1]))
        self.ui.txtMadjunInversa23.setText(str(Adj[1][2]))
        self.ui.txtMadjunInversa31.setText(str(Adj[2][0]))
        self.ui.txtMadjunInversa32.setText(str(Adj[2][1]))
        self.ui.txtMadjunInversa33.setText(str(Adj[2][2]))

        #Convertir determinante a fracción antes de usarlo en la inversa
        det_frac = Fraction(det)

        # MATRIZ INVERSA (Adjunta / Determinante) en fracciones
        Inv = [[Fraction(Adj[i][j]) / det_frac for j in range(3)] for i in range(3)]

        # MOSTRAR INVERSA COMO FRACCIÓN
        self.ui.txtMinversaInversa11.setText(str(Inv[0][0]))
        self.ui.txtMinversaInversa12.setText(str(Inv[0][1]))
        self.ui.txtMinversaInversa13.setText(str(Inv[0][2]))
        self.ui.txtMinversaInversa21.setText(str(Inv[1][0]))
        self.ui.txtMinversaInversa22.setText(str(Inv[1][1]))
        self.ui.txtMinversaInversa23.setText(str(Inv[1][2]))
        self.ui.txtMinversaInversa31.setText(str(Inv[2][0]))
        self.ui.txtMinversaInversa32.setText(str(Inv[2][1]))
        self.ui.txtMinversaInversa33.setText(str(Inv[2][2]))

     except ValueError:
        QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos en todos los campos.")
     


        # CREAR LA APLICACION Y MOSTRARLA
if __name__ =="__main__":  
    app = QApplication(sys.argv)
    myapp = form()
    myapp.show()
    sys.exit(app.exec_()) 

    
    