#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=UTF-8

# Form implementation generated from reading ui file 'bc_genrep_gui.ui'
#
# Created: Sun May 26 15:35:39 2013
#      by: PyQt4 UI code generator 4.9.1, modified manually
#

import os
from PyQt4 import QtCore, QtGui

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

from generate_report import *
from bc_utils import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    fiwalkXmlFileName = "null"
    beAnnotatedDirName = "null"
    outputDirName = "null"
    configFileName = "null"

    # DEBUG: The below lines are for bypassing gui - for test purposes only.
    # Comment out the above 4 lines for testing
    '''
    fiwalkXmlFileName = "/home/sunitha/Research/TestData/BEO_master/charlie_fi_F.xml"
    beAnnotatedDirName = "/home/sunitha/Research/TestData/BEO_master/annotated_charlie_output"
    outputDirName = "/home/sunitha/Research/TestData/BEO_master/charlie_xml_outdir"
    configFileName = "/home/sunitha/BC/bitcurator-master/python/t"
    '''
 
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(436, 511)
        self.label_configFile = QtGui.QLabel(Form)
        self.label_configFile.setGeometry(QtCore.QRect(10, 200, 211, 17))
        self.label_configFile.setObjectName(_fromUtf8("label_configFile"))
        self.lineEdit_configFile = QtGui.QLineEdit(Form)
        self.lineEdit_configFile.setGeometry(QtCore.QRect(10, 220, 271, 31))
        self.lineEdit_configFile.setObjectName(_fromUtf8("lineEdit_configFile"))
        self.label_outdir = QtGui.QLabel(Form)
        self.label_outdir.setGeometry(QtCore.QRect(10, 140, 201, 17))
        self.label_outdir.setObjectName(_fromUtf8("label_outdir"))
        self.lineEdit_outdir = QtGui.QLineEdit(Form)
        self.lineEdit_outdir.setGeometry(QtCore.QRect(10, 160, 271, 27))
        self.lineEdit_outdir.setObjectName(_fromUtf8("lineEdit_outdir"))
        self.label_annDir = QtGui.QLabel(Form)
        self.label_annDir.setGeometry(QtCore.QRect(10, 70, 291, 27))
        self.label_annDir.setObjectName(_fromUtf8("label_annDir"))
        self.lineEdit_annDir = QtGui.QLineEdit(Form)
        self.lineEdit_annDir.setGeometry(QtCore.QRect(10, 100, 273, 27))
        self.lineEdit_annDir.setText(_fromUtf8(""))
        self.lineEdit_annDir.setObjectName(_fromUtf8("lineEdit_annDir"))
        self.label_xmlfile = QtGui.QLabel(Form)
        self.label_xmlfile.setGeometry(QtCore.QRect(10, 10, 131, 27))
        self.label_xmlfile.setObjectName(_fromUtf8("label_xmlfile"))
        self.lineEdit_xmlFile = QtGui.QLineEdit(Form)
        self.lineEdit_xmlFile.setGeometry(QtCore.QRect(10, 40, 273, 27))
        self.lineEdit_xmlFile.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_xmlFile.setText(_fromUtf8(""))
        self.lineEdit_xmlFile.setObjectName(_fromUtf8("lineEdit_xmlFile"))
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(210, 470, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(290, 40, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        ret = self.buttonBox.clicked.connect(self.buttonClicked)

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
        # If file not selected through menu, see if it is typed in the box
        if self.fiwalkXmlFileName == "null":
            self.fiwalkXmlFileName  = ui.lineEdit_xmlFile.text()
            print("Fiwalk XML FIle Selected from the box: ", self.fiwalkXmlFileName)

        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeAnnotatedDir)

        if self.beAnnotatedDirName == "null":
            self.beAnnotatedDirName = ui.lineEdit_annDir.text()
            print("Annotated Directory Selected fron the box: ", self.beAnnotatedDirName)
        QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputDir)

        if self.outputDirName == "null":
            self.outputDirName = ui.lineEdit_outdir.text()
            print("Output Directory selected from the box: ", self.outputDirName)

        QtCore.QObject.connect(self.toolButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getConfigFile)
        if self.configFileName == '':
            self.configFileName  = ui.lineEdit_configFile.text()
            print("Config File selected from the box: ", self.configFileName)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def readOutput(self):
        self.textBrowser2.append(QString(self.process.readStdout()))
        if self.process.isRunning()==False:
            self.textBrowser2.append("\n Completed Successfully")
        
    def buttonClicked(self, button):
        print("(delete me): CLICKED", self, button)

        # Use the default config file if not provided
        if (self.configFileName == "null"):
            self.configFileName = "/etc/bitcurator/bc_report_config.txt"
        
        print("Generating Reports: config_file: ", self.configFileName)
        print("Fiwalk XML File : ", self.fiwalkXmlFileName)
        print("Annotated Dir: ", self.beAnnotatedDirName)
        print("outdir: ", self.outputDirName)
        use_config_file = True  ## FIXME
            
        bc_get_reports(PdfReport, FiwalkReport, self.fiwalkXmlFileName, \
                                 self.beAnnotatedDirName, \
                                 self.outputDirName, \
                                 self.configFileName)              

        QtCore.QCoreApplication.instance().quit()
   
    def getFiwalkXmlFileName(self):
        xml_file = QtGui.QFileDialog.getOpenFileName()

        print("Fiwalk XML File Selected: ", xml_file)

        self.lineEdit_xmlFile.setText(xml_file)

        # If file not selected through menu, see if it is typed in the box
        if xml_file == '':
            xml_file = ui.lineEdit_xmlFile.text()
            print("FFFFFiwalk XML FIle Selected from the box: ", xml_file)

        self.fiwalkXmlFileName = xml_file
        return xml_file

    def getBeAnnotatedDir(self):
        ann_dir = QtGui.QFileDialog.getExistingDirectory()
        print("Annotated Directory Selected: ", ann_dir)
        ####if ann_dir == '':
            ####ann_dir = ui.lineEdit_annDir.text()
            ####print("Annotated Directory Selected fron the box: ", ann_dir)
 
        self.lineEdit_annDir.setText(ann_dir)
        self.beAnnotatedDirName = ann_dir
        return ann_dir

    def getOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName()
        print("Output Directory Selected: ", outdir)

        if outdir == '':
            outdir = ui.lineEdit_outdir.text()
            print("Output Directory selected from the box: ", outdir)
        self.lineEdit_outdir.setText(outdir)
        self.outputDirName = outdir
        return outdir

    def getConfigFile(self):
        config_file = QtGui.QFileDialog.getOpenFileName()
        print("Config File Selected: ", config_file)

        self.lineEdit_configFile.setText(config_file)
        self.configFileName = config_file
        return config_file

    def getFileName1(self, le):
        fileDialog = QtGui.QFileDialog()
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), fileDialog.show)
        return (fileDialog)

    def selectFile():
        lineEdit.setText(QFileDialog.getOpenFileName())

    #pushButton.clicked.connect(selectFile)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_configFile.setText(QtGui.QApplication.translate("Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_configFile.setText(QtGui.QApplication.translate("Form", "/home/sunitha/BC/bitcurator-master/t", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_configFile.setPlaceholderText(QtGui.QApplication.translate("Form", "~/BC/bitcurator-master/python", None, QtGui.QApplication.UnicodeUTF8))
        self.label_outdir.setText(QtGui.QApplication.translate("Form", "Output directory for reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_outdir.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/charlie_xml_outdir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_annDir.setText(QtGui.QApplication.translate("Form", "Annotated Bulk Extractor output directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_annDir.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/annotated_charlie_output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_xmlfile.setText(QtGui.QApplication.translate("Form", "Fiwalk XML file:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_xmlFile.setPlaceholderText(QtGui.QApplication.translate("Form", "/home/sunitha/Research/TestData/BEO_master/charlie.xml", None, QtGui.QApplication.UnicodeUTF8))
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

    sys.exit(app.exec_())

