# -*- coding: utf-8 -*-

# bc_reports_tab5.py
#
# Implementation of GUI interface in PyQT4 for generating various files and
# reports for Bitcurator project.
# Form implementation generated from reading ui file 'bc_reports_tab5.ui'
# Heavily modified manually
#
# Created: Sat Jul  6 20:33:35 2013
#      by: PyQt4 UI code generator 4.9.1
#

import os
from PyQt4 import QtCore, QtGui
from subprocess import Popen,PIPE
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

class Ui_bc_Form(object):
    imageFileName = "null"
    fwImageFileName = "null"
    beImageFileName = "null"
    xmlFileName = "null"
    fwXmlFileName = "null"
    TextFileName = "null"
    beDir = "null"
    annDir = "null" 
    bcpyDir = "null" 
    annBcpyDir = "null" 
    outputDirName = "null"
    beOutputDirName = "null"
    configFileName = "null"
    reportsDir = "null"
    annOutputDirName = "null"
    annBeFeatDir = "null"

    def setupUi(self, bc_Form):
        bc_Form.setObjectName(_fromUtf8("bc_Form"))
        bc_Form.resize(705, 723)
        self.tabWidget = QtGui.QTabWidget(bc_Form)
        self.tabWidget.setGeometry(QtCore.QRect(50, 60, 631, 641))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit_image = QtGui.QLineEdit(self.tab)
        self.lineEdit_image.setGeometry(QtCore.QRect(60, 60, 151, 21))
        self.lineEdit_image.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_image.setText(_fromUtf8(""))
        self.lineEdit_image.setObjectName(_fromUtf8("lineEdit_image"))
        self.toolButton_image = QtGui.QToolButton(self.tab)
        self.toolButton_image.setGeometry(QtCore.QRect(260, 60, 23, 25))
        self.toolButton_image.setObjectName(_fromUtf8("toolButton_image"))
        self.label_image = QtGui.QLabel(self.tab)
        self.label_image.setGeometry(QtCore.QRect(70, 40, 81, 21))
        self.label_image.setObjectName(_fromUtf8("label_image"))
        self.label_outdir = QtGui.QLabel(self.tab)
        self.label_outdir.setGeometry(QtCore.QRect(60, 150, 201, 17))
        self.label_outdir.setObjectName(_fromUtf8("label_outdir"))
        self.lineEdit_outdir = QtGui.QLineEdit(self.tab)
        self.lineEdit_outdir.setGeometry(QtCore.QRect(60, 170, 151, 21))
        self.lineEdit_outdir.setObjectName(_fromUtf8("lineEdit_outdir"))
        self.toolButton_outdir = QtGui.QToolButton(self.tab)
        self.toolButton_outdir.setGeometry(QtCore.QRect(260, 170, 23, 25))
        self.toolButton_outdir.setObjectName(_fromUtf8("toolButton_outdir"))
        self.label_config = QtGui.QLabel(self.tab)
        self.label_config.setGeometry(QtCore.QRect(60, 200, 151, 20))
        self.label_config.setObjectName(_fromUtf8("label_config"))
        self.lineEdit_confile = QtGui.QLineEdit(self.tab)
        self.lineEdit_confile.setGeometry(QtCore.QRect(60, 220, 151, 21))
        self.lineEdit_confile.setText(_fromUtf8(""))
        self.lineEdit_confile.setObjectName(_fromUtf8("lineEdit_confile"))
        self.toolButton_confile = QtGui.QToolButton(self.tab)
        self.toolButton_confile.setGeometry(QtCore.QRect(260, 220, 23, 25))
        self.toolButton_confile.setObjectName(_fromUtf8("toolButton_confile"))
        self.label_cmdlineoutput = QtGui.QLabel(self.tab)
        self.label_cmdlineoutput.setGeometry(QtCore.QRect(20, 280, 171, 17))
        self.label_cmdlineoutput.setObjectName(_fromUtf8("label_cmdlineoutput"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        #self.textEdit.setGeometry(QtCore.QRect(20, 300, 571, 211))
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 371, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        #self.buttonBox.setGeometry(QtCore.QRect(350, 520, 231, 31))
        self.buttonBox.setGeometry(QtCore.QRect(150, 450, 231, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_bcpydir = QtGui.QLabel(self.tab)
        self.label_bcpydir.setGeometry(QtCore.QRect(60, 100, 201, 21))
        self.label_bcpydir.setObjectName(_fromUtf8("label_bcpydir"))
        self.lineEdit_bcpydir = QtGui.QLineEdit(self.tab)
        self.lineEdit_bcpydir.setGeometry(QtCore.QRect(60, 120, 151, 21))
        self.lineEdit_bcpydir.setObjectName(_fromUtf8("lineEdit_bcpydir"))
        self.toolButton_bcpydir = QtGui.QToolButton(self.tab)
        self.toolButton_bcpydir.setGeometry(QtCore.QRect(260, 120, 23, 25))
        self.toolButton_bcpydir.setObjectName(_fromUtf8("toolButton_bcpydir"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        # Tab-2: Fiwalk XML Generation
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_fw_image = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_fw_image.setGeometry(QtCore.QRect(70, 90, 131, 21))
        self.lineEdit_fw_image.setText(_fromUtf8(""))
        self.lineEdit_fw_image.setObjectName(_fromUtf8("lineEdit_fw_image"))
        self.label_fw_image = QtGui.QLabel(self.tab_2)
        self.label_fw_image.setGeometry(QtCore.QRect(70, 60, 81, 31))
        self.label_fw_image.setObjectName(_fromUtf8("label_fw_image"))
        self.label_fw_xmlFile = QtGui.QLabel(self.tab_2)
        self.label_fw_xmlFile.setGeometry(QtCore.QRect(70, 140, 121, 21))
        self.label_fw_xmlFile.setObjectName(_fromUtf8("label_fw_xmlFile"))
        self.lineEdit_fw_xmlFile = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_fw_xmlFile.setGeometry(QtCore.QRect(70, 160, 131, 21))
        self.lineEdit_fw_xmlFile.setText(_fromUtf8(""))
        self.lineEdit_fw_xmlFile.setObjectName(_fromUtf8("lineEdit_fw_xmlFile"))
        self.toolButton_fw_image = QtGui.QToolButton(self.tab_2)
        self.toolButton_fw_image.setGeometry(QtCore.QRect(220, 90, 23, 25))
        self.toolButton_fw_image.setObjectName(_fromUtf8("toolButton_fw_image"))
        self.toolButton_fw_xmlFile = QtGui.QToolButton(self.tab_2)
        self.toolButton_fw_xmlFile.setGeometry(QtCore.QRect(220, 160, 23, 25))
        self.toolButton_fw_xmlFile.setObjectName(_fromUtf8("toolButton_fw_xmlFile"))
        # fw buttonBox (ok/close/cancel)
        self.buttonBox_fw = QtGui.QDialogButtonBox(self.tab_2)
        self.buttonBox_fw.setGeometry(QtCore.QRect(140, 330, 176, 27))
        self.buttonBox_fw.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_fw.setObjectName(_fromUtf8("buttonBox_fw"))

        # fw cmdline output box:
        self.textEdit_fw = QtGui.QTextEdit(self.tab_2)
        self.textEdit_fw.setGeometry(QtCore.QRect(70, 237, 271, 71))
        self.textEdit_fw.setObjectName(_fromUtf8("textEdit_fw"))
        self.label_fwcmdlineoutput = QtGui.QLabel(self.tab_2)
        self.label_fwcmdlineoutput.setGeometry(QtCore.QRect(70, 210, 161, 21))
        self.label_fwcmdlineoutput.setObjectName(_fromUtf8("label_fwcmdlineoutput"))
        # Now tab_2 is ready. Add it.
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        # Tab-3: Bulk Extractor command
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lineEdit_be_image = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_be_image.setGeometry(QtCore.QRect(70, 90, 131, 21))
        self.lineEdit_be_image.setText(_fromUtf8(""))
        self.lineEdit_be_image.setObjectName(_fromUtf8("lineEdit_be_image"))
        self.label_be_image = QtGui.QLabel(self.tab_3)
        self.label_be_image.setGeometry(QtCore.QRect(70, 60, 81, 31))
        self.label_be_image.setObjectName(_fromUtf8("label_be_image"))
        self.label_be_outDir = QtGui.QLabel(self.tab_3)
        self.label_be_outDir.setGeometry(QtCore.QRect(70, 140, 121, 21))
        self.label_be_outDir.setObjectName(_fromUtf8("label_be_outDir"))
        self.lineEdit_be_outDir = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_be_outDir.setGeometry(QtCore.QRect(70, 160, 131, 21))
        self.lineEdit_be_outDir.setText(_fromUtf8(""))
        self.lineEdit_be_outDir.setObjectName(_fromUtf8("lineEdit_be_outDir"))
        self.toolButton_be_image = QtGui.QToolButton(self.tab_3)
        self.toolButton_be_image.setGeometry(QtCore.QRect(220, 90, 23, 25))
        self.toolButton_be_image.setObjectName(_fromUtf8("toolButton_be_image"))
        self.toolButton_be_outDir = QtGui.QToolButton(self.tab_3)
        self.toolButton_be_outDir.setGeometry(QtCore.QRect(220, 160, 23, 25))
        self.toolButton_be_outDir.setObjectName(_fromUtf8("toolButton_be_outDir"))
        self.buttonBox_be = QtGui.QDialogButtonBox(self.tab_3)
        self.buttonBox_be.setGeometry(QtCore.QRect(160, 370, 176, 27))
        self.buttonBox_be.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_be.setObjectName(_fromUtf8("buttonBox_be"))
        self.textEdit_be = QtGui.QTextEdit(self.tab_3)
        self.textEdit_be.setGeometry(QtCore.QRect(70, 237, 261, 111))
        self.textEdit_be.setObjectName(_fromUtf8("textEdit_be"))
        self.label_becmdlineoutput = QtGui.QLabel(self.tab_3)
        self.label_becmdlineoutput.setGeometry(QtCore.QRect(70, 210, 161, 21))
        self.label_becmdlineoutput.setObjectName(_fromUtf8("label_becmdlineoutput"))
        # Tab 3 is ready. Add it.
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        # Tab - 4: Annotated Files directory
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.lineEdit_ann_image = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_ann_image.setGeometry(QtCore.QRect(70, 50, 131, 21))
        self.lineEdit_ann_image.setText(_fromUtf8(""))
        self.lineEdit_ann_image.setObjectName(_fromUtf8("lineEdit_ann_image"))
        self.label_ann_image = QtGui.QLabel(self.tab_4)
        self.label_ann_image.setGeometry(QtCore.QRect(70, 30, 81, 21))
        self.label_ann_image.setObjectName(_fromUtf8("label_ann_image"))
        self.label_ann_beFeatDir = QtGui.QLabel(self.tab_4)
        #self.label_ann_beFeatDir.setGeometry(QtCore.QRect(70, 90, 181, 21))
        self.label_ann_beFeatDir.setGeometry(QtCore.QRect(70, 90, 251, 21))
        self.label_ann_beFeatDir.setObjectName(_fromUtf8("label_ann_beFeatDir"))
        self.lineEdit_ann_beFeatDir = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_ann_beFeatDir.setGeometry(QtCore.QRect(70, 110, 121, 21))
        self.lineEdit_ann_beFeatDir.setText(_fromUtf8(""))
        self.lineEdit_ann_beFeatDir.setObjectName(_fromUtf8("lineEdit_ann_beFeatDir"))
        self.toolButton_ann_image = QtGui.QToolButton(self.tab_4)
        self.toolButton_ann_image.setGeometry(QtCore.QRect(220, 50, 23, 25))
        self.toolButton_ann_image.setObjectName(_fromUtf8("toolButton_ann_image"))
        self.toolButton_ann_beFeatDir = QtGui.QToolButton(self.tab_4)
        self.toolButton_ann_beFeatDir.setGeometry(QtCore.QRect(220, 110, 23, 25))
        self.toolButton_ann_beFeatDir.setObjectName(_fromUtf8("toolButton_ann_beFeatDir"))
        self.buttonBox_ann = QtGui.QDialogButtonBox(self.tab_4)
        self.buttonBox_ann.setGeometry(QtCore.QRect(160, 450, 176, 27))
        self.buttonBox_ann.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_ann.setObjectName(_fromUtf8("buttonBox_ann"))
        self.textEdit_ann = QtGui.QTextEdit(self.tab_4)
        self.textEdit_ann.setGeometry(QtCore.QRect(70, 310, 261, 111))
        self.textEdit_ann.setObjectName(_fromUtf8("textEdit_ann"))
        self.label_anncmdlineoutput = QtGui.QLabel(self.tab_4)
        self.label_anncmdlineoutput.setGeometry(QtCore.QRect(70, 290, 161, 21))
        self.label_anncmdlineoutput.setObjectName(_fromUtf8("label_anncmdlineoutput"))
        self.label_ann_annDir = QtGui.QLabel(self.tab_4)
        self.label_ann_annDir.setGeometry(QtCore.QRect(70, 151, 231, 20))
        self.label_ann_annDir.setObjectName(_fromUtf8("label_ann_annDir"))
        self.lineEdit_ann_annDir = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_ann_annDir.setGeometry(QtCore.QRect(70, 170, 113, 27))
        self.lineEdit_ann_annDir.setObjectName(_fromUtf8("lineEdit_ann_annDir"))
        self.toolButton_ann_annDir = QtGui.QToolButton(self.tab_4)
        self.toolButton_ann_annDir.setGeometry(QtCore.QRect(220, 170, 23, 25))
        self.toolButton_ann_annDir.setObjectName(_fromUtf8("toolButton_ann_annDir"))
        self.label_ann_bcpyDir = QtGui.QLabel(self.tab_4)
        self.label_ann_bcpyDir.setGeometry(QtCore.QRect(70, 220, 241, 21))
        self.label_ann_bcpyDir.setObjectName(_fromUtf8("label_ann_bcpyDir"))
        self.lineEdit_ann_bcpyDir = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_ann_bcpyDir.setGeometry(QtCore.QRect(70, 240, 113, 27))
        self.lineEdit_ann_bcpyDir.setObjectName(_fromUtf8("lineEdit_ann_bcpyDir"))
        self.toolButton_ann_bcpyDir = QtGui.QToolButton(self.tab_4)
        self.toolButton_ann_bcpyDir.setGeometry(QtCore.QRect(220, 240, 23, 25))
        self.toolButton_ann_bcpyDir.setObjectName(_fromUtf8("toolButton_ann_bcpyDir"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        # Common buttonBox: FIXME: May not be necessary. Remove
        ###self.buttonBox_Global = QtGui.QDialogButtonBox(bc_Form)
        ###self.buttonBox_Global.setGeometry(QtCore.QRect(440, 610, 176, 27))
        #self.buttonBox_Global.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        ###self.buttonBox_Global.setStandardButtons(QtGui.QDialogButtonBox.Close)
        ###self.buttonBox_Global.setObjectName(_fromUtf8("buttonBox_Global"))
        

        # The standard output from this point is placed by an in-memory 
        # buffer. 
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        # The common Cancel button quits the application
        ###QtCore.QObject.connect(self.buttonBox_Global, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        QtCore.QObject.connect(self.toolButton_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getImageFileName)

        QtCore.QObject.connect(self.toolButton_bcpydir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getbcpyDir)

        QtCore.QObject.connect(self.toolButton_outdir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputDir)

        QtCore.QObject.connect(self.toolButton_confile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getConfigFile)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkAllReports)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        # Tab-2: Fiwalk XML Generation
        
        QtCore.QObject.connect(self.toolButton_fw_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwImageFileName)

        QtCore.QObject.connect(self.toolButton_fw_xmlFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwOutputXmlFilePath)
        QtCore.QObject.connect(self.buttonBox_fw, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkFw)
        QtCore.QObject.connect(self.buttonBox_fw, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        ## 3rd Tab
        QtCore.QObject.connect(self.toolButton_be_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeImageFileName)

        QtCore.QObject.connect(self.toolButton_be_outDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeOutputDir)
        QtCore.QObject.connect(self.buttonBox_be, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkAnn)
        #QtCore.QObject.connect(self.buttonBox_be, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        ##self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        ## 4th Tab
        QtCore.QObject.connect(self.toolButton_ann_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnImageFileName)

        QtCore.QObject.connect(self.toolButton_ann_beFeatDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeFeatDir)
        QtCore.QObject.connect(self.toolButton_ann_annDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnOutputDir)
        QtCore.QObject.connect(self.toolButton_ann_bcpyDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnBcpyDir)
        QtCore.QObject.connect(self.buttonBox_ann, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkAnn)
        QtCore.QObject.connect(self.buttonBox_ann, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        ## 5th Tab
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))

        self.retranslateUi(bc_Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bc_Form)

    # buttonClickCancel: This called by any click that represents the
    # "Reject" role - Cancel and Close here. It just terminates the Gui.
    def buttonClickedCancel(self):
        QtCore.QCoreApplication.instance().quit()

    def getImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName()
        print(">> Image File Selected: ", image_file)

        self.lineEdit_image.setText(image_file)
        
        self.imageFileName = image_file

    def getFwImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName()
        print(">> Image File Selected: ", image_file)

        self.lineEdit_fw_image.setText(image_file)
        
        self.fwimageFileName = image_file

    def getBeImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName()
        print(">> Image File Selected: ", image_file)

        self.lineEdit_be_image.setText(image_file)
        
        self.beImageFileName = image_file

    def getAnnImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName()
        print(">> Image File Selected: ", image_file)

        self.lineEdit_ann_image.setText(image_file)
        
        self.annImageFileName = image_file

    def getbcpyDir(self):
        # Navigation
        bcpyDir = QtGui.QFileDialog.getExistingDirectory()
        print(">> BC Python Directory Selected: ", bcpyDir)

        self.lineEdit_bcpydir.setText(bcpyDir)
        
        self.bcpyDir = bcpyDir

    def getOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName()

        ## print(">> Output Directory Selected by navigating: ", outdir)
        print(">> Output Directory Selected for All Reports ", outdir)

        self.lineEdit_outdir.setText(outdir)
        self.outputDirName = outdir

        if os.path.exists(self.outputDirName):
            raise RuntimeError(out_dir+" exists")

            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout

            exit(1)

        os.mkdir(self.outputDirName)

    def getBeOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName()

        ## print(">> BE Output Directory Selected by navigating: ", outdir)
        print(">> BE Output Directory Selected for Bulk Extractor ", outdir)

        self.lineEdit_be_outDir.setText(outdir)
        self.beOutputDirName = outdir

        if os.path.exists(self.beOutputDirName):
            raise RuntimeError(outdir+" exists")

            self.textEdit_be.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout

            exit(1)

        os.mkdir(self.beOutputDirName)

    def getBeFeatDir(self):
        beFeatDir = QtGui.QFileDialog.getExistingDirectory()
        print(">> Annotate: BE Features Directory Selected: ", beFeatDir)

        self.lineEdit_ann_beFeatDir.setText(beFeatDir)
        
        self.annBeFeatDir = beFeatDir

    def getAnnOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        ann_outdir = QtGui.QFileDialog.getSaveFileName()

        ## print(">> Annotated files Directory Selected by navigating: ", ann_outdir)
        print(">> Output Directory Selected for Bulk Extractor ", ann_outdir)
        self.lineEdit_ann_annDir.setText(ann_outdir)
        self.annOutputDirName = ann_outdir

        if os.path.exists(self.annOutputDirName):
            raise RuntimeError(ann_outdir+" exists")

            self.textEdit_ann.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout

            exit(1)

        os.mkdir(self.annOutputDirName)
    def getAnnBcpyDir(self):
        # Navigation
        bcpyDir = QtGui.QFileDialog.getExistingDirectory()
        print(">> BC Python Directory Selected: ", bcpyDir)

        self.lineEdit_ann_bcpyDir.setText(bcpyDir)
        
        self.annBcpyDir = bcpyDir
    '''
    # getFiwalkXmlFileName: Routine to let the user choose the XML file -
    # by navigating trough the directories
    def getFiwalkXmlFileName(self):

        # Navigation
        xml_file = QtGui.QFileDialog.getOpenFileName()
        # print("D: Fiwalk XML File Selected: ", xml_file)

        self.lineEdit_xmlFile.setText(xml_file)

        self.fiwalkXmlFileName = xml_file
        return xml_file
    '''

    ###def getFwImageFileName(self):
        #### Navigation
        ###image_file = QtGui.QFileDialog.getOpenFileName()
        ###print(">> Image File Selected: ", image_file)

        ###self.lineEdit_fw_image.setText(image_file)
        
        ###self.fwimageFileName = image_file

    def getFwOutputXmlFilePath(self):
        # Navigation
        xml_output_file = QtGui.QFileDialog.getSaveFileName()
        ## print("D: Fiwalk XML File Selected: ", xml_output_file)

        self.lineEdit_fw_xmlFile.setText(xml_output_file)
        
        self.xmlFileName = xml_output_file
        self.TextFileName = xml_output_file + '.txt'


    # buttonClickedOkAllReports: Routine invoked when the OK button is clicked.
    # Using StringIO (equivalent to cStringIO in Python-2.x), the stdio is
    # redirected into an in-memory buffer, which is displayed in the 
    # text window at the end.
    def buttonClickedOkAllReports(self):
        # First create a directory for storing bulk-extractor files and
        # another for storing the annotated files.
        ## FIXME: Trying to imitate c/c++'s static local varaible
        ## buttonClickedOk.ctr += 1
        ## print("CTR = ", buttonClickedOk.ctr)
        
        self.beDir = self.outputDirName + '/beDir'
        if os.path.exists(self.beDir):
            raise RuntimeError(self.beDir+" exists")

            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            exit(1)

        os.mkdir(self.beDir)
        print(">> Created Bulk Extractor Directory: ", self.beDir)

        # Now create the Feature files using bulk-extractor
        cmd = ['bulk_extractor', self.imageFileName, '-o', self.beDir]

        print(">> Bulk_extractor running on image ", self.imageFileName)
        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
        if len(err) > 0:
            raise ValueError("Error in bulk-extractor (" + str(err).strip() + "): "+" ".join(cmd))
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            exit(1)
        else:
            print("\n>>  Success!!! Bulk-extractor created feature files in Directory ", self.beDir)

        # Now create the XML file using fiwalk
        self.xmlFileName = self.outputDirName + '/fiwalkXmlFile.xml'
        self.TextFileName = self.outputDirName + '/fiwalkXmlFile.txt'
        cmd = ['fiwalk', '-f', '-X', self.xmlFileName, '-T', self.TextFileName, self.imageFileName]
        print(">> Command Executed for Fiwalk = ", cmd)
        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()

        if len(err) > 0:
            print(">> ERROR!!! Fiwalk terminated with error: \n", err)
            #sys.stderr.write("Debug: type(err) = %r.\n" % type(err))
            # Terminate the redirecting of the stdout to the in-memory buffer.
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            raise ValueError("fiwalk error (" + str(err).strip() + "): "+" ".join(cmd))
            exit(1)
        else:
            print("\n>>  Success!!! Fiwalk created the following files: \n")
            print("    o ", self.xmlFileName)
            print("    o ", self.TextFileName)

        # Now create the directory for Annotated files and run the python
        # script identify_filenames to crate the annotated files in that directory.
        self.annDir = self.outputDirName + '/annDir'
        if os.path.exists(self.annDir):
            raise RuntimeError(self.annDir+" exists")
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            exit(1)

        os.mkdir(self.annDir)
        print("\n>> Directory for annotated files %s is created " %self.annDir)

        ## Now run the identify_filenames script from bcpyDir specified by
        ## the user.

        identify_cmd = self.bcpyDir + '/' + 'identify_filenames.py'
        cmd = ['python3',identify_cmd,'--all','--imagefile',\
          self.imageFileName, self.beDir, self.annDir]
        print("\n>> Running identify_filanames script : ", cmd)

        ###ret = self.bcRunCmd(cmd, err)
        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
        if len(err) > 0:
           print(">> ERROR!!! identify_filenames terminated with error: \n", err)
           self.textEdit.setText( sys.stdout.getvalue() )
           sys.stdout = self.oldstdout
           raise ValueError("fiwalk error (" + str(err).strip() + "): "+" ".join(cmd))
           exit(1)

        print("\n>>  Success!!! Annotated files created the directory: ", self.annDir)

        # To generate reports, create a 'reports' directory in outdir
        self.reportsDir = self.outputDirName + '/reportsDir'

        # Now Check the parameters and run the reports
        if self.bc_tab5_check_parameters() == -1:
            print(">> Report Generation is Aborted ")
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            exit (1)

        print("\n >> Generating Reports in directory ", self.reportsDir)
    
        # All fine. Generate the reports now.
        bc_get_reports(PdfReport, FiwalkReport, self.xmlFileName, \
                                 self.annDir, \
                                 self.reportsDir, \
                                 self.configFileName)

        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def buttonClickedOkFw(self):

        # The standard output from this point is placed by an in-memory 
        # buffer.
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        # If Image file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_fw_image.text() != self.fwImageFileName:
            self.fwImageFileName = ui.lineEdit_fw_image.text()
            ## print("D: Image File Selected from the box: ", self.imageFileName)

        # If output XML file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_fw_xmlFile.text() != self.fwXmlFileName:
            self.fwXmlFileName = ui.lineEdit_fw_xmlFile.text()
            self.fwTextFileName = self.fwXmlFileName + '.txt'
            ## print("D: XML File Selected from the box: ", self.xmlFileName)

        cmd = ['fiwalk', '-f', '-X', self.fwXmlFileName, '-T', self.fwTextFileName, self.imageFileName]
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
           print("    o ", self.fwXmlFileName)
           print("    o ", self.fwTextFileName)
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit_fw.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def buttonClickedOkBe(self):
        # The standard output from this point is placed by an in-memory 
        # buffer.
        ## FIXME: Redirecting the stdout seems to make the code hang
        ## here. So commenting it out for now. Need to be fixed.
        ## self.oldstdout = sys.stdout
        ## sys.stdout = StringIO()

        # If Image file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_be_image.text() != self.beImageFileName:
            self.beImageFileName = ui.lineEdit_be_image.text()
            print("D: Image File Selected from the box: ", self.beimageFileName)

        # If output Dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_be_outDir.text() != self.beOutputDirName:
            self.beOutputDirName = ui.lineEdit_be_outDir.text()
            print("D: Output Dir fir Bulk Extractor Selected from the box: ", self.beOutputDirName)

        cmd = ['bulk_extractor', self.beImageFileName, '-o', self.beOutputDirName]
        print(">> Command Executed for Bulk Extractor = ", cmd)

        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()

        if len(err) > 0 :
           #sys.stderr.write("Debug: type(err) = %r.\n" % type(err))
           # Terminate the redirecting of the stdout to the in-memory buffer.
           print(">> ERROR!!! Bulk_extractor terminated with error: \n", err)
           self.textEdit_be.setText( sys.stdout.getvalue() )
           sys.stdout = self.oldstdout
           raise ValueError("bulk_extractor error (" + str(err).strip() + "): "+" ".join(cmd))
        else:
           print("\n>>  Success!!! Bulk_extractor created the feature files in the Directory: ", self.beOutputDirName)
           print("\n")
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit_be.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def buttonClickedOkAnn(self):
        # If Image file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_image.text() != self.annImageFileName:
            self.annImageFileName = ui.lineEdit_ann_image.text()
            print("D: Image File Selected from the box: ", self.annimageFileName)

        # If beFeature Dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_beFeatDir.text() != self.annBeFeatDir:
            self.annBeFeatDir = ui.lineEdit_ann_beFeatDir.text()
            print("D: Output Dir fir Bulk Extractor Selected from the box: ", self.annBeFeatDir)

        # If annOutputDir Dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_annDir.text() != self.annOutputDirName:
            self.annOutputDirName = ui.lineEdit_ann_annDir.text()
            print("D: Ann Output Dir  Selected from the box: ", self.annOutputDirName)

        identify_cmd = self.annBcpyDir + '/' + 'identify_filenames.py'
        print("bcpyDir: ", self.annBcpyDir)
        cmd = ['python3',identify_cmd,'--all','--imagefile',\
          self.annImageFileName, self.annBeFeatDir, self.annOutputDirName]
        print("\n>> Running identify_filanames script : ", cmd)

        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
        if len(err) > 0:
            print(">> ERROR!!! identify_filenames terminated with error: \n", err)
            self.textEdit_ann.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            raise ValueError("identify_filenames error (" + str(err).strip() + "): "+" ".join(cmd))
            exit(1)

        print("\n>>  Success!!! Annotated files created in the directory: ", self.annOutputDirName)
        self.textEdit_ann.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def bcRunCmd(self, cmd, err):
        ## print("D: >> Executing Unix Cmd : ", cmd)

        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
        if len(err) > 0:
            ## print("\n>> [D] bcRunCmd: Failure!!! command executed: ", cmd)
            return (-1)
        else:
            ## print("\n>> [D] bcRunCmd: Success!!! command executed: ", cmd)
            return (0)

    # getConfigFile: Select the config file from the directory structure.
    def getConfigFile(self):
        config_file = QtGui.QFileDialog.getOpenFileName()
        ## print(">> [D] Config File Selected  navigating: ", config_file)
        print(">> Config File Selected: ", config_file)

        self.lineEdit_confile.setText(config_file)
        self.configFileName = config_file
        return config_file

    # bc_tab5_check_parameters: Check if the selected files exist. Also
    # if the text entered in the boxes doesn't match what was selected
    # by navigating through directory structure, use the text in the
    # box as the final selection.
    def bc_tab5_check_parameters(self):
        # If Image file not selected through menu, see if it is typed in the box:

        if ui.lineEdit_image.text() != self.imageFileName:
            self.imageFileName  = ui.lineEdit_image.text()
            # print("D:Image FIle Selected from the box: ", self.imageFileName)
        if not os.path.exists(self.imageFileName):
            print("Image File %s does not exist. Aborting" %self.imageFileName)
            return (-1)         

        # If Bitcurator Python dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_bcpydir.text() != self.bcpyDir:
            self.bcDir = ui.lineEdit_bcpydir.text()
            # print("D: BC Python Directory Selected from the box: ", self.bcpyDir)

        if not os.path.exists(self.bcpyDir):
            print("BC Python Directory %s does not exist. Aborting" %self.bcpyDir)
            return (-1)         

        # If Outdir is not selected through menu, see if it is typed 
        # in the text box: 
        if ui.lineEdit_outdir.text() != self.outputDirName:
            self.outputDirName = ui.lineEdit_outdir.text()
            # print("D: Output Directory selected from the box: ", self.outputDirName)
        # Check for outdir is already done earlier. So no need to do it here.

        if ui.lineEdit_confile.text() != self.configFileName:
            self.configFileName  = ui.lineEdit_configFile.text()
            # print("D: Config File selected from the box: ", self.configFileName)

        # If config file is not provided by the user, user the default one
        if not os.path.exists(self.configFileName):
            print(">> Using the default config file: /etc/bitcurator/bc_report_config.txt")
            self.configFileName = "/etc/bitcurator/bc_report_config.txt"

        return (0)


    def retranslateUi(self, bc_Form):
        bc_Form.setWindowTitle(QtGui.QApplication.translate("bc_Form", "Bitcurator Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("bc_Form", "Image File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_outdir.setText(QtGui.QApplication.translate("bc_Form", "Output directory for reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_outdir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_outdir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_config.setText(QtGui.QApplication.translate("bc_Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_confile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_confile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command line output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_bcpydir.setText(QtGui.QApplication.translate("bc_Form", "Bitcurator Python Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_bcpydir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_bcpydir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("bc_Form", "All Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("bc_Form", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("bc_Form", "Annotated Features", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("bc_Form", "Reports", None, QtGui.QApplication.UnicodeUTF8))
        
        # Tab-2: Fiwalk XML
        self.lineEdit_fw_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_xmlFile.setText(QtGui.QApplication.translate("bc_Form", "Output XML File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_fw_xmlFile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_fw_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_fw_xmlFile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("bc_Form", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))

        # Tab-3: Bulk Extractor
        self.lineEdit_be_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_be_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_be_outDir.setText(QtGui.QApplication.translate("bc_Form", "Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_be_outDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_be_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_be_outDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_becmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))
        
        # Tab-4: Annotated Files
        self.label_ann_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_beFeatDir.setText(QtGui.QApplication.translate("bc_Form", "Bulk Extractor Feature Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_annDir.setText(QtGui.QApplication.translate("bc_Form", "Annotated Files Directory(Output)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_bcpyDir.setText(QtGui.QApplication.translate("bc_Form", "Bulk Extractor Python Directory", None, QtGui.QApplication.UnicodeUTF8))

        self.lineEdit_ann_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_beFeatDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_annDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_bcpyDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))

        self.toolButton_ann_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_beFeatDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_annDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_bcpyDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.label_becmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    bc_Form = QtGui.QWidget()
    ui = Ui_bc_Form()
    ui.setupUi(bc_Form)
    bc_Form.show()
    sys.exit(app.exec_())

