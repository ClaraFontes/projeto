# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(442, 694)
        self.frame = QtWidgets.QFrame(Inicio)
        self.frame.setGeometry(QtCore.QRect(10, 10, 421, 671))
        self.frame.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_comprar = QtWidgets.QPushButton(self.frame)
        self.bt_comprar.setGeometry(QtCore.QRect(100, 380, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_comprar.setFont(font)
        self.bt_comprar.setStyleSheet("QPushButton{\n"
"    background-color: rgba(221, 33, 33, 0.99);\n"
"    border-radius: 12px;\n"
"    color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 206, 137);\n"
"    border-radius: 12px;\n"
"    color: rgb(100, 76, 47);\n"
"}")
        self.bt_comprar.setObjectName("bt_comprar")
        self.bt_vender = QtWidgets.QPushButton(self.frame)
        self.bt_vender.setEnabled(True)
        self.bt_vender.setGeometry(QtCore.QRect(100, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_vender.setFont(font)
        self.bt_vender.setStyleSheet("QPushButton{\n"
"    background-color: rgba(221, 33, 33, 0.99);\n"
"    border-radius: 12px;\n"
"    color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 206, 137);\n"
"    border-radius: 12px;\n"
"    color: rgb(100, 76, 47);\n"
"}\n"
"")
        self.bt_vender.setObjectName("bt_vender")
        self.tck = QtWidgets.QLabel(self.frame)
        self.tck.setGeometry(QtCore.QRect(130, 160, 151, 101))
        self.tck.setStyleSheet("")
        self.tck.setText("")
        self.tck.setPixmap(QtGui.QPixmap("../imgs/tickets.png"))
        self.tck.setScaledContents(True)
        self.tck.setObjectName("tck")
        self.bt_comprar.raise_()
        self.tck.raise_()
        self.bt_vender.raise_()

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Início"))
        self.bt_comprar.setText(_translate("Inicio", "COMPRAR INGRESSOS"))
        self.bt_vender.setText(_translate("Inicio", "VENDER EVENTO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QWidget()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())
