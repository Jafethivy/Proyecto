# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\POO\PROYECTOS\Proyectoe\Ui\Menu\u_mesa1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 669)
        self.cuenta1 = QtWidgets.QTableWidget(Dialog)
        self.cuenta1.setGeometry(QtCore.QRect(370, 10, 401, 531))
        self.cuenta1.setObjectName("cuenta1")
        self.cuenta1.setColumnCount(3)
        self.cuenta1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cuenta1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cuenta1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cuenta1.setHorizontalHeaderItem(2, item)
        self.cuenta1.horizontalHeader().setMinimumSectionSize(40)
        self.cuenta1.verticalHeader().setMinimumSectionSize(40)
        self.total1 = QtWidgets.QLabel(Dialog)
        self.total1.setGeometry(QtCore.QRect(630, 550, 91, 16))
        self.total1.setObjectName("total1")
        self.arroz1 = QtWidgets.QPushButton(Dialog)
        self.arroz1.setGeometry(QtCore.QRect(50, 60, 131, 61))
        self.arroz1.setObjectName("arroz1")
        self.pera1 = QtWidgets.QPushButton(Dialog)
        self.pera1.setGeometry(QtCore.QRect(200, 60, 131, 61))
        self.pera1.setObjectName("pera1")
        self.hamburguesa1 = QtWidgets.QPushButton(Dialog)
        self.hamburguesa1.setGeometry(QtCore.QRect(50, 140, 131, 61))
        self.hamburguesa1.setObjectName("hamburguesa1")
        self.pizza1 = QtWidgets.QPushButton(Dialog)
        self.pizza1.setGeometry(QtCore.QRect(200, 140, 131, 61))
        self.pizza1.setObjectName("pizza1")
        self.borrar = QtWidgets.QPushButton(Dialog)
        self.borrar.setGeometry(QtCore.QRect(380, 550, 93, 28))
        self.borrar.setObjectName("borrar")
        self.arroz1_2 = QtWidgets.QPushButton(Dialog)
        self.arroz1_2.setGeometry(QtCore.QRect(200, 210, 131, 61))
        self.arroz1_2.setObjectName("arroz1_2")
        self.arroz1_3 = QtWidgets.QPushButton(Dialog)
        self.arroz1_3.setGeometry(QtCore.QRect(50, 210, 131, 61))
        self.arroz1_3.setObjectName("arroz1_3")
        self.arroz1_4 = QtWidgets.QPushButton(Dialog)
        self.arroz1_4.setGeometry(QtCore.QRect(50, 280, 131, 61))
        self.arroz1_4.setObjectName("arroz1_4")
        self.arroz1_5 = QtWidgets.QPushButton(Dialog)
        self.arroz1_5.setGeometry(QtCore.QRect(200, 280, 131, 61))
        self.arroz1_5.setObjectName("arroz1_5")
        self.arroz1_6 = QtWidgets.QPushButton(Dialog)
        self.arroz1_6.setGeometry(QtCore.QRect(50, 350, 131, 61))
        self.arroz1_6.setObjectName("arroz1_6")
        self.arroz1_7 = QtWidgets.QPushButton(Dialog)
        self.arroz1_7.setGeometry(QtCore.QRect(200, 350, 131, 61))
        self.arroz1_7.setObjectName("arroz1_7")
        self.arroz1_8 = QtWidgets.QPushButton(Dialog)
        self.arroz1_8.setGeometry(QtCore.QRect(50, 420, 131, 61))
        self.arroz1_8.setObjectName("arroz1_8")
        self.arroz1_9 = QtWidgets.QPushButton(Dialog)
        self.arroz1_9.setGeometry(QtCore.QRect(200, 420, 131, 61))
        self.arroz1_9.setObjectName("arroz1_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.cuenta1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Producto"))
        item = self.cuenta1.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Cantidad"))
        item = self.cuenta1.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Precio"))
        self.total1.setText(_translate("Dialog", "TOTAL"))
        self.arroz1.setText(_translate("Dialog", "ARROZ"))
        self.pera1.setText(_translate("Dialog", "PERA"))
        self.hamburguesa1.setText(_translate("Dialog", "HAMBURGUESA"))
        self.pizza1.setText(_translate("Dialog", "PIZZA"))
        self.borrar.setText(_translate("Dialog", "BORRAR FILA"))
        self.arroz1_2.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_3.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_4.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_5.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_6.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_7.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_8.setText(_translate("Dialog", "ARROZ"))
        self.arroz1_9.setText(_translate("Dialog", "ARROZ"))
