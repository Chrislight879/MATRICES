# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matricesXYRHDl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 0, 691, 541))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 411, 41))
        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 30, 451, 41))
        self.label_6 = QLabel(self.tab_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 150, 49, 16))
        self.label_7 = QLabel(self.tab_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 70, 151, 151))
        self.label_7.setStyleSheet(u"border-image: url(:/cct/images.jpeg);")
        self.label_46 = QLabel(self.tab_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(190, 220, 321, 41))
        self.label_47 = QLabel(self.tab_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(170, 250, 361, 41))
        self.label_74 = QLabel(self.tab_5)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(0, 280, 361, 41))
        self.label_75 = QLabel(self.tab_5)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(0, 400, 361, 41))
        self.label_76 = QLabel(self.tab_5)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(0, 310, 361, 41))
        self.label_77 = QLabel(self.tab_5)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(0, 370, 401, 41))
        self.label_78 = QLabel(self.tab_5)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(0, 340, 361, 41))
        self.label_79 = QLabel(self.tab_5)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(0, 430, 401, 41))
        self.label_80 = QLabel(self.tab_5)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(320, 470, 401, 41))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 300, 194, 141))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.txtMresSum31 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum31.setObjectName(u"txtMresSum31")

        self.gridLayout_3.addWidget(self.txtMresSum31, 3, 0, 1, 1)

        self.txtMresSum33 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum33.setObjectName(u"txtMresSum33")

        self.gridLayout_3.addWidget(self.txtMresSum33, 3, 2, 1, 1)

        self.txtMresSum32 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum32.setObjectName(u"txtMresSum32")

        self.gridLayout_3.addWidget(self.txtMresSum32, 3, 1, 1, 1)

        self.txtMresSum23 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum23.setObjectName(u"txtMresSum23")

        self.gridLayout_3.addWidget(self.txtMresSum23, 2, 2, 1, 1)

        self.txtMresSum22 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum22.setObjectName(u"txtMresSum22")

        self.gridLayout_3.addWidget(self.txtMresSum22, 2, 1, 1, 1)

        self.txtMresSum21 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum21.setObjectName(u"txtMresSum21")

        self.gridLayout_3.addWidget(self.txtMresSum21, 2, 0, 1, 1)

        self.txtMresSum13 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum13.setObjectName(u"txtMresSum13")

        self.gridLayout_3.addWidget(self.txtMresSum13, 1, 2, 1, 1)

        self.txtMresSum12 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum12.setObjectName(u"txtMresSum12")

        self.gridLayout_3.addWidget(self.txtMresSum12, 1, 1, 1, 1)

        self.txtMresSum11 = QLineEdit(self.gridLayoutWidget_3)
        self.txtMresSum11.setObjectName(u"txtMresSum11")

        self.gridLayout_3.addWidget(self.txtMresSum11, 1, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 10, 271, 24))
        self.label_9.setFont(font)
        self.gridLayoutWidget_8 = QWidget(self.tab)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 50, 475, 164))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.gridLayoutWidget_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout_19.addWidget(self.label_19, 0, 2, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_20 = QLabel(self.gridLayoutWidget_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_20.addWidget(self.label_20, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.txtMbSum33 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum33.setObjectName(u"txtMbSum33")

        self.gridLayout_20.addWidget(self.txtMbSum33, 3, 2, 1, 1)

        self.txtMbSum31 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum31.setObjectName(u"txtMbSum31")

        self.gridLayout_20.addWidget(self.txtMbSum31, 3, 0, 1, 1)

        self.txtMbSum21 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum21.setObjectName(u"txtMbSum21")

        self.gridLayout_20.addWidget(self.txtMbSum21, 2, 0, 1, 1)

        self.txtMbSum32 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum32.setObjectName(u"txtMbSum32")

        self.gridLayout_20.addWidget(self.txtMbSum32, 3, 1, 1, 1)

        self.txtMbSum22 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum22.setObjectName(u"txtMbSum22")

        self.gridLayout_20.addWidget(self.txtMbSum22, 2, 1, 1, 1)

        self.txtMbSum23 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum23.setObjectName(u"txtMbSum23")

        self.gridLayout_20.addWidget(self.txtMbSum23, 2, 2, 1, 1)

        self.txtMbSum13 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum13.setObjectName(u"txtMbSum13")

        self.gridLayout_20.addWidget(self.txtMbSum13, 1, 2, 1, 1)

        self.txtMbSum12 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum12.setObjectName(u"txtMbSum12")

        self.gridLayout_20.addWidget(self.txtMbSum12, 1, 1, 1, 1)

        self.txtMbSum11 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMbSum11.setObjectName(u"txtMbSum11")

        self.gridLayout_20.addWidget(self.txtMbSum11, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_20, 0, 3, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.txtMaSum33 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum33.setObjectName(u"txtMaSum33")

        self.gridLayout_21.addWidget(self.txtMaSum33, 3, 2, 1, 1)

        self.txtMaSum23 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum23.setObjectName(u"txtMaSum23")

        self.gridLayout_21.addWidget(self.txtMaSum23, 2, 2, 1, 1)

        self.txtMaSum11 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum11.setObjectName(u"txtMaSum11")

        self.gridLayout_21.addWidget(self.txtMaSum11, 1, 0, 1, 1)

        self.txtMaSum12 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum12.setObjectName(u"txtMaSum12")

        self.gridLayout_21.addWidget(self.txtMaSum12, 1, 1, 1, 1)

        self.txtMaSum13 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum13.setObjectName(u"txtMaSum13")

        self.gridLayout_21.addWidget(self.txtMaSum13, 1, 2, 1, 1)

        self.txtMaSum32 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum32.setObjectName(u"txtMaSum32")

        self.gridLayout_21.addWidget(self.txtMaSum32, 3, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_21.addWidget(self.label_21, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.txtMaSum22 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum22.setObjectName(u"txtMaSum22")

        self.gridLayout_21.addWidget(self.txtMaSum22, 2, 1, 1, 1)

        self.txtMaSum31 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum31.setObjectName(u"txtMaSum31")

        self.gridLayout_21.addWidget(self.txtMaSum31, 3, 0, 1, 1)

        self.txtMaSum21 = QLineEdit(self.gridLayoutWidget_8)
        self.txtMaSum21.setObjectName(u"txtMaSum21")

        self.gridLayout_21.addWidget(self.txtMaSum21, 2, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_21, 0, 1, 1, 1)

        self.btnCalcularSum = QPushButton(self.tab)
        self.btnCalcularSum.setObjectName(u"btnCalcularSum")
        self.btnCalcularSum.setGeometry(QRect(510, 90, 171, 61))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_6 = QWidget(self.tab_2)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 55, 361, 141))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_13.addWidget(self.label_13, 0, 2, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.txtMbResta12 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta12.setObjectName(u"txtMbResta12")

        self.gridLayout_14.addWidget(self.txtMbResta12, 1, 1, 1, 1)

        self.txtMbResta22 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta22.setObjectName(u"txtMbResta22")

        self.gridLayout_14.addWidget(self.txtMbResta22, 2, 1, 1, 1)

        self.txtMbResta11 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta11.setObjectName(u"txtMbResta11")

        self.gridLayout_14.addWidget(self.txtMbResta11, 1, 0, 1, 1)

        self.txtMbResta23 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta23.setObjectName(u"txtMbResta23")

        self.gridLayout_14.addWidget(self.txtMbResta23, 2, 2, 1, 1)

        self.txtMbResta21 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta21.setObjectName(u"txtMbResta21")

        self.gridLayout_14.addWidget(self.txtMbResta21, 2, 0, 1, 1)

        self.txtMbResta32 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta32.setObjectName(u"txtMbResta32")

        self.gridLayout_14.addWidget(self.txtMbResta32, 3, 1, 1, 1)

        self.txtMbResta31 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta31.setObjectName(u"txtMbResta31")

        self.gridLayout_14.addWidget(self.txtMbResta31, 3, 0, 1, 1)

        self.txtMbResta33 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta33.setObjectName(u"txtMbResta33")

        self.gridLayout_14.addWidget(self.txtMbResta33, 3, 2, 1, 1)

        self.txtMbResta13 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMbResta13.setObjectName(u"txtMbResta13")

        self.gridLayout_14.addWidget(self.txtMbResta13, 1, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_14.addWidget(self.label_11, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 3, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.txtMaResta23 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta23.setObjectName(u"txtMaResta23")

        self.gridLayout_15.addWidget(self.txtMaResta23, 2, 2, 1, 1)

        self.txtMaResta13 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta13.setObjectName(u"txtMaResta13")

        self.gridLayout_15.addWidget(self.txtMaResta13, 1, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_15.addWidget(self.label_12, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.txtMaResta21 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta21.setObjectName(u"txtMaResta21")

        self.gridLayout_15.addWidget(self.txtMaResta21, 2, 0, 1, 1)

        self.txtMaResta22 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta22.setObjectName(u"txtMaResta22")

        self.gridLayout_15.addWidget(self.txtMaResta22, 2, 1, 1, 1)

        self.txtMaResta31 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta31.setObjectName(u"txtMaResta31")

        self.gridLayout_15.addWidget(self.txtMaResta31, 3, 0, 1, 1)

        self.txtMaResta12 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta12.setObjectName(u"txtMaResta12")

        self.gridLayout_15.addWidget(self.txtMaResta12, 1, 1, 1, 1)

        self.txtMaResta33 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta33.setObjectName(u"txtMaResta33")

        self.gridLayout_15.addWidget(self.txtMaResta33, 3, 2, 1, 1)

        self.txtMaResta32 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta32.setObjectName(u"txtMaResta32")

        self.gridLayout_15.addWidget(self.txtMaResta32, 3, 1, 1, 1)

        self.txtMaResta11 = QLineEdit(self.gridLayoutWidget_6)
        self.txtMaResta11.setObjectName(u"txtMaResta11")

        self.gridLayout_15.addWidget(self.txtMaResta11, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_15, 0, 1, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.tab_2)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 330, 151, 141))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.txtMresResta11 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta11.setObjectName(u"txtMresResta11")

        self.gridLayout_10.addWidget(self.txtMresResta11, 1, 0, 1, 1)

        self.txtMresResta31 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta31.setObjectName(u"txtMresResta31")

        self.gridLayout_10.addWidget(self.txtMresResta31, 3, 0, 1, 1)

        self.txtMresResta23 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta23.setObjectName(u"txtMresResta23")

        self.gridLayout_10.addWidget(self.txtMresResta23, 2, 2, 1, 1)

        self.txtMresResta12 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta12.setObjectName(u"txtMresResta12")

        self.gridLayout_10.addWidget(self.txtMresResta12, 1, 1, 1, 1)

        self.txtMresResta22 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta22.setObjectName(u"txtMresResta22")

        self.gridLayout_10.addWidget(self.txtMresResta22, 2, 1, 1, 1)

        self.txtMresResta21 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta21.setObjectName(u"txtMresResta21")

        self.gridLayout_10.addWidget(self.txtMresResta21, 2, 0, 1, 1)

        self.txtMresResta32 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta32.setObjectName(u"txtMresResta32")

        self.gridLayout_10.addWidget(self.txtMresResta32, 3, 1, 1, 1)

        self.txtMresResta13 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta13.setObjectName(u"txtMresResta13")

        self.gridLayout_10.addWidget(self.txtMresResta13, 1, 2, 1, 1)

        self.txtMresResta33 = QLineEdit(self.gridLayoutWidget_5)
        self.txtMresResta33.setObjectName(u"txtMresResta33")

        self.gridLayout_10.addWidget(self.txtMresResta33, 3, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(410, 10, 271, 24))
        self.label_10.setFont(font)
        self.btnCalcularResta = QPushButton(self.tab_2)
        self.btnCalcularResta.setObjectName(u"btnCalcularResta")
        self.btnCalcularResta.setGeometry(QRect(500, 100, 171, 61))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_7 = QWidget(self.tab_3)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(20, 50, 431, 136))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.gridLayoutWidget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_16.addWidget(self.label_14, 0, 2, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.txtMbMulti12 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti12.setObjectName(u"txtMbMulti12")

        self.gridLayout_17.addWidget(self.txtMbMulti12, 1, 1, 1, 1)

        self.txtMbMulti22 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti22.setObjectName(u"txtMbMulti22")

        self.gridLayout_17.addWidget(self.txtMbMulti22, 2, 1, 1, 1)

        self.txtMbMulti11 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti11.setObjectName(u"txtMbMulti11")

        self.gridLayout_17.addWidget(self.txtMbMulti11, 1, 0, 1, 1)

        self.txtMbMulti23 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti23.setObjectName(u"txtMbMulti23")

        self.gridLayout_17.addWidget(self.txtMbMulti23, 2, 2, 1, 1)

        self.txtMbMulti21 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti21.setObjectName(u"txtMbMulti21")

        self.gridLayout_17.addWidget(self.txtMbMulti21, 2, 0, 1, 1)

        self.txtMbMulti32 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti32.setObjectName(u"txtMbMulti32")

        self.gridLayout_17.addWidget(self.txtMbMulti32, 3, 1, 1, 1)

        self.txtMbMulti31 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti31.setObjectName(u"txtMbMulti31")

        self.gridLayout_17.addWidget(self.txtMbMulti31, 3, 0, 1, 1)

        self.txtMbMulti33 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti33.setObjectName(u"txtMbMulti33")

        self.gridLayout_17.addWidget(self.txtMbMulti33, 3, 2, 1, 1)

        self.txtMbMulti13 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMbMulti13.setObjectName(u"txtMbMulti13")

        self.gridLayout_17.addWidget(self.txtMbMulti13, 1, 2, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_17.addWidget(self.label_15, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_16.addLayout(self.gridLayout_17, 0, 3, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.txtMaMulti23 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti23.setObjectName(u"txtMaMulti23")

        self.gridLayout_18.addWidget(self.txtMaMulti23, 2, 2, 1, 1)

        self.txtMaMulti13 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti13.setObjectName(u"txtMaMulti13")

        self.gridLayout_18.addWidget(self.txtMaMulti13, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_18.addWidget(self.label_16, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.txtMaMulti21 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti21.setObjectName(u"txtMaMulti21")

        self.gridLayout_18.addWidget(self.txtMaMulti21, 2, 0, 1, 1)

        self.txtMaMulti22 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti22.setObjectName(u"txtMaMulti22")

        self.gridLayout_18.addWidget(self.txtMaMulti22, 2, 1, 1, 1)

        self.txtMaMulti31 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti31.setObjectName(u"txtMaMulti31")

        self.gridLayout_18.addWidget(self.txtMaMulti31, 3, 0, 1, 1)

        self.txtMaMulti12 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti12.setObjectName(u"txtMaMulti12")

        self.gridLayout_18.addWidget(self.txtMaMulti12, 1, 1, 1, 1)

        self.txtMaMulti33 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti33.setObjectName(u"txtMaMulti33")

        self.gridLayout_18.addWidget(self.txtMaMulti33, 3, 2, 1, 1)

        self.txtMaMulti32 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti32.setObjectName(u"txtMaMulti32")

        self.gridLayout_18.addWidget(self.txtMaMulti32, 3, 1, 1, 1)

        self.txtMaMulti11 = QLineEdit(self.gridLayoutWidget_7)
        self.txtMaMulti11.setObjectName(u"txtMaMulti11")

        self.gridLayout_18.addWidget(self.txtMaMulti11, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_18, 0, 1, 1, 1)

        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(400, 10, 271, 24))
        self.label_17.setFont(font)
        self.gridLayoutWidget_4 = QWidget(self.tab_3)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(20, 340, 151, 141))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.txtMresMulti11 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti11.setObjectName(u"txtMresMulti11")

        self.gridLayout_12.addWidget(self.txtMresMulti11, 1, 0, 1, 1)

        self.txtMresMulti31 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti31.setObjectName(u"txtMresMulti31")

        self.gridLayout_12.addWidget(self.txtMresMulti31, 3, 0, 1, 1)

        self.txtMresMulti23 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti23.setObjectName(u"txtMresMulti23")

        self.gridLayout_12.addWidget(self.txtMresMulti23, 2, 2, 1, 1)

        self.txtMresMulti12 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti12.setObjectName(u"txtMresMulti12")

        self.gridLayout_12.addWidget(self.txtMresMulti12, 1, 1, 1, 1)

        self.txtMresMulti22 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti22.setObjectName(u"txtMresMulti22")

        self.gridLayout_12.addWidget(self.txtMresMulti22, 2, 1, 1, 1)

        self.txtMresMulti21 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti21.setObjectName(u"txtMresMulti21")

        self.gridLayout_12.addWidget(self.txtMresMulti21, 2, 0, 1, 1)

        self.txtMresMulti32 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti32.setObjectName(u"txtMresMulti32")

        self.gridLayout_12.addWidget(self.txtMresMulti32, 3, 1, 1, 1)

        self.txtMresMulti13 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti13.setObjectName(u"txtMresMulti13")

        self.gridLayout_12.addWidget(self.txtMresMulti13, 1, 2, 1, 1)

        self.txtMresMulti33 = QLineEdit(self.gridLayoutWidget_4)
        self.txtMresMulti33.setObjectName(u"txtMresMulti33")

        self.gridLayout_12.addWidget(self.txtMresMulti33, 3, 2, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.btnCalcularMulti = QPushButton(self.tab_3)
        self.btnCalcularMulti.setObjectName(u"btnCalcularMulti")
        self.btnCalcularMulti.setGeometry(QRect(480, 90, 171, 61))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_18 = QLabel(self.tab_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(400, 10, 271, 24))
        self.label_18.setFont(font)
        self.gridLayoutWidget_9 = QWidget(self.tab_4)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(20, 340, 194, 141))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.txtMadjunInversa11 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa11.setObjectName(u"txtMadjunInversa11")

        self.gridLayout_22.addWidget(self.txtMadjunInversa11, 1, 0, 1, 1)

        self.txtMadjunInversa31 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa31.setObjectName(u"txtMadjunInversa31")

        self.gridLayout_22.addWidget(self.txtMadjunInversa31, 3, 0, 1, 1)

        self.txtMadjunInversa23 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa23.setObjectName(u"txtMadjunInversa23")

        self.gridLayout_22.addWidget(self.txtMadjunInversa23, 2, 2, 1, 1)

        self.txtMadjunInversa12 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa12.setObjectName(u"txtMadjunInversa12")

        self.gridLayout_22.addWidget(self.txtMadjunInversa12, 1, 1, 1, 1)

        self.txtMadjunInversa22 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa22.setObjectName(u"txtMadjunInversa22")

        self.gridLayout_22.addWidget(self.txtMadjunInversa22, 2, 1, 1, 1)

        self.txtMadjunInversa21 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa21.setObjectName(u"txtMadjunInversa21")

        self.gridLayout_22.addWidget(self.txtMadjunInversa21, 2, 0, 1, 1)

        self.txtMadjunInversa32 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa32.setObjectName(u"txtMadjunInversa32")

        self.gridLayout_22.addWidget(self.txtMadjunInversa32, 3, 1, 1, 1)

        self.txtMadjunInversa13 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa13.setObjectName(u"txtMadjunInversa13")

        self.gridLayout_22.addWidget(self.txtMadjunInversa13, 1, 2, 1, 1)

        self.txtMadjunInversa33 = QLineEdit(self.gridLayoutWidget_9)
        self.txtMadjunInversa33.setObjectName(u"txtMadjunInversa33")

        self.gridLayout_22.addWidget(self.txtMadjunInversa33, 3, 2, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_22.addWidget(self.label_24, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayoutWidget_10 = QWidget(self.tab_4)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 40, 151, 141))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.txtMaInversa11 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa11.setObjectName(u"txtMaInversa11")

        self.gridLayout_23.addWidget(self.txtMaInversa11, 1, 0, 1, 1)

        self.txtMaInversa31 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa31.setObjectName(u"txtMaInversa31")

        self.gridLayout_23.addWidget(self.txtMaInversa31, 3, 0, 1, 1)

        self.txtMaInversa23 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa23.setObjectName(u"txtMaInversa23")

        self.gridLayout_23.addWidget(self.txtMaInversa23, 2, 2, 1, 1)

        self.txtMaInversa12 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa12.setObjectName(u"txtMaInversa12")

        self.gridLayout_23.addWidget(self.txtMaInversa12, 1, 1, 1, 1)

        self.txtMaInversa22 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa22.setObjectName(u"txtMaInversa22")

        self.gridLayout_23.addWidget(self.txtMaInversa22, 2, 1, 1, 1)

        self.txtMaInversa21 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa21.setObjectName(u"txtMaInversa21")

        self.gridLayout_23.addWidget(self.txtMaInversa21, 2, 0, 1, 1)

        self.txtMaInversa32 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa32.setObjectName(u"txtMaInversa32")

        self.gridLayout_23.addWidget(self.txtMaInversa32, 3, 1, 1, 1)

        self.txtMaInversa13 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa13.setObjectName(u"txtMaInversa13")

        self.gridLayout_23.addWidget(self.txtMaInversa13, 1, 2, 1, 1)

        self.txtMaInversa33 = QLineEdit(self.gridLayoutWidget_10)
        self.txtMaInversa33.setObjectName(u"txtMaInversa33")

        self.gridLayout_23.addWidget(self.txtMaInversa33, 3, 2, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_23.addWidget(self.label_25, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayoutWidget_11 = QWidget(self.tab_4)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(250, 310, 194, 141))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.gridLayoutWidget_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_24.addWidget(self.label_26, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.txtDeterInversa = QLineEdit(self.gridLayoutWidget_11)
        self.txtDeterInversa.setObjectName(u"txtDeterInversa")

        self.gridLayout_24.addWidget(self.txtDeterInversa, 1, 0, 1, 3)

        self.gridLayoutWidget_12 = QWidget(self.tab_4)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(470, 340, 194, 141))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.txtMinversaInversa11 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa11.setObjectName(u"txtMinversaInversa11")

        self.gridLayout_26.addWidget(self.txtMinversaInversa11, 1, 0, 1, 1)

        self.txtMinversaInversa31 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa31.setObjectName(u"txtMinversaInversa31")

        self.gridLayout_26.addWidget(self.txtMinversaInversa31, 3, 0, 1, 1)

        self.txtMinversaInversa23 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa23.setObjectName(u"txtMinversaInversa23")

        self.gridLayout_26.addWidget(self.txtMinversaInversa23, 2, 2, 1, 1)

        self.txtMinversaInversa12 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa12.setObjectName(u"txtMinversaInversa12")

        self.gridLayout_26.addWidget(self.txtMinversaInversa12, 1, 1, 1, 1)

        self.txtMinversaInversa22 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa22.setObjectName(u"txtMinversaInversa22")

        self.gridLayout_26.addWidget(self.txtMinversaInversa22, 2, 1, 1, 1)

        self.txtMinversaInversa21 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa21.setObjectName(u"txtMinversaInversa21")

        self.gridLayout_26.addWidget(self.txtMinversaInversa21, 2, 0, 1, 1)

        self.txtMinversaInversa32 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa32.setObjectName(u"txtMinversaInversa32")

        self.gridLayout_26.addWidget(self.txtMinversaInversa32, 3, 1, 1, 1)

        self.txtMinversaInversa13 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa13.setObjectName(u"txtMinversaInversa13")

        self.gridLayout_26.addWidget(self.txtMinversaInversa13, 1, 2, 1, 1)

        self.txtMinversaInversa33 = QLineEdit(self.gridLayoutWidget_12)
        self.txtMinversaInversa33.setObjectName(u"txtMinversaInversa33")

        self.gridLayout_26.addWidget(self.txtMinversaInversa33, 3, 2, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_26.addWidget(self.label_28, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.btnCalcularInversa = QPushButton(self.tab_4)
        self.btnCalcularInversa.setObjectName(u"btnCalcularInversa")
        self.btnCalcularInversa.setGeometry(QRect(260, 70, 171, 61))
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UNIVERSIDAD CAT\u00d3LICA DE EL SALVADOR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FACTULDAD DE INGENIER\u00cdA Y ARQUITECTURA", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"PARCIAL M\u00c9TODOS NUM\u00c9RICOS", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"M\u00c9TODOS NUM\u00c9RICOS SECCI\u00d3N \"B\"", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"PRESENTADO POR:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"DOCENTE:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Nataly Yamileth Solis Cortez", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Christopher Banejam\u00edn Vanegas Azucena", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"D\u00e9bora Alexandra Mendoza\u00a0Pineda", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Ma. Rafael Leonardo Jim\u00e9nez Alvar\u00e9z", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"SANTA ANA, 27 DE FEBRERO DE 2025", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"PORTADA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RESPUESTA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SOLO INGRESAR NUMEROS", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"SUMAR", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"MATRIZ B", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"MATRIZ A", None))
        self.btnCalcularSum.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"SUMA", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"RESTAR", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MATRIZ B", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"MATRIZ A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RESPUESTA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SOLO INGRESAR NUMEROS", None))
        self.btnCalcularResta.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"RESTA", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MULTIPLICAR", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MATRIZ B", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"MATRIZ A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"SOLO INGRESAR NUMEROS", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"RESPUESTA", None))
        self.btnCalcularMulti.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"MULTIPLICACION", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"SOLO INGRESAR NUMEROS", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ADJUNTA", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"MATRIZ A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"DETERMINANTE", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"INVERSA", None))
        self.btnCalcularInversa.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"INVERSA", None))
    # retranslateUi

