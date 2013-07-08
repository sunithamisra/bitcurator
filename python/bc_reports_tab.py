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
    xmlFileName = "null"
    TextFileName = "null"
    beDir = "null"
    annDir = "null" 
    bcpyDir = "null" 
    outputDirName = "null"
    configFileName = "null"
    ReoirtsDir = "null"
    def setupUi(self, bc_Form):
        bc_Form.setObjectName(_fromUtf8("bc_Form"))
        bc_Form.resize(705, 723)
        self.tabWidget = QtGui.QTabWidget(bc_Form)
        self.tabWidget.setGeometry(QtCore.QRect(40, 60, 631, 571))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit_image = QtGui.QLineEdit(self.tab)
        self.lineEdit_image.setGeometry(QtCore.QRect(210, 60, 151, 21))
        self.lineEdit_image.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_image.setText(_fromUtf8(""))
        self.lineEdit_image.setObjectName(_fromUtf8("lineEdit_image"))
        self.toolButton_image = QtGui.QToolButton(self.tab)
        self.toolButton_image.setGeometry(QtCore.QRect(400, 60, 23, 25))
        self.toolButton_image.setObjectName(_fromUtf8("toolButton_image"))
        self.label_image = QtGui.QLabel(self.tab)
        self.label_image.setGeometry(QtCore.QRect(120, 60, 81, 21))
        self.label_image.setObjectName(_fromUtf8("label_image"))
        self.label_outdir = QtGui.QLabel(self.tab)
        self.label_outdir.setGeometry(QtCore.QRect(0, 150, 201, 17))
        self.label_outdir.setObjectName(_fromUtf8("label_outdir"))
        self.lineEdit_outdir = QtGui.QLineEdit(self.tab)
        self.lineEdit_outdir.setGeometry(QtCore.QRect(210, 150, 151, 21))
        self.lineEdit_outdir.setObjectName(_fromUtf8("lineEdit_outdir"))
        self.toolButton_outdir = QtGui.QToolButton(self.tab)
        self.toolButton_outdir.setGeometry(QtCore.QRect(400, 150, 23, 25))
        self.toolButton_outdir.setObjectName(_fromUtf8("toolButton_outdir"))
        self.label_config = QtGui.QLabel(self.tab)
        self.label_config.setGeometry(QtCore.QRect(50, 190, 151, 20))
        self.label_config.setObjectName(_fromUtf8("label_config"))
        self.lineEdit_confile = QtGui.QLineEdit(self.tab)
        self.lineEdit_confile.setGeometry(QtCore.QRect(210, 190, 151, 21))
        self.lineEdit_confile.setText(_fromUtf8(""))
        self.lineEdit_confile.setObjectName(_fromUtf8("lineEdit_confile"))
        self.toolButton_confile = QtGui.QToolButton(self.tab)
        self.toolButton_confile.setGeometry(QtCore.QRect(400, 190, 23, 25))
        self.toolButton_confile.setObjectName(_fromUtf8("toolButton_confile"))
        self.label_cmdlineoutput = QtGui.QLabel(self.tab)
        self.label_cmdlineoutput.setGeometry(QtCore.QRect(20, 240, 171, 17))
        self.label_cmdlineoutput.setObjectName(_fromUtf8("label_cmdlineoutput"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 270, 571, 211))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(370, 490, 231, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_bcpydir = QtGui.QLabel(self.tab)
        self.label_bcpydir.setGeometry(QtCore.QRect(5, 101, 201, 21))
        self.label_bcpydir.setObjectName(_fromUtf8("label_bcpydir"))
        self.lineEdit_bcpydir = QtGui.QLineEdit(self.tab)
        self.lineEdit_bcpydir.setGeometry(QtCore.QRect(210, 106, 151, 21))
        self.lineEdit_bcpydir.setObjectName(_fromUtf8("lineEdit_bcpydir"))
        self.toolButton_bcpydir = QtGui.QToolButton(self.tab)
        self.toolButton_bcpydir.setGeometry(QtCore.QRect(400, 100, 23, 25))
        self.toolButton_bcpydir.setObjectName(_fromUtf8("toolButton_bcpydir"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        # The standard output from this point is placed by an in-memory 
        # buffer.
        self.oldstdout = sys.stdout
        sys.stdout = StringIO()

        QtCore.QObject.connect(self.toolButton_image, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getImageFileName)

        QtCore.QObject.connect(self.toolButton_bcpydir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getbcpyDir)

        QtCore.QObject.connect(self.toolButton_outdir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getOutputDir)

        QtCore.QObject.connect(self.toolButton_confile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getConfigFile)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickedOk)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonClickedCancel)
        
        ### 2nd Tab
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        ### 3rd Tab
        ##self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        ### 4th Tab
        ##self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        ### 5th Tab
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
        print(">> Output Directory Selected ", outdir)

        self.lineEdit_outdir.setText(outdir)
        self.outputDirName = outdir

        if os.path.exists(self.outputDirName):
            raise RuntimeError(out_dir+" exists")

            self.textEdit.setText( sys.stdout.getvalue() )
            sys.stdout = self.oldstdout

            exit(1)

        os.mkdir(self.outputDirName)

    # buttonClickedOk: Routine invoked when the OK button is clicked.
    # Using StringIO (equivalent to cStringIO in Python-2.x), the stdio is
    # redirected into an in-memory buffer, which is displayed in the 
    # text window at the end.
    def buttonClickedOk(self):
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
        ret = self.bcRunCmd(cmd)

        if ret == -1 :
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

        ret = self.bcRunCmd(cmd)
        if ret == -1 :
           print(">> ERROR!!! Fiwalk terminated with error: \n", err)
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

    def bcRunCmd(self, cmd):
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("bc_Form", "Bulk Extractor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("bc_Form", "Annotated Features", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("bc_Form", "Fiwalk XML", None, QtGui.QApplication.UnicodeUTF8))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("bc_Form", "Reports", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    bc_Form = QtGui.QWidget()
    ui = Ui_bc_Form()
    ui.setupUi(bc_Form)
    bc_Form.show()
    sys.exit(app.exec_())

