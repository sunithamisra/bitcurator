# -*- coding: utf-8 -*-

# bc_reports_tab5.py
#
# Implementation of GUI interface in PyQT4 for generating various files and
# reports for Bitcurator project.
# Form implementation generated from reading ui file 'bc_reports_tab7*.ui'
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
    repFwXmlFileName = "null"
    repOutDir = "null"
    repConfile = "null"
    repAnnDir = "null"

    def setupUi(self, bc_Form):
        # Set the directory to user's home directory
        os.chdir(os.environ["HOME"])

        bc_Form.setObjectName(_fromUtf8("bc_Form"))
        #bc_Form.resize(512, 605)
        bc_Form.resize(512, 630)
        self.tabWidget = QtGui.QTabWidget(bc_Form)
        #self.tabWidget.setGeometry(QtCore.QRect(30, 10, 481, 581))
        #self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 561))
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 581))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))


        # Tab-2: Fiwalk XML Generation

        # fw input Image File
        self.tab_fw = QtGui.QWidget()
        self.tab_fw.setObjectName(_fromUtf8("tab_fw"))
        
        self.label_fw_image = QtGui.QLabel(self.tab_fw)
        self.label_fw_image.setGeometry(QtCore.QRect(20, 100, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fw_image.setFont(font)
        self.label_fw_image.setObjectName(_fromUtf8("label_fw_image"))
        self.lineEdit_fw_image = QtGui.QLineEdit(self.tab_fw)
        self.lineEdit_fw_image.setGeometry(QtCore.QRect(20, 121, 381, 20))
        self.lineEdit_fw_image.setObjectName(_fromUtf8("lineEdit_fw_image"))
        self.toolButton_fw_image = QtGui.QToolButton(self.tab_fw)
        self.toolButton_fw_image.setGeometry(QtCore.QRect(410, 120, 23, 25))
        self.toolButton_fw_image.setObjectName(_fromUtf8("toolButton_fw_image"))
        self.label_fwhdr = QtGui.QLabel(self.tab_fw)
        self.label_fwhdr.setGeometry(QtCore.QRect(10, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fwhdr.setFont(font)
        self.label_fwhdr.setWordWrap(True)
        self.label_fwhdr.setObjectName(_fromUtf8("label"))
        
        # fw output XML File
        self.label_fw_xmlFile = QtGui.QLabel(self.tab_fw)
        self.label_fw_xmlFile.setGeometry(QtCore.QRect(20, 176, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fw_xmlFile.setFont(font)
        self.label_fw_xmlFile.setObjectName(_fromUtf8("label_fw_xmlFile"))
        self.lineEdit_fw_xmlFile = QtGui.QLineEdit(self.tab_fw)
        self.lineEdit_fw_xmlFile.setGeometry(QtCore.QRect(20, 199, 381, 21))
        self.lineEdit_fw_xmlFile.setObjectName(_fromUtf8("lineEdit_fw_xmlFile"))
        self.toolButton_fw_xmlFile = QtGui.QToolButton(self.tab_fw)
        self.toolButton_fw_xmlFile.setGeometry(QtCore.QRect(410, 200, 23, 25))
        self.toolButton_fw_xmlFile.setObjectName(_fromUtf8("toolButton_fw_xmlFile"))
        # fw cmdline output box:
        self.label_fwcmdlineoutput = QtGui.QLabel(self.tab_fw)
        self.label_fwcmdlineoutput.setGeometry(QtCore.QRect(20, 260, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fwcmdlineoutput.setFont(font)
        self.label_fwcmdlineoutput.setObjectName(_fromUtf8("label_fwcmdlineoutput"))
        self.textEdit_fwcmdlineoutput = QtGui.QTextEdit(self.tab_fw)
        self.textEdit_fwcmdlineoutput.setGeometry(QtCore.QRect(20, 280, 411, 161))
        self.textEdit_fwcmdlineoutput.setObjectName(_fromUtf8("textEdit_fwcmdlineoutput"))
        
        # fw buttonBox (ok/close/cancel)
        self.buttonBox_fw = QtGui.QDialogButtonBox(self.tab_fw)
        self.buttonBox_fw.setGeometry(QtCore.QRect(200, 450, 231, 31))
        self.buttonBox_fw.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_fw.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_fw.setObjectName(_fromUtf8("buttonBox_fw"))
        
        # Now tab_fw is ready. Add it.
        self.tabWidget.addTab(self.tab_fw, _fromUtf8(""))

        # Tab-3: Bulk Extractor command

        self.tab_be = QtGui.QWidget()
        self.tab_be.setObjectName(_fromUtf8("tab_be"))

        # be: output Directory
        self.label_be_outDir = QtGui.QLabel(self.tab_be)
        self.label_be_outDir.setGeometry(QtCore.QRect(20, 176, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_be_outDir.setFont(font)
        self.label_be_outDir.setObjectName(_fromUtf8("label_be_outDir"))
        self.lineEdit_be_outDir = QtGui.QLineEdit(self.tab_be)
        self.lineEdit_be_outDir.setGeometry(QtCore.QRect(20, 199, 381, 21))
        self.lineEdit_be_outDir.setObjectName(_fromUtf8("lineEdit_be_outDir"))
        self.toolButton_be_outDir = QtGui.QToolButton(self.tab_be)
        self.toolButton_be_outDir.setGeometry(QtCore.QRect(410, 200, 23, 25))
        self.toolButton_be_outDir.setObjectName(_fromUtf8("toolButton_be_outDir"))

        # be: cmd line output window
        self.label_becmdlineoutput = QtGui.QLabel(self.tab_be)
        self.label_becmdlineoutput.setGeometry(QtCore.QRect(20, 260, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_becmdlineoutput.setFont(font)
        self.label_becmdlineoutput.setObjectName(_fromUtf8("label_becmdlineoutput"))
        self.textEdit_becmdlineoutput = QtGui.QTextEdit(self.tab_be)
        self.textEdit_becmdlineoutput.setGeometry(QtCore.QRect(20, 280, 411, 161))
        self.textEdit_becmdlineoutput.setObjectName(_fromUtf8("textEdit_becmdlineoutput"))

        # be: click button ok/cancel/close
        self.buttonBox_be = QtGui.QDialogButtonBox(self.tab_be)
        self.buttonBox_be.setGeometry(QtCore.QRect(200, 450, 231, 31))
        self.buttonBox_be.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_be.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_be.setObjectName(_fromUtf8("buttonBox_be"))

        # be: image file name
        self.label_be_image = QtGui.QLabel(self.tab_be)
        self.label_be_image.setGeometry(QtCore.QRect(20, 100, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_be_image.setFont(font)
        self.label_be_image.setObjectName(_fromUtf8("label_be_image"))
        self.lineEdit_be_image = QtGui.QLineEdit(self.tab_be)
        self.lineEdit_be_image.setGeometry(QtCore.QRect(20, 121, 381, 20))
        self.lineEdit_be_image.setObjectName(_fromUtf8("lineEdit_be_image"))
        self.toolButton_be_image = QtGui.QToolButton(self.tab_be)
        self.toolButton_be_image.setGeometry(QtCore.QRect(410, 120, 23, 25))
        self.toolButton_be_image.setObjectName(_fromUtf8("toolButton_be_image"))
        self.label_behdr = QtGui.QLabel(self.tab_be)
        self.label_behdr.setGeometry(QtCore.QRect(20, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_behdr.setFont(font)
        self.label_behdr.setWordWrap(True)
        self.label_behdr.setObjectName(_fromUtf8("label_behdr"))

        # Add the tab now
        # NOTE: Bulk Extractor ta bis commented out for now.
        ## self.tabWidget.addTab(self.tab_be, _fromUtf8(""))
        

        # Tab - ann: Annotated Files directory
        self.tab_ann = QtGui.QWidget()
        self.tab_ann.setObjectName(_fromUtf8("tab_ann"))
        self.lineEdit_ann_image = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_image.setGeometry(QtCore.QRect(20, 100, 361, 21))
        self.lineEdit_ann_image.setText(_fromUtf8(""))
        self.lineEdit_ann_image.setObjectName(_fromUtf8("lineEdit_ann_image"))
        self.label_ann_image = QtGui.QLabel(self.tab_ann)
        self.label_ann_image.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_image.setFont(font)
        self.label_ann_image.setObjectName(_fromUtf8("label_ann_image"))
        self.label_ann_beFeatDir = QtGui.QLabel(self.tab_ann)
        self.label_ann_beFeatDir.setGeometry(QtCore.QRect(20, 150, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_beFeatDir.setFont(font)
        self.label_ann_beFeatDir.setObjectName(_fromUtf8("label_ann_beFeatDir"))
        self.lineEdit_ann_beFeatDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_beFeatDir.setGeometry(QtCore.QRect(20, 170, 361, 21))
        self.lineEdit_ann_beFeatDir.setText(_fromUtf8(""))
        self.lineEdit_ann_beFeatDir.setObjectName(_fromUtf8("lineEdit_ann_beFeatDir"))
        self.toolButton_ann_image = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_image.setGeometry(QtCore.QRect(410, 100, 23, 25))
        self.toolButton_ann_image.setObjectName(_fromUtf8("toolButton_ann_image"))
        self.toolButton_ann_beFeatDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_beFeatDir.setGeometry(QtCore.QRect(410, 170, 23, 25))
        self.toolButton_ann_beFeatDir.setObjectName(_fromUtf8("toolButton_ann_beFeatDir"))
        self.buttonBox_ann = QtGui.QDialogButtonBox(self.tab_ann)
        self.buttonBox_ann.setGeometry(QtCore.QRect(260, 510, 176, 27))
        self.buttonBox_ann.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_ann.setObjectName(_fromUtf8("buttonBox_ann"))
        self.textEdit_ann = QtGui.QTextEdit(self.tab_ann)
        self.textEdit_ann.setGeometry(QtCore.QRect(20, 360, 421, 131))
        self.textEdit_ann.setObjectName(_fromUtf8("textEdit_ann"))
        self.label_anncmdlineoutput = QtGui.QLabel(self.tab_ann)
        self.label_anncmdlineoutput.setGeometry(QtCore.QRect(20, 340, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_anncmdlineoutput.setFont(font)
        self.label_anncmdlineoutput.setObjectName(_fromUtf8("label_anncmdlineoutput"))
        self.label_ann_annDir = QtGui.QLabel(self.tab_ann)
        self.label_ann_annDir.setGeometry(QtCore.QRect(20, 220, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_annDir.setFont(font)
        self.label_ann_annDir.setObjectName(_fromUtf8("label_ann_annDir"))
        self.lineEdit_ann_annDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_annDir.setGeometry(QtCore.QRect(20, 237, 361, 20))
        self.lineEdit_ann_annDir.setObjectName(_fromUtf8("lineEdit_ann_annDir"))
        self.toolButton_ann_annDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_annDir.setGeometry(QtCore.QRect(410, 240, 23, 25))
        self.toolButton_ann_annDir.setObjectName(_fromUtf8("toolButton_ann_annDir"))
        self.label_ann_bcpyDir = QtGui.QLabel(self.tab_ann)
        self.label_ann_bcpyDir.setGeometry(QtCore.QRect(20, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_bcpyDir.setFont(font)
        self.label_ann_bcpyDir.setObjectName(_fromUtf8("label_ann_bcpyDir"))
        self.lineEdit_ann_bcpyDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_bcpyDir.setGeometry(QtCore.QRect(20, 310, 361, 21))
        self.lineEdit_ann_bcpyDir.setObjectName(_fromUtf8("lineEdit_ann_bcpyDir"))
        self.toolButton_ann_bcpyDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_bcpyDir.setGeometry(QtCore.QRect(410, 310, 23, 25))
        self.toolButton_ann_bcpyDir.setObjectName(_fromUtf8("toolButton_ann_bcpyDir"))
        self.label_annhdr = QtGui.QLabel(self.tab_ann)
        self.label_annhdr.setGeometry(QtCore.QRect(20, 10, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_annhdr.setFont(font)
        self.label_annhdr.setAutoFillBackground(True)
        self.label_annhdr.setWordWrap(True)
        self.label_annhdr.setObjectName(_fromUtf8("label_ann"))
        self.tabWidget.addTab(self.tab_ann, _fromUtf8(""))

        # First tab: Reports
        self.tab_rep = QtGui.QWidget()
        self.tab_rep.setObjectName(_fromUtf8("tab_rep"))
        self.lineEdit_rep_fwxmlfile = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_fwxmlfile.setGeometry(QtCore.QRect(20, 59, 351, 21))
        self.lineEdit_rep_fwxmlfile.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_rep_fwxmlfile.setText(_fromUtf8(""))
        self.lineEdit_rep_fwxmlfile.setObjectName(_fromUtf8("lineEdit_rep_fwxmlfile"))
        self.toolButton_rep_fwxmlfile = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_fwxmlfile.setGeometry(QtCore.QRect(400, 60, 23, 25))
        self.toolButton_rep_fwxmlfile.setObjectName(_fromUtf8("toolButton_rep_fwxmlfile"))
        self.label_rep_fwxmlfile = QtGui.QLabel(self.tab_rep)
        self.label_rep_fwxmlfile.setGeometry(QtCore.QRect(20, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_fwxmlfile.setFont(font)
        self.label_rep_fwxmlfile.setObjectName(_fromUtf8("label_rep_fwxmlfile"))
        self.label_rep_outdir = QtGui.QLabel(self.tab_rep)
        self.label_rep_outdir.setGeometry(QtCore.QRect(20, 160, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_outdir.setFont(font)
        self.label_rep_outdir.setObjectName(_fromUtf8("label_rep_outdir"))
        self.lineEdit_rep_outdir = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_outdir.setGeometry(QtCore.QRect(20, 180, 351, 21))
        self.lineEdit_rep_outdir.setObjectName(_fromUtf8("lineEdit_rep_outdir"))
        self.toolButton_rep_outdir = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_outdir.setGeometry(QtCore.QRect(400, 180, 23, 25))
        self.toolButton_rep_outdir.setObjectName(_fromUtf8("toolButton_rep_outdir"))
        self.label_rep_config = QtGui.QLabel(self.tab_rep)
        self.label_rep_config.setGeometry(QtCore.QRect(20, 220, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_config.setFont(font)
        self.label_rep_config.setObjectName(_fromUtf8("label_rep_config"))
        self.lineEdit_rep_confile = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_confile.setGeometry(QtCore.QRect(20, 240, 351, 21))
        self.lineEdit_rep_confile.setText(_fromUtf8(""))
        self.lineEdit_rep_confile.setObjectName(_fromUtf8("lineEdit_rep_confile"))
        self.toolButton_rep_confile = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_confile.setGeometry(QtCore.QRect(400, 240, 23, 25))
        self.toolButton_rep_confile.setObjectName(_fromUtf8("toolButton_rep_confile"))
        self.label_rep_cmdlineoutput = QtGui.QLabel(self.tab_rep)
        self.label_rep_cmdlineoutput.setGeometry(QtCore.QRect(20, 280, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_cmdlineoutput.setFont(font)
        self.label_rep_cmdlineoutput.setObjectName(_fromUtf8("label_rep_cmdlineoutput"))
        self.textEdit_rep = QtGui.QTextEdit(self.tab_rep)
        self.textEdit_rep.setGeometry(QtCore.QRect(20, 300, 401, 161))
        self.textEdit_rep.setObjectName(_fromUtf8("textEdit_rep"))
        self.buttonBox_rep = QtGui.QDialogButtonBox(self.tab_rep)
        self.buttonBox_rep.setGeometry(QtCore.QRect(190, 470, 231, 31))
        self.buttonBox_rep.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_rep.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox_rep.setObjectName(_fromUtf8("buttonBox_rep"))
        self.label_rep_annDir = QtGui.QLabel(self.tab_rep)
        self.label_rep_annDir.setGeometry(QtCore.QRect(20, 100, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_annDir.setFont(font)
        self.label_rep_annDir.setObjectName(_fromUtf8("label_rep_annDir"))
        self.lineEdit_rep_annDir = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_annDir.setGeometry(QtCore.QRect(20, 120, 351, 20))
        self.lineEdit_rep_annDir.setObjectName(_fromUtf8("lineEdit_rep_annDir"))
        self.toolButton_rep_annDir = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_annDir.setGeometry(QtCore.QRect(400, 120, 23, 25))
        self.toolButton_rep_annDir.setObjectName(_fromUtf8("toolButton_rep_annDir"))
        self.label_rephdr = QtGui.QLabel(self.tab_rep)
        self.label_rephdr.setGeometry(QtCore.QRect(20, 10, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_rephdr.setFont(font)
        self.label_rephdr.setWordWrap(True)
        self.label_rephdr.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab_rep, _fromUtf8(""))

        ## Tab for All Reports (NOTE: To be hidden)

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

        # NOTE: All reports tab is commented out for now.
        ## self.tabWidget.addTab(self.tab, _fromUtf8(""))

        # File navigation through toolButton:

        # The standard output from this point is placed by an in-memory 
        # buffer. 
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        ## File navigation for All Reports
        QtCore.QObject.connect(self.toolButton_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getImageFileName)

        QtCore.QObject.connect(self.toolButton_bcpydir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getbcpyDir)

        QtCore.QObject.connect(self.toolButton_outdir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputDir)

        QtCore.QObject.connect(self.toolButton_confile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getConfigFile)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkAllReports)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        # File navigation for Fiwalk XML Generation tab
        
        QtCore.QObject.connect(self.toolButton_fw_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwImageFileName)

        QtCore.QObject.connect(self.toolButton_fw_xmlFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwOutputXmlFilePath)
        QtCore.QObject.connect(self.buttonBox_fw, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkFw)
        QtCore.QObject.connect(self.buttonBox_fw, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        # File navigation for BE 
        QtCore.QObject.connect(self.toolButton_be_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeImageFileName)

        QtCore.QObject.connect(self.toolButton_be_outDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeOutputDir)
        QtCore.QObject.connect(self.buttonBox_be, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkBe)
        QtCore.QObject.connect(self.buttonBox_be, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        #  File navigation for Annotated files Tab
        QtCore.QObject.connect(self.toolButton_ann_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnImageFileName)

        QtCore.QObject.connect(self.toolButton_ann_beFeatDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeFeatDir)
        QtCore.QObject.connect(self.toolButton_ann_annDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnOutputDir)
        QtCore.QObject.connect(self.toolButton_ann_bcpyDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnBcpyDir)
        QtCore.QObject.connect(self.buttonBox_ann, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkAnn)
        QtCore.QObject.connect(self.buttonBox_ann, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

        # File navigation for Reports Tab
        QtCore.QObject.connect(self.toolButton_rep_fwxmlfile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepFwXmlFileName)
        QtCore.QObject.connect(self.toolButton_rep_outdir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepOutputDir)
        QtCore.QObject.connect(self.toolButton_rep_confile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepConfigFile)
        QtCore.QObject.connect(self.toolButton_rep_annDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepBeAnnotatedDir)

        QtCore.QObject.connect(self.buttonBox_rep, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOkRep)
        QtCore.QObject.connect(self.buttonBox_rep, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)

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

    ##'''
    ## All reports
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
    ##'''

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

            self.textEdit_becmdlineoutput.setText( sys.stdout.getvalue() )
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

    def getFwOutputXmlFilePath(self):
        # Navigation
        xml_output_file = QtGui.QFileDialog.getSaveFileName()
        ## print("D: Fiwalk XML File Selected: ", xml_output_file)

        self.lineEdit_fw_xmlFile.setText(xml_output_file)
        
        self.xmlFileName = xml_output_file
        self.TextFileName = xml_output_file + '.txt'

    # get: Routine to let the user choose the XML file -
    # by navigating trough the directories
    def getRepFwXmlFileName(self):
        # Navigation
        xml_file = QtGui.QFileDialog.getOpenFileName()
        # print("D: Fiwalk XML File Selected: ", xml_file)

        self.lineEdit_rep_fwxmlfile.setText(xml_file)

        self.repFwXmlFileName = xml_file
        return xml_file
    
    # getRepBeAnnotatedDir: Routine to let the user choose the Directory name 
    # containing the annotated files by navigating 
    def getRepBeAnnotatedDir(self):
        ann_dir = QtGui.QFileDialog.getExistingDirectory()
        # print("D: Annotated Directory Selected by navigating: ", ann_dir)

        self.lineEdit_rep_annDir.setText(ann_dir)
        self.repAnnDir = ann_dir
        return ann_dir

    # getOutputDir: Routine to let the user choose the Directory name 
    # to output the reports by navigating 
    def getRepOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName()

        # print("D: Output Directory Selected by navigating: ", outdir)

        self.lineEdit_rep_outdir.setText(outdir)
        self.repOutDir = outdir
        return outdir

    # getConfigFile: Select the config file from the directory structure.
    def getRepConfigFile(self):
        config_file = QtGui.QFileDialog.getOpenFileName()
        # print("D: Config File Selected by navigating: ", config_file)

        self.lineEdit_rep_confile.setText(config_file)
        self.repConfile = config_file
        return config_file
    

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
        if self.bc_allrep_check_parameters() == -1:
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

        cmd = ['fiwalk', '-f', '-X', self.fwXmlFileName, '-T', self.fwTextFileName, self.fwImageFileName]
        print(">> Command Executed for Fiwalk = ", cmd)

        (data, err) = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()

        if len(err) > 0 :
           #sys.stderr.write("Debug: type(err) = %r.\n" % type(err))
           # Terminate the redirecting of the stdout to the in-memory buffer.
           print(">> ERROR!!! Fiwalk terminated with error: \n", err)
           self.textEdit_fwcmdlineoutput.setText( sys.stdout.getvalue() )
           sys.stdout = self.oldstdout
           raise ValueError("fiwalk error (" + str(err).strip() + "): "+" ".join(cmd))
        else:
           print("\n>>  Success!!! Fiwalk crated the following files: \n")
           print("    o ", self.fwXmlFileName)
           print("    o ", self.fwTextFileName)
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        #self.textEdit_fw.setText( sys.stdout.getvalue() )
        self.textEdit_fwcmdlineoutput.setText( sys.stdout.getvalue() )
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
            # print("D: Image File Selected from the box: ", self.beimageFileName)

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
           self.textEdit_becmdlineoutput.setText( sys.stdout.getvalue() )
           sys.stdout = self.oldstdout
           raise ValueError("bulk_extractor error (" + str(err).strip() + "): "+" ".join(cmd))
        else:
           print("\n>>  Success!!! Bulk_extractor created the feature files in the Directory: ", self.beOutputDirName)
           print("\n")
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit_becmdlineoutput.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def buttonClickedOkAnn(self):
        # If Image file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_image.text() != self.annImageFileName:
            self.annImageFileName = ui.lineEdit_ann_image.text()
            # print("D: Image File Selected from the box: ", self.annimageFileName)

        # If beFeature Dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_beFeatDir.text() != self.annBeFeatDir:
            self.annBeFeatDir = ui.lineEdit_ann_beFeatDir.text()
            # print("D: Output Dir fir Bulk Extractor Selected from the box: ", self.annBeFeatDir)

        # If annOutputDir Dir is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_ann_annDir.text() != self.annOutputDirName:
            self.annOutputDirName = ui.lineEdit_ann_annDir.text()
            # print("D: Ann Output Dir  Selected from the box: ", self.annOutputDirName)

        # If bcpyDir doesn't exist, default it to 
        # /home/bcadmin/Tools/bulk_extractor/python

        if not os.path.exists(self.annBcpyDir):
            # print("D: Setting default directory for BC python directory") 
            self.annBcpyDir = "/home/bcadmin/Tools/bulk_extractor/python"

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

    def buttonClickedOkRep(self):
        use_config_file = True

        ### FIXME: self.setEnabled(False)
        # The standard output from this point is placed by an in-memory 
        # buffer.
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        # Check if the indicated files exist. If not, return after 
        # printing the error. Also terminate the redirecting of the 
        # stdout to the in-memory buffer.
        if self.bc_rep_check_parameters() == -1:
            print(">> Report Generation is Aborted ")
            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            return

        # All fine. Generate the reports now.
        bc_get_reports(PdfReport, FiwalkReport, self.repFwXmlFileName, \
                                 self.repAnnDir, \
                                 self.repOutDir, \
                                 self.repConfile)

        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit_rep.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

        # We will not quit from the Gui window until the user clicks
        # on Close.
        # QtCore.QCoreApplication.instance().quit()

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

    def bc_rep_check_parameters(self):
        # If XML file not selected through menu, see if it is typed in the box:

        if ui.lineEdit_rep_fwxmlfile.text() != self.repFwXmlFileName:
            self.repFwXmlFileName  = ui.lineEdit_rep_fwxmlfile.text()
            # print("D:Fiwalk XML FIle Selected from the box: ", self.repFwXmlFileName)
        if not os.path.exists(self.repFwXmlFileName):
            print("XML File %s does not exist. Aborting" %self.repFwXmlFileName)
            return (-1)

        # If Annotated file is not selected through menu, see if it is
        # typed in the text box: 
        if ui.lineEdit_rep_annDir.text() != self.repAnnDir:
            self.repAnnDir = ui.lineEdit_rep_annDir.text()
            # print("D: Annotated Directory Selected from the box: ", self.repAnnDir)

        if not os.path.exists(self.repAnnDir):
            print("BE Annotated Directory %s does not exist. Aborting" %self.repAnnDir)
            return (-1)

        # If Outdir is not selected through menu, see if it is typed 
        # in the text box: 
        if ui.lineEdit_rep_outdir.text() != self.repOutDir:
            self.repOutDir = ui.lineEdit_rep_outdir.text()
            # print("D: Output Directory selected from the box: ", self.repOutDir)
        # The directory is not supposed to exist. Return -1 if it does. 
        if (os.path.exists(self.repOutDir)):
            print(">> Error: Output Directory %s exists. " %self.repOutDir)
            return (-1)

        if ui.lineEdit_rep_confile.text() != self.repConfile:
            self.repConfile  = ui.lineEdit_rep_confile.text()
            # print("D: Config File selected from the box: ", self.repConfile)

        # If config file is not provided by the user, user the default one
        if not os.path.exists(self.repConfile):
            print(">> Using the default config file: /etc/bitcurator/bc_report_config.txt")
            self.configFileName = "/etc/bitcurator/bc_report_config.txt"

        return (0)
    

    # bc_allrep_check_parameters: Check if the selected files exist. Also
    # if the text entered in the boxes doesn't match what was selected
    # by navigating through directory structure, use the text in the
    # box as the final selection.
    def bc_allrep_check_parameters(self):
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
        ###'''
        self.lineEdit_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        #self.tn.translate("bc_Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("bc_Form", "Image File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_outdir.setText(QtGui.QApplication.translate("bc_Form", "Output Directory For Reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_outdir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_outdir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        ###self.label_config.setText(QtGui.QApplicatiotoolButton_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getImageFileName)
        self.label_config.setText(QtGui.QApplication.translate("bc_Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))


        self.lineEdit_confile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_confile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command line output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_bcpydir.setText(QtGui.QApplication.translate("bc_Form", "Bitcurator Python Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_bcpydir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_bcpydir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("bc_Form", "All Reports", None, QtGui.QApplication.UnicodeUTF8))
        ###'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fw), QtGui.QApplication.translate("bc_Form", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ann), QtGui.QApplication.translate("bc_Form", "Annotated Features", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_be), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rep), QtGui.QApplication.translate("bc_Form", "Reports", None, QtGui.QApplication.UnicodeUTF8))

        # Tab-1: Reports
        self.lineEdit_rep_fwxmlfile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_fwxmlfile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_fwxmlfile.setText(QtGui.QApplication.translate("bc_Form", "Fiwalk XML File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_outdir.setText(QtGui.QApplication.translate("bc_Form", "Output Directory For Reports:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_outdir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_outdir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_config.setText(QtGui.QApplication.translate("bc_Form", "Config File (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_confile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_confile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_cmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_annDir.setText(QtGui.QApplication.translate("bc_Form", "Annotated Bulk Extractor Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_annDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_annDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rephdr.setText(QtGui.QApplication.translate("bc_Form", "Produces Office Open XML and PDF reports to assist in image analysis", None, QtGui.QApplication.UnicodeUTF8))
        
        # Tab-2: Fiwalk XML
        self.lineEdit_fw_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_xmlFile.setText(QtGui.QApplication.translate("bc_Form", "Output XML File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_fw_xmlFile.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_fw_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_fw_xmlFile.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fw), QtGui.QApplication.translate("bc_Form", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fwhdr.setText(QtGui.QApplication.translate("bc_Form", "Fiwalk produces a DFXML file showing the volumes, directories, and files contained within a disk image.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fwcmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output:", None, QtGui.QApplication.UnicodeUTF8))

        # Tab-3: Bulk Extractor
        self.lineEdit_be_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_be_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_be_outDir.setText(QtGui.QApplication.translate("bc_Form", "Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_be_outDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_be_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.label_behdr.setText(QtGui.QApplication.translate("bc_Form", "Bulk extractor identifies features of interest within a disk image. This interface uses only the default settings; for customized extractions, please use the Bulk Extractor Viewer.", None, QtGui.QApplication.UnicodeUTF8))
                

        self.toolButton_be_outDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_becmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_be), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))
        
        # Tab-4: Annotated Files
        self.label_ann_image.setText(QtGui.QApplication.translate("bc_Form", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_beFeatDir.setText(QtGui.QApplication.translate("bc_Form", "Bulk Extractor Feature Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_annDir.setText(QtGui.QApplication.translate("bc_Form", "Annotated Files Directory (Output)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_bcpyDir.setText(QtGui.QApplication.translate("bc_Form", "Bulk Extractor Python Directory", None, QtGui.QApplication.UnicodeUTF8))

        self.lineEdit_ann_image.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_beFeatDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_annDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_bcpyDir.setPlaceholderText(QtGui.QApplication.translate("bc_Form", "/home/bcadmin/Tools/bulk_extractor/python", None, QtGui.QApplication.UnicodeUTF8))

        self.toolButton_ann_image.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_beFeatDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_annDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_bcpyDir.setText(QtGui.QApplication.translate("bc_Form", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.label_anncmdlineoutput.setText(QtGui.QApplication.translate("bc_Form", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_be), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_annhdr.setText(QtGui.QApplication.translate("bc_Form", "Produces reports that identify which bulk extractor features are contained within files in a disk image.", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    bc_Form = QtGui.QWidget()
    ui = Ui_bc_Form()
    ui.setupUi(bc_Form)
    bc_Form.show()
    sys.exit(app.exec_())

