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

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.btnCalcularResta.clicked.connect(self.restar)
        self.ui.btnCalcularSum.clicked.connect(self.sumar)
        self.ui.btnCalcularInversa.clicked.connect(self.inversa)

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

    def sumar(self):

      
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

    def inversa(self):
    # MATRIZ ORIGINAL
      A = [
         [float(self.ui.txtMaInversa11.text()), float(self.ui.txtMaInversa12.text()), float(self.ui.txtMaInversa13.text())],
         [float(self.ui.txtMaInversa21.text()), float(self.ui.txtMaInversa22.text()), float(self.ui.txtMaInversa23.text())],
         [float(self.ui.txtMaInversa31.text()), float(self.ui.txtMaInversa32.text()), float(self.ui.txtMaInversa33.text())],
      ] 

      # DETERMINANTE (Regla de Sarrus)
      det = (
            A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
          - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
          + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
       )

      # MOSTRAR DETERMINANTE
      self.ui.txtDeterInversa.setText(str(det))

      if det == 0:
        self.ui.txtMinversaInversa11.setText("Nu hay")
        self.ui.txtMinversaInversa12.setText("Nu hay")
        self.ui.txtMinversaInversa13.setText("Nu hay")
        self.ui.txtMinversaInversa21.setText("Nu hay")
        self.ui.txtMinversaInversa22.setText("Nu hay")
        self.ui.txtMinversaInversa23.setText("Nu hay")
        self.ui.txtMinversaInversa31.setText("Nu hay")
        self.ui.txtMinversaInversa32.setText("Nu hay")
        self.ui.txtMinversaInversa33.setText("Nu hay")
        return

      # MATRIZ DE COFACTORES
      Cof = [
           [
             ((A[1][1] * A[2][2] - A[1][2] * A[2][1]) * ((-1) ** (0 + 0))),
             ((A[1][0] * A[2][2] - A[1][2] * A[2][0]) * ((-1) ** (0 + 1))),
             ((A[1][0] * A[2][1] - A[1][1] * A[2][0]) * ((-1) ** (0 + 2))),
           ],
           [
             ((A[0][1] * A[2][2] - A[0][2] * A[2][1]) * ((-1) ** (1 + 0))),
             ((A[0][0] * A[2][2] - A[0][2] * A[2][0]) * ((-1) ** (1 + 1))),
             ((A[0][0] * A[2][1] - A[0][1] * A[2][0]) * ((-1) ** (1 + 2))),
           ],
           [
             ((A[0][1] * A[1][2] - A[0][2] * A[1][1]) * ((-1) ** (2 + 0))),
             ((A[0][0] * A[1][2] - A[0][2] * A[1][0]) * ((-1) ** (2 + 1))),
             ((A[0][0] * A[1][1] - A[0][1] * A[1][0]) * ((-1) ** (2 + 2))),
           ],
        ]

      # MATRIZ ADJUNTA (Transpuesta de la matriz de cofactores)
      Adj = [[Cof[j][i] for j in range(3)] for i in range(3)]

      # MOSTRAR ADJUNTA
      self.ui.txtMadjunInversa11.setText(str(Adj[0][0]))
      self.ui.txtMadjunInversa12.setText(str(Adj[0][1]))
      self.ui.txtMadjunInversa13.setText(str(Adj[0][2]))
      self.ui.txtMadjunInversa21.setText(str(Adj[1][0]))
      self.ui.txtMadjunInversa22.setText(str(Adj[1][1]))
      self.ui.txtMadjunInversa23.setText(str(Adj[1][2]))
      self.ui.txtMadjunInversa31.setText(str(Adj[2][0]))
      self.ui.txtMadjunInversa32.setText(str(Adj[2][1]))
      self.ui.txtMadjunInversa33.setText(str(Adj[2][2]))

      # MATRIZ INVERSA (Adjunta / Determinante)
      det = float(det)  # Asegura que det sea flotante
      Inv = [[float(Adj[i][j]) / float(det) for j in range(3)] for i in range(3)]

      # MOSTRAR INVERSA
      self.ui.txtMinversaInversa11.setText(str(Inv[0][0]))
      self.ui.txtMinversaInversa12.setText(str(Inv[0][1]))
      self.ui.txtMinversaInversa13.setText(str(Inv[0][2]))
      self.ui.txtMinversaInversa21.setText(str(Inv[1][0]))
      self.ui.txtMinversaInversa22.setText(str(Inv[1][1]))
      self.ui.txtMinversaInversa23.setText(str(Inv[1][2]))
      self.ui.txtMinversaInversa31.setText(str(Inv[2][0]))
      self.ui.txtMinversaInversa32.setText(str(Inv[2][1]))
      self.ui.txtMinversaInversa33.setText(str(Inv[2][2]))

  

        # CREAR LA APLICACION Y MOSTRARLA
if __name__ =="__main__":  
    app = QApplication(sys.argv)
    myapp = form()
    myapp.show()
    sys.exit(app.exec_()) 

    
    