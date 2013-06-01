# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bc_genrep_gui.ui'
#
# Created: Sun May 26 15:35:39 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    fiwalkXmlFileName = "null"
    beAnnotatedDirName = "null"
    outputDirName = "null"
    configFileName = "null"

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(436, 511)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 211, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 220, 271, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 201, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 160, 271, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 291, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 273, 27))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 27))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 273, 27))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(210, 470, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(290, 40, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        #self.fileDialog = QtGui.QFileDialog()
        ##self.fileDialog = QtGui.QFileDialog()
        ##self.fileDialog.show()

        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(290, 100, 23, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(290, 160, 23, 25))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 300, 421, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 171, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(290, 220, 23, 25))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))

        self.retranslateUi(Form)

        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFiwalkXmlFileName)

        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeAnnotatedDir)

        QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputDir)

        QtCore.QObject.connect(self.toolButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getConfigFile)
        
        print("SELECTED TEXT: ", self.fiwalkXmlFileName)
        ##self.lineEdit.text = QtCore.QString.selectedText()


        QtCore.QMetaObject.connectSlotsByName(Form)
   
    def getFiwalkXmlFileName(self):
        path = QtGui.QFileDialog.getOpenFileName()
        print("Fiwalk XML File Selected: ", path)
        self.lineEdit.setText(path)
        self.fiwalkXmlFileName = path
        return path

    def getBeAnnotatedDir(self):
        # FIXME: Follow the method used above for all the cases
        # even though they work fine the way they are.
        self.fileDialog = QtGui.QFileDialog()
        path = self.fileDialog.getOpenFileName()
        print("Annotated Dir: ", path)
        self.lineEdit_2.setText(path)
        self.beAnnotatedDirName = path
        return path

    def getOutputDir(self):
        self.fileDialog = QtGui.QFileDialog()
        path = self.fileDialog.getOpenFileName()
        print("Output Dir: ", path)
        self.lineEdit_3.setText(path)
        self.outputDirName = path
        return path

    def getConfigFile(self):
        self.fileDialog = QtGui.QFileDialog()
        path = self.fileDialog.getOpenFileName()
        print("Output Dir: ", path)
        self.lineEdit_4.setText(path)
        self.configFileName = path
        return path

    def selectXmlFile(self):
        ##self.fileDialog = self.getFileName(self.lineEdit)
        self.lineEdit.setText(self.fileDialog.getOpenFileName())
        text = self.lineEdit.text()
        
        print("SELECTED TEXT: ", text)

    def getFileName1(self, le):
        fileDialog = QtGui.QFileDialog()
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), fileDialog.show)
        return (fileDialog)
      
    def selectFile():
        lineEdit.setText(QFileDialog.getOpenFileName())

    #pushButton.clicked.connect(selectFile)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("Form", "/home/sunitha/BC/bitcurator-master/t", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setPlaceholderText(QtGui.QApplication.translate("Form", "~/BC/bitcurator-master/python", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Output directory for reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/charlie_xml_outdir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Annotated Bulk Extractor output directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/annotated_charlie_output", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Fiwalk XML file:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/charlie.xml", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Command line output:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    print("SELECTING XML FILE")
    ##ui.selectXmlFile()
    sys.exit(app.exec_())

