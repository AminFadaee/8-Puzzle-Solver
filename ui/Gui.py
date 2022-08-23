# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QPushButton, QLabel, QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(165, 290)
        Form.setStyleSheet(_fromUtf8("background-color: b;"))
        self.bt1 = QPushButton(Form)
        self.bt1.setGeometry(QtCore.QRect(10, 10, 45, 45))
        self.bt1.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt1.setObjectName(_fromUtf8("bt1"))
        self.bt2 = QPushButton(Form)
        self.bt2.setGeometry(QtCore.QRect(60, 10, 45, 45))
        self.bt2.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt2.setObjectName(_fromUtf8("bt2"))
        self.bt3 = QPushButton(Form)
        self.bt3.setGeometry(QtCore.QRect(110, 10, 45, 45))
        self.bt3.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt3.setObjectName(_fromUtf8("bt3"))
        self.bt6 = QPushButton(Form)
        self.bt6.setGeometry(QtCore.QRect(110, 60, 45, 45))
        self.bt6.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt6.setObjectName(_fromUtf8("bt6"))
        self.bt5 = QPushButton(Form)
        self.bt5.setGeometry(QtCore.QRect(60, 60, 45, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.bt5.setFont(font)
        self.bt5.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt5.setObjectName(_fromUtf8("bt5"))
        self.bt4 = QPushButton(Form)
        self.bt4.setGeometry(QtCore.QRect(10, 60, 45, 45))
        self.bt4.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt4.setObjectName(_fromUtf8("bt4"))
        self.bt7 = QPushButton(Form)
        self.bt7.setGeometry(QtCore.QRect(10, 110, 45, 45))
        self.bt7.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt7.setObjectName(_fromUtf8("bt7"))
        self.bt8 = QPushButton(Form)
        self.bt8.setGeometry(QtCore.QRect(60, 110, 45, 45))
        self.bt8.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.bt8.setObjectName(_fromUtf8("bt8"))
        self.btsol = QPushButton(Form)
        self.btsol.setGeometry(QtCore.QRect(10, 205, 145, 30))
        self.btsol.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.btsol.setObjectName(_fromUtf8("btsol"))
        self.movesLab = QLabel(Form)
        self.movesLab.setGeometry(QtCore.QRect(10, 240, 140, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("comic sans ms"))
        self.movesLab.setFont(font)
        self.movesLab.setStyleSheet(_fromUtf8("color:grey; font-family:\'comic sans ms\'"))
        self.movesLab.setText(_fromUtf8(""))
        self.movesLab.setAlignment(QtCore.Qt.AlignCenter)
        self.movesLab.setObjectName(_fromUtf8("movesLab"))
        self.timeLab = QLabel(Form)
        self.timeLab.setGeometry(QtCore.QRect(10, 261, 140, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("comic sans ms"))
        self.timeLab.setFont(font)
        self.timeLab.setStyleSheet(_fromUtf8("color:grey; font-family:\'comic sans ms\'"))
        self.timeLab.setText(_fromUtf8(""))
        self.timeLab.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLab.setObjectName(_fromUtf8("timeLab"))
        self.btrand = QPushButton(Form)
        self.btrand.setGeometry(QtCore.QRect(10, 170, 145, 30))
        self.btrand.setStyleSheet(_fromUtf8("background-color:grey;\n"
"border-radius: 5px;\n"
"border-radius: 5px;\n"
"border-radius:5px;\n"
"border-color:black;\n"
"color: b;\n"
"font-family: \'Comic Sans MS\';\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"border:\'solid\';"))
        self.btrand.setObjectName(_fromUtf8("btrand"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.bt1.setText(_translate("Form", "1", None))
        self.bt2.setText(_translate("Form", "2", None))
        self.bt3.setText(_translate("Form", "3", None))
        self.bt6.setText(_translate("Form", "6", None))
        self.bt5.setText(_translate("Form", "5", None))
        self.bt4.setText(_translate("Form", "4", None))
        self.bt7.setText(_translate("Form", "7", None))
        self.bt8.setText(_translate("Form", "8", None))
        self.btsol.setText(_translate("Form", "Solve", None))
        self.btrand.setText(_translate("Form", "Randomize", None))

