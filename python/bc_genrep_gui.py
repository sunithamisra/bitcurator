# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bc_genrep_gui.ui'
#
# Created: Tue May 21 21:37:01 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(711, 459)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 115, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 30, 271, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(565, 423, 137, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 130, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 300, 85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 300, 61, 21))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 130, 51, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(565, 200, 85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(468, 200, 71, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(9, 299, 45, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 300, 271, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 138, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 273, 27))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 120, 91, 27))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 120, 273, 27))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 50, 81, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.update)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_2.setText)
        QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_3.setText)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit.setText)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Config File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("Form", "/home/sunitha/BC/bitcurator-master/t", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setPlaceholderText(QtGui.QApplication.translate("Form", "~/BC/bitcurator-master/python", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Generate Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_7.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Outdir", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/charlie_xml_outdir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Annotated directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/annotated_charlie_output", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "fiwalk xmlfile", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/charlie.xml", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

