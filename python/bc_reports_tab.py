#!/usr/bin/python3
# -*- coding: utf-8 -*-

# bc_reports_tab5.py
#
# Implementation of GUI interface in PyQT4 for generating various files and
# reports for Bitcurator project.
# Form implementation generated from reading ui file 'bc_reports_tab7*.ui'
# Heavily modified manually
#
# Created: Sat Jul 6 20:33:35 2013
# by: PyQt4 UI code generator 4.9.1
#

import os
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from subprocess import Popen,PIPE
import sys, time
import threading

from generate_report import *
from bc_utils import *
#from PyQt4.Qsci import *

try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# The following global variables are used as they are used in the
# threads which access attributes defined in other classes. In Python this
# seems to be the only simple solution for a case like this where the 
# GUI attributes are initialized only once by the main routine.
global_fw = "null"
g_textEdit_fwcmdlineoutput = "null"
g_xmlFwFilename = "null"
global_ann = "null"
g_textEdit_anncmdlineoutput = "null"


class Ui_MainWindow(object):
    #def __init__(self, parent=None):
        #self.setupUi(MainWindow)

    imageFileName = "null"
    fwImageFileName = "null"
    beImageFileName = "null"
    annImageFileName = "null"
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
    progressBar_fw = "null"

    # The standard output from this point is placed by an in-memory
    # buffer. This was originally done much later, but due to the indroduction
    # of the threads which need to access these elements, this was put in
    # global location.
    oldstdout = sys.stdout
    sys.stdout = StringIO()

    global g_oldstdout
    g_oldstdout = oldstdout

    global g_fwXmlFileName
    g_fwXmlFileName =  fwXmlFileName

    def setupUi(self, MainWindow):
        # Set the directory to user's home directory
        os.chdir(os.environ["HOME"])

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(599, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_fw = QtGui.QWidget()
        self.tab_fw.setObjectName(_fromUtf8("tab_fw"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_fw)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.textEdit_fwcmdlineoutput = QtGui.QTextEdit(self.tab_fw)

        global g_textEdit_fwcmdlineoutput
        g_textEdit_fwcmdlineoutput = self.textEdit_fwcmdlineoutput     

        self.textEdit_fwcmdlineoutput.setObjectName(_fromUtf8("textEdit_fwcmdlineoutput"))
        self.gridLayout_3.addWidget(self.textEdit_fwcmdlineoutput, 6, 0, 1, 6)
        self.label_fw_image = QtGui.QLabel(self.tab_fw)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fw_image.setFont(font)
        self.label_fw_image.setObjectName(_fromUtf8("label_fw_image"))
        self.gridLayout_3.addWidget(self.label_fw_image, 1, 0, 1, 2)
        self.label_fw_xmlFile = QtGui.QLabel(self.tab_fw)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fw_xmlFile.setFont(font)
        self.label_fw_xmlFile.setObjectName(_fromUtf8("label_fw_xmlFile"))
        self.gridLayout_3.addWidget(self.label_fw_xmlFile, 3, 0, 1, 2)
        self.label_fwcmdlineoutput = QtGui.QLabel(self.tab_fw)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fwcmdlineoutput.setFont(font)
        self.label_fwcmdlineoutput.setObjectName(_fromUtf8("label_fwcmdlineoutput"))
        self.gridLayout_3.addWidget(self.label_fwcmdlineoutput, 5, 0, 1, 1)
        self.label_fwhdr = QtGui.QLabel(self.tab_fw)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_fwhdr.setFont(font)
        self.label_fwhdr.setWordWrap(True)
        self.label_fwhdr.setObjectName(_fromUtf8("label_fwhdr"))
        self.gridLayout_3.addWidget(self.label_fwhdr, 0, 0, 1, 6)
        self.lineEdit_fw_image = QtGui.QLineEdit(self.tab_fw)
        self.lineEdit_fw_image.setObjectName(_fromUtf8("lineEdit_fw_image"))
        self.gridLayout_3.addWidget(self.lineEdit_fw_image, 2, 0, 1, 5)
        self.toolButton_fw_xmlFile = QtGui.QToolButton(self.tab_fw)
        self.toolButton_fw_xmlFile.setObjectName(_fromUtf8("toolButton_fw_xmlFile"))
        self.gridLayout_3.addWidget(self.toolButton_fw_xmlFile, 4, 5, 1, 1)
        self.lineEdit_fw_xmlFile = QtGui.QLineEdit(self.tab_fw)
        self.lineEdit_fw_xmlFile.setObjectName(_fromUtf8("lineEdit_fw_xmlFile"))
        self.gridLayout_3.addWidget(self.lineEdit_fw_xmlFile, 4, 0, 1, 5)
        self.toolButton_fw_image = QtGui.QToolButton(self.tab_fw)
        self.toolButton_fw_image.setObjectName(_fromUtf8("toolButton_fw_image"))
        self.gridLayout_3.addWidget(self.toolButton_fw_image, 2, 5, 1, 1)
        self.pb_fw_close = QtGui.QPushButton(self.tab_fw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_fw_close.sizePolicy().hasHeightForWidth())
        self.pb_fw_close.setSizePolicy(sizePolicy)
        self.pb_fw_close.setObjectName(_fromUtf8("pb_fw_close"))
        self.gridLayout_3.addWidget(self.pb_fw_close, 7, 2, 1, 1)
        self.pb_fw_cancel = QtGui.QPushButton(self.tab_fw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_fw_cancel.sizePolicy().hasHeightForWidth())
        self.pb_fw_cancel.setSizePolicy(sizePolicy)
        self.pb_fw_cancel.setObjectName(_fromUtf8("pb_fw_cancel"))
        self.gridLayout_3.addWidget(self.pb_fw_cancel, 7, 3, 1, 1)
        self.pb_fw_run = QtGui.QPushButton(self.tab_fw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_fw_run.sizePolicy().hasHeightForWidth())
        self.pb_fw_run.setSizePolicy(sizePolicy)
        self.pb_fw_run.setObjectName(_fromUtf8("pb_fw_run"))
        self.gridLayout_3.addWidget(self.pb_fw_run, 7, 4, 1, 1)


        #self.progressBar_fw = QtGui.QProgressBar(self.tab_fw)
        self.progressBar_fw = ProgressBar()
        global global_fw
        global_fw =  self.progressBar_fw

        self.progressBar_fw.setProperty("value", 1)
        self.progressBar_fw.setObjectName(_fromUtf8("progressBar_fw"))
        self.gridLayout_3.addWidget(self.progressBar_fw, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab_fw, _fromUtf8(""))

        '''
        self.tab_bev = QtGui.QWidget()
        self.tab_bev.setObjectName(_fromUtf8("tab_bev"))
        self.pushButton_bev = QtGui.QPushButton(self.tab_bev)
        self.pushButton_bev.setGeometry(QtCore.QRect(220, 130, 135, 27))
        self.pushButton_bev.setObjectName(_fromUtf8("pushButton_bev"))
        self.label_bevhdr = QtGui.QLabel(self.tab_bev)
        self.label_bevhdr.setGeometry(QtCore.QRect(9, 9, 561, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_bevhdr.setFont(font)
        self.label_bevhdr.setWordWrap(True)
        self.label_bevhdr.setObjectName(_fromUtf8("label_bevhdr"))
        self.tabWidget.addTab(self.tab_bev, _fromUtf8(""))
        '''

        '''
        self.tab_bev = QtGui.QWidget()
        self.tab_bev.setObjectName(_fromUtf8("tab_bev"))
        self.pb_bev_close = QtGui.QPushButton(self.tab_bev)
        self.pb_bev_close.setGeometry(QtCore.QRect(493, 518, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_bev_close.sizePolicy().hasHeightForWidth())
        self.pb_bev_close.setSizePolicy(sizePolicy)
        self.pb_bev_close.setObjectName(_fromUtf8("pb_bev_close"))
        self.textEdit_bev = QtGui.QTextEdit(self.tab_bev)
        self.textEdit_bev.setGeometry(QtCore.QRect(9, 269, 571, 211))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_bev.sizePolicy().hasHeightForWidth())
        self.textEdit_bev.setSizePolicy(sizePolicy)
        self.textEdit_bev.setObjectName(_fromUtf8("textEdit_bev"))
        self.label_bevhdr = QtGui.QLabel(self.tab_bev)
        self.label_bevhdr.setGeometry(QtCore.QRect(10, 20, 551, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bevhdr.sizePolicy().hasHeightForWidth())
        self.label_bevhdr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_bevhdr.setFont(font)
        self.label_bevhdr.setWordWrap(True)
        self.label_bevhdr.setObjectName(_fromUtf8("label_bevhdr"))
        self.pushButton_bev = QtGui.QPushButton(self.tab_bev)
        self.pushButton_bev.setGeometry(QtCore.QRect(200, 160, 135, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bev.sizePolicy().hasHeightForWidth())
        self.pushButton_bev.setSizePolicy(sizePolicy)
        self.pushButton_bev.setObjectName(_fromUtf8("pushButton_bev"))
        self.label_bev_commandline = QtGui.QLabel(self.tab_bev)
        self.label_bev_commandline.setGeometry(QtCore.QRect(20, 240, 181, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_bev_commandline.setFont(font)
        self.label_bev_commandline.setObjectName(_fromUtf8("label_bev_commandline"))
        self.tabWidget.addTab(self.tab_bev, _fromUtf8(""))
        '''
        self.tab_bev = QtGui.QWidget()
        self.tab_bev.setObjectName(_fromUtf8("tab_bev"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_bev)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_bevhdr = QtGui.QLabel(self.tab_bev)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bevhdr.sizePolicy().hasHeightForWidth())
        self.label_bevhdr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_bevhdr.setFont(font)
        self.label_bevhdr.setWordWrap(True)
        self.label_bevhdr.setObjectName(_fromUtf8("label_bevhdr"))
        self.gridLayout_5.addWidget(self.label_bevhdr, 0, 0, 1, 3)
        self.textEdit_bev = QtGui.QTextEdit(self.tab_bev)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_bev.sizePolicy().hasHeightForWidth())
        self.textEdit_bev.setSizePolicy(sizePolicy)
        self.textEdit_bev.setObjectName(_fromUtf8("textEdit_bev"))
        self.gridLayout_5.addWidget(self.textEdit_bev, 5, 0, 1, 3)
        self.pb_bev_close = QtGui.QPushButton(self.tab_bev)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_bev_close.sizePolicy().hasHeightForWidth())
        self.pb_bev_close.setSizePolicy(sizePolicy)
        self.pb_bev_close.setObjectName(_fromUtf8("pb_bev_close"))
        self.gridLayout_5.addWidget(self.pb_bev_close, 6, 2, 1, 1)
        self.label_bev_commandline = QtGui.QLabel(self.tab_bev)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bev_commandline.sizePolicy().hasHeightForWidth())
        self.label_bev_commandline.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_bev_commandline.setFont(font)
        self.label_bev_commandline.setObjectName(_fromUtf8("label_bev_commandline"))
        self.gridLayout_5.addWidget(self.label_bev_commandline, 3, 0, 1, 1)
        self.pushButton_bev = QtGui.QPushButton(self.tab_bev)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bev.sizePolicy().hasHeightForWidth())
        self.pushButton_bev.setSizePolicy(sizePolicy)
        self.pushButton_bev.setObjectName(_fromUtf8("pushButton_bev"))
        self.gridLayout_5.addWidget(self.pushButton_bev, 1, 1, 2, 1)
        self.tabWidget.addTab(self.tab_bev, _fromUtf8(""))

        self.tab_ann = QtGui.QWidget()
        self.tab_ann.setObjectName(_fromUtf8("tab_ann"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_ann)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_ann_annDir = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_annDir.setFont(font)
        self.label_ann_annDir.setObjectName(_fromUtf8("label_ann_annDir"))
        self.gridLayout_4.addWidget(self.label_ann_annDir, 5, 0, 1, 4)
        self.pb_ann_close = QtGui.QPushButton(self.tab_ann)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ann_close.sizePolicy().hasHeightForWidth())
        self.pb_ann_close.setSizePolicy(sizePolicy)
        self.pb_ann_close.setObjectName(_fromUtf8("pb_ann_close"))
        self.gridLayout_4.addWidget(self.pb_ann_close, 11, 2, 1, 1)
        self.toolButton_ann_annDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_annDir.setObjectName(_fromUtf8("toolButton_ann_annDir"))
        self.gridLayout_4.addWidget(self.toolButton_ann_annDir, 6, 5, 1, 1)
        self.textEdit_ann = QtGui.QTextEdit(self.tab_ann)
        self.textEdit_ann.setAutoFillBackground(True)

        global g_textEdit_anncmdlineoutput
        g_textEdit_anncmdlineoutput = self.textEdit_ann
        

        self.textEdit_ann.setObjectName(_fromUtf8("textEdit_ann"))
        self.gridLayout_4.addWidget(self.textEdit_ann, 10, 0, 1, 6)
        self.label_anncmdlineoutput = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_anncmdlineoutput.setFont(font)
        self.label_anncmdlineoutput.setObjectName(_fromUtf8("label_anncmdlineoutput"))
        self.gridLayout_4.addWidget(self.label_anncmdlineoutput, 9, 0, 1, 1)
        self.toolButton_ann_image = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_image.setObjectName(_fromUtf8("toolButton_ann_image"))
        self.gridLayout_4.addWidget(self.toolButton_ann_image, 2, 5, 1, 1)
        self.label_ann_image = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_image.setFont(font)
        self.label_ann_image.setObjectName(_fromUtf8("label_ann_image"))
        self.gridLayout_4.addWidget(self.label_ann_image, 1, 0, 1, 1)
        self.label_ann_beFeatDir = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_beFeatDir.setFont(font)
        self.label_ann_beFeatDir.setObjectName(_fromUtf8("label_ann_beFeatDir"))
        self.gridLayout_4.addWidget(self.label_ann_beFeatDir, 3, 0, 1, 4)
        self.pb_ann_cancel = QtGui.QPushButton(self.tab_ann)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ann_cancel.sizePolicy().hasHeightForWidth())
        self.pb_ann_cancel.setSizePolicy(sizePolicy)
        self.pb_ann_cancel.setObjectName(_fromUtf8("pb_ann_cancel"))
        self.gridLayout_4.addWidget(self.pb_ann_cancel, 11, 3, 1, 1)
        self.pb_ann_run = QtGui.QPushButton(self.tab_ann)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ann_run.sizePolicy().hasHeightForWidth())
        self.pb_ann_run.setSizePolicy(sizePolicy)
        self.pb_ann_run.setObjectName(_fromUtf8("pb_ann_run"))
        self.gridLayout_4.addWidget(self.pb_ann_run, 11, 4, 1, 1)
        self.lineEdit_ann_image = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_image.setText(_fromUtf8(""))
        self.lineEdit_ann_image.setObjectName(_fromUtf8("lineEdit_ann_image"))
        self.gridLayout_4.addWidget(self.lineEdit_ann_image, 2, 0, 1, 5)
        self.lineEdit_ann_bcpyDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_bcpyDir.setText(_fromUtf8(""))
        self.lineEdit_ann_bcpyDir.setObjectName(_fromUtf8("lineEdit_ann_bcpyDir"))
        self.gridLayout_4.addWidget(self.lineEdit_ann_bcpyDir, 8, 0, 1, 5)
        self.toolButton_ann_beFeatDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_beFeatDir.setObjectName(_fromUtf8("toolButton_ann_beFeatDir"))
        self.gridLayout_4.addWidget(self.toolButton_ann_beFeatDir, 4, 5, 1, 1)
        self.label_ann_bcpyDir = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ann_bcpyDir.setFont(font)
        self.label_ann_bcpyDir.setObjectName(_fromUtf8("label_ann_bcpyDir"))
        self.gridLayout_4.addWidget(self.label_ann_bcpyDir, 7, 0, 1, 4)
        self.label_annhdr = QtGui.QLabel(self.tab_ann)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_annhdr.setFont(font)
        self.label_annhdr.setWordWrap(True)
        self.label_annhdr.setObjectName(_fromUtf8("label_annhdr"))
        self.gridLayout_4.addWidget(self.label_annhdr, 0, 0, 1, 6)
        self.lineEdit_ann_annDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_annDir.setObjectName(_fromUtf8("lineEdit_ann_annDir"))
        self.gridLayout_4.addWidget(self.lineEdit_ann_annDir, 6, 0, 1, 5)
        self.lineEdit_ann_beFeatDir = QtGui.QLineEdit(self.tab_ann)
        self.lineEdit_ann_beFeatDir.setText(_fromUtf8(""))
        self.lineEdit_ann_beFeatDir.setObjectName(_fromUtf8("lineEdit_ann_beFeatDir"))
        self.gridLayout_4.addWidget(self.lineEdit_ann_beFeatDir, 4, 0, 1, 5)

        self.toolButton_ann_bcpyDir = QtGui.QToolButton(self.tab_ann)
        self.toolButton_ann_bcpyDir.setObjectName(_fromUtf8("toolButton_ann_bcpyDir"))
        self.gridLayout_4.addWidget(self.toolButton_ann_bcpyDir, 8, 5, 1, 1)

        #self.progressBar_ann = QtGui.QProgressBar(self.tab_ann)
        self.progressBar_ann = ProgressBar()
        global global_ann
        global_ann = self.progressBar_ann
  
        self.progressBar_ann.setProperty("value", 1)
        self.progressBar_ann.setObjectName(_fromUtf8("progressBar_ann"))
        self.gridLayout_4.addWidget(self.progressBar_ann, 11, 0, 1, 1)
        self.tabWidget.addTab(self.tab_ann, _fromUtf8(""))

        self.tab_rep = QtGui.QWidget()
        self.tab_rep.setObjectName(_fromUtf8("tab_rep"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_rep)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_rep_outdir = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_outdir.setObjectName(_fromUtf8("lineEdit_rep_outdir"))
        self.gridLayout_2.addWidget(self.lineEdit_rep_outdir, 6, 0, 1, 4)
        self.label_rephdr = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_rephdr.setFont(font)
        self.label_rephdr.setWordWrap(True)
        self.label_rephdr.setObjectName(_fromUtf8("label_rephdr"))
        self.gridLayout_2.addWidget(self.label_rephdr, 0, 0, 1, 5)
        self.label_rep_fwxmlfile = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_fwxmlfile.setFont(font)
        self.label_rep_fwxmlfile.setObjectName(_fromUtf8("label_rep_fwxmlfile"))
        self.gridLayout_2.addWidget(self.label_rep_fwxmlfile, 1, 0, 1, 1)
        self.lineEdit_rep_fwxmlfile = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_fwxmlfile.setText(_fromUtf8(""))
        self.lineEdit_rep_fwxmlfile.setObjectName(_fromUtf8("lineEdit_rep_fwxmlfile"))
        self.gridLayout_2.addWidget(self.lineEdit_rep_fwxmlfile, 2, 0, 1, 4)
        self.toolButton_rep_fwxmlfile = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_fwxmlfile.setObjectName(_fromUtf8("toolButton_rep_fwxmlfile"))
        self.gridLayout_2.addWidget(self.toolButton_rep_fwxmlfile, 2, 4, 1, 1)
        self.label_rep_annDir = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_annDir.setFont(font)
        self.label_rep_annDir.setObjectName(_fromUtf8("label_rep_annDir"))
        self.gridLayout_2.addWidget(self.label_rep_annDir, 3, 0, 1, 1)
        self.lineEdit_rep_annDir = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_annDir.setText(_fromUtf8(""))
        self.lineEdit_rep_annDir.setObjectName(_fromUtf8("lineEdit_rep_annDir"))
        self.gridLayout_2.addWidget(self.lineEdit_rep_annDir, 4, 0, 1, 4)
        self.toolButton_rep_annDir = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_annDir.setObjectName(_fromUtf8("toolButton_rep_annDir"))
        self.gridLayout_2.addWidget(self.toolButton_rep_annDir, 4, 4, 1, 1)
        self.label_rep_outdir = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_outdir.setFont(font)
        self.label_rep_outdir.setObjectName(_fromUtf8("label_rep_outdir"))
        self.gridLayout_2.addWidget(self.label_rep_outdir, 5, 0, 1, 1)
        self.toolButton_rep_outdir = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_outdir.setObjectName(_fromUtf8("toolButton_rep_outdir"))
        self.gridLayout_2.addWidget(self.toolButton_rep_outdir, 6, 4, 1, 1)
        self.label_rep_confile = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_confile.setFont(font)
        self.label_rep_confile.setObjectName(_fromUtf8("label_rep_confile"))
        self.gridLayout_2.addWidget(self.label_rep_confile, 7, 0, 1, 1)
        self.lineEdit_rep_confile = QtGui.QLineEdit(self.tab_rep)
        self.lineEdit_rep_confile.setObjectName(_fromUtf8("lineEdit_rep_confile"))
        self.gridLayout_2.addWidget(self.lineEdit_rep_confile, 8, 0, 1, 4)
        self.toolButton_rep_confile = QtGui.QToolButton(self.tab_rep)
        self.toolButton_rep_confile.setObjectName(_fromUtf8("toolButton_rep_confile"))
        self.gridLayout_2.addWidget(self.toolButton_rep_confile, 8, 4, 1, 1)
        self.label_rep_cmdlineoutput = QtGui.QLabel(self.tab_rep)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rep_cmdlineoutput.setFont(font)
        self.label_rep_cmdlineoutput.setObjectName(_fromUtf8("label_rep_cmdlineoutput"))
        self.gridLayout_2.addWidget(self.label_rep_cmdlineoutput, 9, 0, 1, 1)
        self.textEdit_rep = QtGui.QTextEdit(self.tab_rep)
        self.textEdit_rep.setAutoFillBackground(True)

        global g_textEdit_repcmdlineoutput
        g_textEdit_repcmdlineoutput = self.textEdit_rep

        self.textEdit_rep.setObjectName(_fromUtf8("textEdit_rep"))
        self.gridLayout_2.addWidget(self.textEdit_rep, 10, 0, 1, 5)
        self.pb_rep_run = QtGui.QPushButton(self.tab_rep)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_rep_run.sizePolicy().hasHeightForWidth())
        self.pb_rep_run.setSizePolicy(sizePolicy)
        self.pb_rep_run.setObjectName(_fromUtf8("pb_rep_run"))
        self.gridLayout_2.addWidget(self.pb_rep_run, 11, 3, 1, 1)
        self.pb_rep_cancel = QtGui.QPushButton(self.tab_rep)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_rep_cancel.sizePolicy().hasHeightForWidth())
        self.pb_rep_cancel.setSizePolicy(sizePolicy)
        self.pb_rep_cancel.setObjectName(_fromUtf8("pb_rep_cancel"))
        self.gridLayout_2.addWidget(self.pb_rep_cancel, 11, 2, 1, 1)
        self.pb_rep_close = QtGui.QPushButton(self.tab_rep)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_rep_close.sizePolicy().hasHeightForWidth())
        self.pb_rep_close.setSizePolicy(sizePolicy)
        self.pb_rep_close.setObjectName(_fromUtf8("pb_rep_close"))
        self.gridLayout_2.addWidget(self.pb_rep_close, 11, 1, 1, 1)

        #self.progressBar_rep = QtGui.QProgressBar(self.tab)
        self.progressBar_rep = ProgressBar()
        global global_rep
        global_rep = self.progressBar_rep

        self.progressBar_rep.setProperty("value", 1)
        self.progressBar_rep.setObjectName(_fromUtf8("progressBar_rep"))
        self.gridLayout_2.addWidget(self.progressBar_rep, 11, 0, 1, 1)
        self.tabWidget.addTab(self.tab_rep, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        ## Note: Check the following block
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionShow_Help = QtGui.QAction(MainWindow)
        self.actionShow_Help.setObjectName(_fromUtf8("actionShow_Help"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionShow_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # File navigation for Fiwalk XML Generation tab
        
        QtCore.QObject.connect(self.toolButton_fw_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwImageFileName)

        QtCore.QObject.connect(self.toolButton_fw_xmlFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getFwOutputXmlFilePath)

        QtCore.QObject.connect(self.pb_fw_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedOkFw)
        QtCore.QObject.connect(self.pb_fw_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)
        QtCore.QObject.connect(self.pb_fw_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)

        # File navigation for beview tab
        QtCore.QObject.connect(self.pb_bev_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)

        # File navigation for Annotated files Tab
        QtCore.QObject.connect(self.toolButton_ann_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnImageFileName)

        QtCore.QObject.connect(self.toolButton_ann_beFeatDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getBeFeatDir)
        QtCore.QObject.connect(self.toolButton_ann_annDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnOutputDir)
        QtCore.QObject.connect(self.toolButton_ann_bcpyDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAnnBcpyDir)

        QtCore.QObject.connect(self.pb_ann_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedOkAnn)
        QtCore.QObject.connect(self.pb_ann_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)
        QtCore.QObject.connect(self.pb_ann_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)

        # File navigation for Reports Tab
        QtCore.QObject.connect(self.toolButton_rep_fwxmlfile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepFwXmlFileName)
        QtCore.QObject.connect(self.toolButton_rep_outdir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepOutputDir)
        QtCore.QObject.connect(self.toolButton_rep_confile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepConfigFile)
        QtCore.QObject.connect(self.toolButton_rep_annDir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getRepBeAnnotatedDir)

        QtCore.QObject.connect(self.pb_rep_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedOkRep)
        QtCore.QObject.connect(self.pb_rep_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)
        QtCore.QObject.connect(self.pb_rep_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedCancel)

        self.actionExit.triggered.connect(self.exitMenu)
        self.actionCopy.triggered.connect(self.copyMenu)
        self.actionCut.triggered.connect(self.cutMenu)
        self.actionPaste.triggered.connect(self.pasteMenu)

        ##QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL("triggered()"), QtCore.SLOT("paste ()"))
        ##QtCore.QObject.connect(self.actionCut, QtCore.SIGNAL("triggered()"), QtCore.SLOT("cut ()"))
        ##QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL("triggered()"), self.text, QtCore.SLOT("copy ()"))


        self.progressBar_fw.show()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exitMenu(self):
        QtCore.QCoreApplication.instance().quit()

    def cutMenu(self):

        cutData = myClipBoard.text("plain",QClipboard.Selection)
        print ("The clipboard has ",  cutData)
        print ("SELECTION ",  QClipboard.Selection)
        print ("CLIPBOARD ",  QClipboard.Clipboard)
        print ("OWNS_CLIPBOARD ",  QClipboard.ownsClipboard())
        print ("OWNS_FINDBUF ",  QClipboard.ownsFindBuffer())
        print ("OWNS_Selection ",  QClipboard.ownsSelection())
        myClipBoard.setText(cutData.text(), QClipboard.Selection)

    def copyMenu(self):
        print("Copying text ")

    def pasteMenu(self):
        print("PASTINGg text ")

    # buttonClickCancel: This called by any click that represents the
    # "Reject" role - Cancel and Close here. It just terminates the Gui.
    def buttonClickedCancel(self):
        QtCore.QCoreApplication.instance().quit()

    def getImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName(caption="Select an image file")
        print(">> Image File Selected: ", image_file)

        self.lineEdit_image.setText(image_file)
        
        self.imageFileName = image_file

    def getFwImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName(caption="Select an image file")
        print(">> Image File Selected: ", image_file)

        self.lineEdit_fw_image.setText(image_file)
        
        self.fwimageFileName = image_file

    def getBeImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName(caption="Select an image file")
        print(">> Image File Selected: ", image_file)

        self.lineEdit_be_image.setText(image_file)
        
        self.beImageFileName = image_file

    def getAnnImageFileName(self):
        # Navigation
        image_file = QtGui.QFileDialog.getOpenFileName(caption="Select an image file")
        print(">> Image File Selected: ", image_file)

        self.lineEdit_ann_image.setText(image_file)
        
        self.annImageFileName = image_file

    def getbcpyDir(self):
        # Navigation
        bcpyDir = QtGui.QFileDialog.getExistingDirectory(caption="Create a directory for the annotation")
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
        outdir = QtGui.QFileDialog.getSaveFileName(caption="Select the bulk extractor feature directory")

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
        beFeatDir = QtGui.QFileDialog.getExistingDirectory(caption="Select the bulk extractor feature directory")
        print(">> Annotate: BE Features Directory Selected: ", beFeatDir)

        self.lineEdit_ann_beFeatDir.setText(beFeatDir)
        
        self.annBeFeatDir = beFeatDir

    def getAnnOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        ann_outdir = QtGui.QFileDialog.getSaveFileName(caption="Create a directory for the annotation")

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
        bcpyDir = QtGui.QFileDialog.getExistingDirectory(caption="")
        print(">> BC Python Directory Selected: ", bcpyDir)

        self.lineEdit_ann_bcpyDir.setText(bcpyDir)
        
        self.annBcpyDir = bcpyDir

    def getFwOutputXmlFilePath(self):
        # Navigation
        xml_output_file = QtGui.QFileDialog.getSaveFileName(caption="Select a location and enter a filename")
        ## print("D: Fiwalk XML File Selected: ", xml_output_file)

        self.lineEdit_fw_xmlFile.setText(xml_output_file)
        
        self.xmlFileName = xml_output_file
        self.TextFileName = xml_output_file + '.txt'

    # get: Routine to let the user choose the XML file -
    # by navigating trough the directories
    def getRepFwXmlFileName(self):
        # Navigation
        xml_file = QtGui.QFileDialog.getOpenFileName(caption="Select a fiwalk XML file")
        # print("D: Fiwalk XML File Selected: ", xml_file)

        self.lineEdit_rep_fwxmlfile.setText(xml_file)

        self.repFwXmlFileName = xml_file
        return xml_file
    
    # getRepBeAnnotatedDir: Routine to let the user choose the Directory name
    # containing the annotated files by navigating
    def getRepBeAnnotatedDir(self):
        ann_dir = QtGui.QFileDialog.getExistingDirectory(caption="Select an annotated features directory")
        # print("D: Annotated Directory Selected by navigating: ", ann_dir)

        self.lineEdit_rep_annDir.setText(ann_dir)
        self.repAnnDir = ann_dir
        return ann_dir

    # getOutputDir: Routine to let the user choose the Directory name
    # to output the reports by navigating
    def getRepOutputDir(self):
        # Since This directory should not exist, use getSaveFileName
        # to let the user create a new directory.
        outdir = QtGui.QFileDialog.getSaveFileName(caption="Create a report directory")

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
            print("\n>> Success!!! Bulk-extractor created feature files in Directory ", self.beDir)

        # Now create the XML file using fiwalk
        self.xmlFileName = self.outputDirName + '/fiwalkXmlFile.xml'
        self.TextFileName = self.outputDirName + '/fiwalkXmlFile.txt'
        #cmd = ['fiwalk', '-f', '-X', self.xmlFileName, '-T', self.TextFileName, self.imageFileName]
        cmd = ['fiwalk', '-f', '-X', self.xmlFileName, self.imageFileName]
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
            print("\n>> Success!!! Fiwalk created the following file(s): \n")
            print(" o ", self.xmlFileName)
            #print(" o ", self.TextFileName)

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

        print("\n>> Success!!! Annotated files created the directory: ", self.annDir)

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
        '''
        bc_get_reports(PdfReport, FiwalkReport, self.xmlFileName, \
                                 self.annDir, \
                                 self.reportsDir, \
                                 self.configFileName)
        '''

        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    # buttonClickedOkFw: Routine invoked when the "Run" (formerly OK) 
    # button on the Fiwalk tab is pressed.
    def buttonClickedOkFw(self):
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

            # Thread uses it. so copy to the global value
            global g_fwXmlFileName
            g_fwXmlFileName = self.fwXmlFileName
            ## print("D: XML File Selected from the box: ", self.xmlFileName)

        cmd = ['fiwalk', '-f', '-X', self.fwXmlFileName, self.fwImageFileName]
        print(">> Command Executed for Fiwalk = ", cmd)

        # Start two threads - one for executing the above command and
        # a second one to start a progress bar on the gui which keeps
        # spinning till the first thread finishes the command execution
        # and signals the second one by setting a flag. 
        thread1 = bcThread_fw(cmd)
        thread2 = guiThread("fiwalk")
        thread1.start()
        thread2.start()

        # Terminate the redirecting of the stdout to the in-memory buffer.
        #### Commented for now, as it is called from the thread : FIXME
        ####self.textEdit_fwcmdlineoutput.setText( sys.stdout.getvalue() )
        ####sys.stdout = self.oldstdout

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
           print("\n>> Success!!! Bulk_extractor created the feature files in the Directory: ", self.beOutputDirName)
           print("\n")
        
        # Terminate the redirecting of the stdout to the in-memory buffer.
        self.textEdit_becmdlineoutput.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    # buttonClickedOkAnn: Routine invoked when the "Run" (formerly OK) 
    # button on the Annotate tab is pressed.
    def buttonClickedOkAnn(self):
        oldstdout = sys.stdout
        sys.stdout = StringIO()

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
            # print("D: Ann Output Dir Selected from the box: ", self.annOutputDirName)

        # If annBcpyDir Dir is not selected through menu, see if it is
        # typed in the text box:
        if ui.lineEdit_ann_bcpyDir.text() != self.annBcpyDir:
            self.annBcpyDir = ui.lineEdit_ann_bcpyDir.text()
            # print("D: Ann Bcpy Dir Selected from the box: ", self.annBcpyDir)

        # If bcpyDir doesn't exist, default it to
        # /home/bcadmin/Tools/bulk_extractor/python

        if not os.path.exists(self.annBcpyDir):
            # print("D: Setting default directory for BC python directory")
            self.annBcpyDir = "/home/bcadmin/Tools/bulk_extractor/python"

        identify_cmd = self.annBcpyDir + '/' + 'identify_filenames.py'
        #print("D: annBcpyDir: ", self.annBcpyDir)

        cmd = ['python3',identify_cmd,'--all','--imagefile',\
          self.annImageFileName, self.annBeFeatDir, self.annOutputDirName]
        print("\n>> Running identify_filanames script : ", cmd)

        # Start two threads - one for executing the above command and
        # a second one to start a progress bar on the gui which keeps
        # spinning till the first thread finishes the command execution
        # and signals the second one by setting a flag. 
        thread1 = bcThread_ann(cmd, self.annOutputDirName)
        thread2 = guiThread("ann")
        thread1.start()
        thread2.start()

    # buttonClickedOkRep: Routine invoked when the "Run" (formerly OK) 
    # button on the Reports tab is pressed.
    def buttonClickedOkRep(self):
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()
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
            self.textEdit_rep.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout
            return

        # Start two threads - one for executing the above command and
        # a second one to start a progress bar on the gui which keeps
        # spinning till the first thread finishes the command execution
        # and signals the second one by setting a flag. 
        thread1 = bcThread_rep(PdfReport, FiwalkReport, \
                               self.repFwXmlFileName,self.repAnnDir, \
                               self.repOutDir, self.repConfile )
        thread2 = guiThread("rep")
        thread1.start()
        thread2.start()

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
        ## print(">> [D] Config File Selected navigating: ", config_file)
        print(">> Config File Selected: ", config_file)

        self.lineEdit_confile.setText(config_file)
        self.configFileName = config_file
        return config_file

    def bc_rep_check_parameters(self):
        # If XML file not selected through menu, see if it is typed in the box:

        if ui.lineEdit_rep_fwxmlfile.text() != self.repFwXmlFileName:
            self.repFwXmlFileName = ui.lineEdit_rep_fwxmlfile.text()
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
            self.repConfile = ui.lineEdit_rep_confile.text()
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
            self.imageFileName = ui.lineEdit_image.text()
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
            self.configFileName = ui.lineEdit_configFile.text()
            # print("D: Config File selected from the box: ", self.configFileName)

        # If config file is not provided by the user, user the default one
        if not os.path.exists(self.configFileName):
            print(">> Using the default config file: /etc/bitcurator/bc_report_config.txt")
            self.configFileName = "/etc/bitcurator/bc_report_config.txt"

        return (0)

    def on_pushButton_bev_clicked(self):
        
        #cmd = ['/usr/bin/java -Xmx1g -jar /home/sunitha/BC/beviewer/BEViewer.jar']
        #cmdstr = "/home/sunitha/BC/kambc/bitcurator/python/beviewer_sh"
        cmdstr = "/usr/bin/java -Xmx1g -jar /home/bcadmin/Tools/bulk_extractor/java_gui/BEViewer.jar"

        print(">> Launching BEViewer >> ")
        
        # Note: We can't use Popen here as the call to Popen blocks, which
        # doesn't let us get back to the GUI when the viewer is launched.
        # startDetached apparently seems to fix that issue.

        QtCore.QProcess.startDetached(cmdstr)
        self.textEdit_bev.setText( sys.stdout.getvalue() )
        sys.stdout = self.oldstdout

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bitcurator Reports", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fw), QtGui.QApplication.translate("MainWindow", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bev), QtGui.QApplication.translate("MainWindow", "BEViewer", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_bev.clicked.connect(self.on_pushButton_bev_clicked)
 

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ann), QtGui.QApplication.translate("MainWindow", "Annotated Features", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rep), QtGui.QApplication.translate("MainWindow", "Reports", None, QtGui.QApplication.UnicodeUTF8))

        # Tab: Reports
        self.lineEdit_rep_fwxmlfile.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_fwxmlfile.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_fwxmlfile.setText(QtGui.QApplication.translate("MainWindow", "Fiwalk XML File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_outdir.setText(QtGui.QApplication.translate("MainWindow", "Output Directory For Reports (new)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_outdir.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_outdir.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_confile.setText(QtGui.QApplication.translate("MainWindow", "Config File (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_confile.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_confile.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rep_cmdlineoutput.setText(QtGui.QApplication.translate("MainWindow", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))

        # Reports Tab: bush buttons
        self.pb_rep_run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_rep_cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_rep_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

        self.label_rep_annDir.setText(QtGui.QApplication.translate("MainWindow", "Annotated Feature Files Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_rep_annDir.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_rep_annDir.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rephdr.setText(QtGui.QApplication.translate("MainWindow", "Produces Office Open XML and PDF reports to assist in image analysis", None, QtGui.QApplication.UnicodeUTF8))
        
        # Tab-2: Fiwalk XML
        self.lineEdit_fw_image.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_image.setText(QtGui.QApplication.translate("MainWindow", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fw_xmlFile.setText(QtGui.QApplication.translate("MainWindow", "Output XML File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_fw_xmlFile.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_fw_image.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

        ## Fiwalk - push buttons
        self.pb_fw_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_fw_cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_fw_run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))

        self.toolButton_fw_xmlFile.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fw), QtGui.QApplication.translate("MainWindow", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fwhdr.setText(QtGui.QApplication.translate("MainWindow", "Fiwalk produces a DFXML file showing the volumes, directories, and files contained within a disk image.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fwcmdlineoutput.setText(QtGui.QApplication.translate("MainWindow", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))

        # beview - close button, Launch button and cmd line label

        self.label_bevhdr.setText(QtGui.QApplication.translate("MainWindow", "Bulk extractor scans disk images, files, and directories and extracts features of interest without parsing the file system. Click on the button to launch the bulk extractor GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_bev_commandline.setText(QtGui.QApplication.translate("MainWindow", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bev.setText(QtGui.QApplication.translate("MainWindow", "Launch BEViewer", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_bev_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

        # Tab-4: Annotated Files
        self.label_ann_image.setText(QtGui.QApplication.translate("MainWindow", "Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_beFeatDir.setText(QtGui.QApplication.translate("MainWindow", "Bulk Extractor Feature Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_annDir.setText(QtGui.QApplication.translate("MainWindow", "Annotated Feature Files Directory (new)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ann_bcpyDir.setText(QtGui.QApplication.translate("MainWindow", "Bulk Extractor Python Directory (optional)", None, QtGui.QApplication.UnicodeUTF8))

        ## Annotated Files: Push buttons
        self.pb_ann_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_ann_cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_ann_run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))

        self.lineEdit_ann_image.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_beFeatDir.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_annDir.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/Path/To/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ann_bcpyDir.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "/home/bcadmin/Tools/bulk_extractor/python", None, QtGui.QApplication.UnicodeUTF8))

        self.toolButton_ann_image.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_beFeatDir.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_annDir.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ann_bcpyDir.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.label_anncmdlineoutput.setText(QtGui.QApplication.translate("MainWindow", "Command Line Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_annhdr.setText(QtGui.QApplication.translate("MainWindow", "Produces reports that identify which bulk extractor features are contained within files in a disk image.", None, QtGui.QApplication.UnicodeUTF8))


        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Help.setText(QtGui.QApplication.translate("MainWindow", "Show Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

# Thread for running the fiwalk command
class bcThread_fw(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        (data, err) = Popen(self.cmd, stdout=PIPE, stderr=PIPE).communicate()

        if len(err) > 0 :
           ProgressBar._active = False
           
           x = Ui_MainWindow
           print(">> ERROR!!! Fiwalk terminated with error: \n", err)
           global g_textEdit_fwcmdlineoutput
           g_textEdit_fwcmdlineoutput.append( sys.stdout.getvalue() )
           sys.stdout = x.oldstdout

           # Set the progressbar maximum to > minimum so the spinning will stop
           global global_fw
           global_fw.progressbar.setRange(0,1)

           raise ValueError("fiwalk error (" + str(err).strip() + "): "+" ".join(self.cmd))
        else:

            # Set the progresbar active flag so the other thread can
            # get out of the while loop.
            ProgressBar._active = False
            #print("D: bcThread_fw: Progressbar Active Flag Set to: ", ProgressBar._active)

            print("\n>> Success!!! Fiwalk created the following file(s): \n")

            # Set the progressbar maximum to > minimum so the spinning will stop
            #global global_fw
            global_fw.progressbar.setRange(0,1)
           
            global g_fwXmlFileName
            print(" o ", g_fwXmlFileName) 

            x = Ui_MainWindow
            # Note: setText for seme reason, wouldn't work when used with
            # global value. append seems to work
            #g_textEdit_fwcmdlineoutput.setText( sys.stdout.getvalue() )
            g_textEdit_fwcmdlineoutput.append( sys.stdout.getvalue() )
            sys.stdout = x.oldstdout
                
# Thread for running the identify_filenames command
class bcThread_ann(threading.Thread):
    def __init__(self, cmd, outdir):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.outdir = outdir

    def run(self):
        (data, err) = Popen(self.cmd, stdout=PIPE, stderr=PIPE).communicate()
        if len(err) > 0:
            print(">> ERROR!!! identify_filenames terminated with error: \n", err)
            ProgressBar._active = False
            x = Ui_MainWindow
            g_textEdit_anncmdlineoutput.append( sys.stdout.getvalue() )
            sys.stdout = x.oldstdout

            # In case the progress bar is spinning, stop it
            global_ann.progressbar.setRange(0,1)
            raise ValueError("identify_filenames error (" + str(err).strip() + "): "+" ".join(self.cmd))
            exit(1)
        else:
            # Set the progresbar active flag so the other thread can
            # get out of the while loop.
            ProgressBar._active = False

            print("\n>> Success!!! Annotated feature files created in the directory: ", self.outdir)

            # Set the progressbar maximum to > minimum so the spinning will stop
            global_ann.progressbar.setRange(0,1)
           
            x = Ui_MainWindow

            g_textEdit_anncmdlineoutput.append( sys.stdout.getvalue() )
            sys.stdout = x.oldstdout

class bcThread_rep(threading.Thread):
    def __init__(self, PdfReport, FiwalkReport, \
                       repFwXmlFileName,repAnnDir, \
                       repOutDir, repConfile ):
        threading.Thread.__init__(self)
        self.PdfReport = PdfReport
        self.FiwalkReport = FiwalkReport
        self.repFwXmlFileName = repFwXmlFileName
        self.repAnnDir = repAnnDir
        self.repOutDir = repOutDir
        self.repConfile = repConfile

    def run(self):
        # Generate the reports now.
        bc_get_reports(PdfReport, FiwalkReport, self.repFwXmlFileName, \
                                 self.repAnnDir, \
                                 self.repOutDir, \
                                 self.repConfile)

        # Set the progresbar active flag so the other thread can
        # get out of the while loop.
        ProgressBar._active = False

        print("\n>> Success!!! Reports generated in the directory: ", self.repOutDir)

        # Set the progressbar maximum to > minimum so the spinning will stop
        global global_rep
        global_rep.progressbar.setRange(0,1)
           
        x = Ui_MainWindow
        global g_textEdit_repcmdlineoutput

        # Terminate the redirecting of the stdout to the in-memory buffer.
        g_textEdit_repcmdlineoutput.append( sys.stdout.getvalue() )
        sys.stdout = x.oldstdout


# This is the thread which spins in a loop till the other thread which
# does the work sets the flag once the task is completed.
class guiThread(threading.Thread):
    def __init__(self, cmd_type):
        threading.Thread.__init__(self)
        self.cmd_type = cmd_type

    def run(self):
        if self.cmd_type == "fiwalk":
            global global_fw
            progressbar = global_fw
        elif self.cmd_type == "ann":
            global global_ann
            progressbar = global_ann
        elif self.cmd_type == "rep":
            global global_rep
            progressbar = global_rep

        progressbar.startLoop_bc(self.cmd_type)

class ProgressBar(QtGui.QWidget):
    _active = False
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)
        self.progressbar = QtGui.QProgressBar()
        main_layout = QtGui.QGridLayout()
        main_layout.addWidget(self.progressbar, 0, 1)
        self.setLayout(main_layout)
        self.setWindowTitle('Progress')

    def closeEvent(self):
        self._active = False

    def startLoop_bc(self, cmd_type):
        self._active = True
        ProgressBar._active = True 

        if cmd_type == "fiwalk":
            global global_fw
            global_fw.progressbar.setRange(0,0)
        elif cmd_type == "ann":
            global global_ann
            global_ann.progressbar.setRange(0,0)
        elif cmd_type == "rep":
            global global_rep
            global_rep.progressbar.setRange(0,0)

        while True:
            time.sleep(1.05)
            QtGui.qApp.processEvents()
            #print("D: ProgressBar._active = ", ProgressBar._active)
            if not ProgressBar._active:
                #print ("D: startLoop_bc thread detected flag = ", ProgressBar._active)
                break
        ProgressBar._active = False

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
