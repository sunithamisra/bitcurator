#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=UTF-8
#
# BitCurator
# Copyright (C) 2012
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
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
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

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
    ### Uncomment for debugging only
    fiwalkXmlFileName = "/home/sunitha/Research/TestData/BEO_master/charlie_fi_F.xml"
    beAnnotatedDirName = "/home/sunitha/Research/TestData/BEO_master/annotated_charlie_output"
    outputDirName = "/home/sunitha/Research/TestData/BEO_master/charlie_xml_outdir"
    configFileName = "/home/sunitha/BC/bitcurator-master/python/t"
    '''
 
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Generate Report"))
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
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOk)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(290, 40, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))


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
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def readOutput(self):
        self.textBrowser2.append(QString(self.process.readStdout()))
        if self.process.isRunning()==False:
            self.textBrowser2.append("\n Completed Successfully")

    # bc_check_parameters: Check if the selected files exist. Also
    # if the text entered in the boxes doesn't match what was selected
    # by navigating through directory structure, use the text in the
    # box as the final selection.
    def bc_check_parameters(self):
        # If XML file not selected through menu, see if it is typed in the box:

        if ui.lineEdit_xmlFile.text() != self.fiwalkXmlFileName:
            self.fiwalkXmlFileName  = ui.lineEdit_xmlFile.text()
            # print("D:Fiwalk XML FIle Selected from the box: ", self.fiwalkXmlFileName)
        if not os.path.exists(self.fiwalkXmlFileName):
            print("XML File %s does not exist. Aborting" %self.fiwalkXmlFileName)
            return (-1)         

        # If Annotated file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_annDir.text() != self.beAnnotatedDirName:
            self.beAnnotatedDirName = ui.lineEdit_annDir.text()
            # print("D: Annotated Directory Selected from the box: ", self.beAnnotatedDirName)

        if not os.path.exists(self.beAnnotatedDirName):
            print("BE Annotated Directory %s does not exist. Aborting" %self.beAnnotatedDirName)
            return (-1)         

        # If Outdir is not selected through menu, see if it is typed 
        # in the text box: 
        if ui.lineEdit_outdir.text() != self.outputDirName:
            self.outputDirName = ui.lineEdit_outdir.text()
            # print("D: Output Directory selected from the box: ", self.outputDirName)
        # The directory is not supposed to exist. Return -1 if it does. 
        if (os.path.exists(self.outputDirName)):
            print(">> Error: Output Directory %s exists. " %self.outputDirName)
            return (-1)         

        if ui.lineEdit_configFile.text() != self.configFileName:
            self.configFileName  = ui.lineEdit_configFile.text()
            # print("D: Config File selected from the box: ", self.configFileName)

        # If config file is not provided by the user, user the default one
        if not os.path.exists(self.configFileName):
            print(">> Using the default config file: /etc/bitcurator/bc_report_config.txt")
            self.configFileName = "/etc/bitcurator/bc_report_config.txt"

        return (0)

    # buttonClickCancel: This called by any click that represents the
    # "Reject" role - Cancel and Close here. It just terminates the Gui.
    def buttonClickedCancel(self):
        QtCore.QCoreApplication.instance().quit()
        
    # buttonClickedOk: Routine invoked when the OK button is clicked.
    # Using StringIO (equivalent to cStringIO in Python-2.x), the stdio is
    # redirected into an in-memory buffer, which is displayed in the 
    # text window at the end.
    def buttonClickedOk(self):

        use_config_file = True

        # The standard output from this point is placed by an in-memory 
        # buffer.
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()
            
        # Check if the indicated files exist. If not, return after 
        # printing the error. Also terminate the redirecting of the 
        # stdout to the in-memory buffer.
        if self.bc_check_parameters() == -1:
            print(">> Report Generation is Aborted ")
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            return

        # All fine. Generate the reports now.
        bc_get_reports(PdfReport, FiwalkReport, self.fiwalkXmlFileName, \
                                 self.beAnnotatedDirName, \
                                 self.outputDirName, \
                                 self.configFileName)              

        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

        # We will not quit from the Gui window until the user clicks
        # on Close.
        # QtCore.QCoreApplication.instance().quit()
   
    # getFiralkXmlFileName: Routine to let the user choose the XML file -
    # by navigating trough the directories
    def getFiwalkXmlFileName(self):

        # Navigation
        xml_file = QtGui.QFileDialog.getOpenFileName()
        # print("D: Fiwalk XML File Selected: ", xml_file)

        self.lineEdit_xmlFile.setText(xml_file)

        self.fiwalkXmlFileName = xml_file
        return xml_file

    # getBeAnnotatedDir: Routine to let the user choose the Directory name 
    # containing the annotated files by navigating 
    def getBeAnnotatedDir(self):
        ann_dir = QtGui.QFileDialog.getExistingDirectory()
        # print("D: Annotated Directory Selected by navigating: ", ann_dir)
 
        self.lineEdit_annDir.setText(ann_dir)
        self.beAnnotatedDirName = ann_dir
        return ann_dir

    # getOutputDir: Routine to let the user choose the Directory name 
    # to output the reports by navigating 
    def getOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName()

        # print("D: Output Directory Selected by navigating: ", outdir)

        self.lineEdit_outdir.setText(outdir)
        self.outputDirName = outdir
        return outdir

    # getConfigFile: Select the config file from the directory structure.
    def getConfigFile(self):
        config_file = QtGui.QFileDialog.getOpenFileName()
        print("D: Config File Selected by navigating: ", config_file)

        self.lineEdit_configFile.setText(config_file)
        self.configFileName = config_file
        return config_file

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Generate Report", "Bitcurator Generate Report", None, QtGui.QApplication.UnicodeUTF8))
        self.label_configFile.setText(QtGui.QApplication.translate("Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_configFile.setPlaceholderText(QtGui.QApplication.translate("Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_configFile.setPlaceholderText(QtGui.QApplication.translate("Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_outdir.setText(QtGui.QApplication.translate("Form", "Output directory for reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_outdir.setPlaceholderText(QtGui.QApplication.translate("Form", "/Path/To/New Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_annDir.setText(QtGui.QApplication.translate("Form", "Annotated Bulk Extractor output directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_annDir.setPlaceholderText(QtGui.QApplication.translate("Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_xmlfile.setText(QtGui.QApplication.translate("Form", "Fiwalk XML file:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_xmlFile.setPlaceholderText(QtGui.QApplication.translate("Form", "/Path/to/File", None, QtGui.QApplication.UnicodeUTF8))
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

