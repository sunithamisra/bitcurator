# -*- coding: utf-8 -*-
#
# BitCurator
# Copyright (C) 2012
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
# Original implementation generated from reading ui file 
# 'bitcurator_fiwalk_xml.ui' Created: Sun Jun 30 11:29:1 
# by: PyQt4 UI code generator 4.9.1
# Modified for running Fiwalk command given the image file.
#

from PyQt4 import QtCore, QtGui
from subprocess import Popen,PIPE
try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FiwalkXMLFileGeneration(object):
    imageFileName = "null"
    xmlFileName = "null"
    TextFileName = "null"
    def setupUi(self, FiwalkXMLFileGeneration):
        FiwalkXMLFileGeneration.setObjectName(_fromUtf8("FiwalkXMLFileGeneration"))
        FiwalkXMLFileGeneration.resize(521, 453)
        self.buttonBox = QtGui.QDialogButtonBox(FiwalkXMLFileGeneration)
        self.buttonBox.setGeometry(QtCore.QRect(140, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(FiwalkXMLFileGeneration)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(FiwalkXMLFileGeneration)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 141, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(FiwalkXMLFileGeneration)
        self.label.setGeometry(QtCore.QRect(50, 16, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(FiwalkXMLFileGeneration)
        self.label_2.setGeometry(QtCore.QRect(50, 86, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(FiwalkXMLFileGeneration)
        self.textEdit.setGeometry(QtCore.QRect(35, 190, 431, 151))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.toolButton = QtGui.QToolButton(FiwalkXMLFileGeneration)
        self.toolButton.setGeometry(QtCore.QRect(210, 40, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(FiwalkXMLFileGeneration)
        self.toolButton_2.setGeometry(QtCore.QRect(210, 110, 23, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))

        self.retranslateUi(FiwalkXMLFileGeneration)

        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getImageFileName)

        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputXmlFilePath)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOk)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FiwalkXMLFileGeneration.reject)
        QtCore.QMetaObject.connectSlotsByName(FiwalkXMLFileGeneration)

        self.toolButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))

    def buttonClickedOk(self):

        # The standard output from this point is placed by an in-memory 
        # buffer.
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        # If Image file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit.text() != self.imageFileName:
            self.imageFileName = ui.lineEdit.text()
            ## print("D: Image File Selected from the box: ", self.imageFileName)

        # If output XML file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_2.text() != self.xmlFileName:
            self.xmlFileName = ui.lineEdit_2.text()
            self.TextFileName = self.xmlFileName + '.txt'
            ## print("D: XML File Selected from the box: ", self.xmlFileName)

        cmd = ['fiwalk', '-f', '-X', self.xmlFileName, '-T', self.TextFileName, self.imageFileName]
        print(">> Command Executed for Fiwalk = ", cmd)

        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()

        if len(err) > 0 :
           #sys.stderr.write("Debug: type(err) = %r.\n" % type(err))
           # Terminate the redirecting of the stdout to the in-memory buffer.
           print(">> ERROR!!! Fiwalk terminated with error: \n", err)
           self.textEdit.setText( sys.stdout.getvalue() )
           sys.stdout = self.oldstdout
           raise ValueError("fiwalk error (" + str(err).strip() + "): "+" ".join(cmd))
        else:
           print("\n>>  Success!!! Fiwalk crated the following files: \n")
           print("    o ", self.xmlFileName)
           print("    o ", self.TextFileName)
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def getImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName()
        ## print("D: Fiwalk Image File Selected: ", image_file)

        self.lineEdit.setText(image_file)
        
        self.imageFileName = image_file

    def getOutputXmlFilePath(self):
        # Navigation
        xml_output_file = QtGui.QFileDialog.getSaveFileName()
        ## print("D: Fiwalk XML File Selected: ", xml_output_file)

        self.lineEdit_2.setText(xml_output_file)
        
        self.xmlFileName = xml_output_file
        self.TextFileName = xml_output_file + '.txt'

    def retranslateUi(self, FiwalkXMLFileGeneration):
        FiwalkXMLFileGeneration.setWindowTitle(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "Image file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "Output XML File (new)", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("FiwalkXMLFileGeneration", "...", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FiwalkXMLFileGeneration = QtGui.QDialog()
    ui = Ui_FiwalkXMLFileGeneration()
    ui.setupUi(FiwalkXMLFileGeneration)
    FiwalkXMLFileGeneration.show()
    sys.exit(app.exec_())

