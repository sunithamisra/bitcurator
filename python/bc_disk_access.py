#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# bc_disk_access --dfxmlfile <file> --filename <oufile>
#
# Ex: Cat: 
# python3 bc_disk_access.py --image ~/aaa/charlie-work-usb-2009-12-11.aff \ 
#   --dfxmlfile ~/aaa/charlie_xml --filename \
#    Email/Charlie_2009-12-04_0941_Sent.txt --cat
#
# Ex: filelist:
# SILS-SUNITHA:$ python3 bc_disk_access.py 
#    --image ~/aaa/charlie-work-usb-2009-12-11.aff 
#    --dfxmlfile ~/aaa/charlie_xml \
#    --listfiles
# 

import os, fiwalk, sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from argparse import ArgumentParser
except ImportError:
    raise ImportError("This script requires ArgumentParser which is in Python 2.7 or Python 3.0")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## app = QtGui.QApplication(sys.argv)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# init widgets

global g_model
global g_image
global g_dfxmlfile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(540, 565)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.DirectoryTree = QtGui.QTreeView(self.centralwidget)
        self.DirectoryTree.setGeometry(QtCore.QRect(10, 40, 521, 401))
        self.DirectoryTree.setObjectName(_fromUtf8("DirectoryTree"))

        self.DirectoryTree.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.model = QtGui.QStandardItemModel()
        self.DirectoryTree.setModel(self.model)
        self.DirectoryTree.setUniformRowHeights(True)
        global g_model 
        g_model = self.model

        g_model.setHorizontalHeaderLabels(['File Structure'])

        self.pushButton_export = QtGui.QPushButton(self.centralwidget)
        self.pushButton_export.setGeometry(QtCore.QRect(420, 460, 98, 27))
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(290, 460, 98, 27))
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionDeSelect_All = QtGui.QAction(MainWindow)
        self.actionDeSelect_All.setObjectName(_fromUtf8("actionDeSelect_All"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionSelect_All)
        self.menuHelp.addAction(self.actionDeSelect_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionExit.triggered.connect(self.exitMenu)
        self.actionSelect_All.triggered.connect(self.selectAllMenu)
        self.actionDeSelect_All.triggered.connect(self.deSelectAllMenu)

        # File navigation for Export
        QtCore.QObject.connect(self.pushButton_export, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedExport)

        # Handle the Close button
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickedClose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exitMenu(self):
        QtCore.QCoreApplication.instance().quit()

    def selectAllMenu(self):
        BcFileStructure.bcCheckAllFiles(BcFileStructure, 1, None)
        
    def deSelectAllMenu(self):
        BcFileStructure.bcCheckAllFiles(BcFileStructure, 0, None)

    def buttonClickedClose(self):
        QtCore.QCoreApplication.instance().quit()

    def buttonClickedExport(self):
        # First navigate through file menu to choose the directory
        exportDir = QtGui.QFileDialog.getSaveFileName()

        print(">> Output Directory Selected: ", exportDir)
        
        # Now loop through the checked files and dump them in this directory
        BcFileStructure.bcCheckAllFiles(BcFileStructure, 2, exportDir)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Disk Image Access Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_export.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeSelect_All.setText(QtGui.QApplication.translate("MainWindow", "DeSelect All", None, QtGui.QApplication.UnicodeUTF8))


class BcFileStructure:

    acc_dict_array = ["filename", "partition", "inode", "name_type", "filesize"]
    fiDictList = []
    parentlist = []
    file_item_of = dict()
    path_of = dict()
    
    # bcCheckAllFiles()
    # Iterate through the leaves of the file structure and check/uncheck
    # all the files based on whether "check" is True or False.
    # This same routine is reused with the parameter "cehck" set to 2, 
    # to dump the contents of the "checked" files to the specified output 
    # directory. 
    def bcCheckAllFiles(self, check, exportDir):
        ## print(">>D: LENGTH of fiDictList: ", len(self.fiDictList))
        for i in range(0, len(self.fiDictList) - 1):
            path = self.fiDictList[i]['filename']
            if self.fiDictList[i]['name_type'] == 'd':
                isdir = True
            else:
                isdir = False
            pathlist = path.split('/')
            pathlen = len(pathlist)
            ## print("D: Path LiSt: ", pathlist, len(pathlist))
            ## print("D: =================")
            last_elem = pathlist[pathlen-1]
            if last_elem == "." or last_elem == "..":
                # Ignore . and ..
                continue 

            if isdir == False:
                # First get the name of the current file
                current_fileordir = pathlist[pathlen-1]

                # Now using the dict of files, file_item_of, get the item 
                # for this file
                current_item = self.file_item_of[current_fileordir]
                if check == 1:
                    ## print("D: Setting File to Checked_state ", current_fileordir) 
                    current_item.setCheckState(2)
                elif check == 0:
                    current_item.setCheckState(0)
                elif check == 2:
                    # If "check" is 2, we use this routine to dump the 
                    # contents of the specified file to the specified output
                    # file. 
                    # If this file is "checked", download its contents.
                    # item.checkState has 0 if not checked, 1 if partially
                    # checked and 2 if checked. 
                    # http://qt.developpez.com/doc/4.6/qt/#checkstate-enum

                    if current_item.checkState() == 2:
                        ## print(">> D: File %s is Checked" %current_fileordir)
                        if not os.path.exists(exportDir):
                            os.mkdir(exportDir)
                        pathlist = path.split('/')
                        oldDir = newDir = exportDir
                        
                        # Iterate through the path list and make the directories
                        # in the path, if they don't already exist.
                        for k in range(0, len(pathlist)-1):
                            newDir = oldDir + '/' + pathlist[k]
                            print("pathlisg-k = {0}, path-k: {1}, Dir: {2} ".format(k, pathlist[k], newDir))
                            if not os.path.exists(newDir):
                                os.mkdir(newDir)
                            oldDir = newDir
                        outfile = newDir + '/'+current_fileordir
                        ## print(">> D: Writing to Outfile: ", outfile, path)
                        
                        filestr.bcCatFile(path, g_image, g_dfxmlfile, True, outfile)
                    #else:
                        #print("File %s is NOT Checked" %current_fileordir)

    # bcExtractFileStr()
    # This routine extracts the file structure given a disk image and the
    # corresponding dfxml file.
    def bcExtractFileStr(self, image, dfxmlfile, outfile):
        # Extract the information from dfxml file to create the 
        # dictionary only if it is not done before.
        if len(self.fiDictList) == 0:
            self.bcProcessDfxmlFileUsingSax(dfxmlfile)
            ## print("D: Length of dictionary fiDictList: ", len(self.fiDictList))

        parent0 = QtGui.QStandardItem('Disk Image: {}'.format(image))
        current_fileordir = image
        parent_dir_item = parent0

        global g_image
        global g_dfxmlfile
        g_image = image
        g_dfxmlfile = dfxmlfile

        # A dictionary item_of{} is maintained which contains each file/
        # directory and its corresponding " tree item" as its value.
        item_of = dict()
        item_of[image] = parent0

        for i in range(0, len(self.fiDictList) - 1):
            path = self.fiDictList[i]['filename']
            if self.fiDictList[i]['name_type'] == 'd':
                isdir = True
            else:
                isdir = False
            pathlist = path.split('/')
            pathlen = len(pathlist)
            ## print("D: Path LiSt: ", pathlist, len(pathlist))
            ## print("D: =================")
            last_elem = pathlist[pathlen-1]
            if last_elem == "." or last_elem == "..":
                # Ignore . and ..
                continue 

            if isdir == True:
                if (pathlen < 2):
                    # If pathlen is < 2 it is a file/dir directly off the root.
                    parent = parent0
                else:
                    parent = item_of[pathlist[pathlen-2]]

                current_dir = pathlist[pathlen-1]
                ## print("D: Set Current_dir to: ", current_dir)
                current_dir_item = QtGui.QStandardItem(current_dir)
                parent_dir_item.appendRow(current_dir_item)
             
                # Save the item of this directory
                item_of[current_dir] = current_dir_item
            else:
                # File: The file could be in any level - top level is the
                # child of parent0 (disk img). The level is sensed by the
                # pathlen 
                current_fileordir = pathlist[pathlen-1]
                current_item = QtGui.QStandardItem(current_fileordir)
                current_item.setCheckable(True)
                current_item.setCheckState(0)

                # save the "item" of each file
                self.file_item_of[current_fileordir] = current_item

                ## print("D: Adding child to parent: ", pathlist[pathlen-2], parent0)

                if pathlen > 1:
                    parent_dir_item = item_of[pathlist[pathlen-2]]
                else:
                    parent_dir_item = parent0
            
                parent_dir_item.appendRow(current_item)

            parent = parent_dir_item
            global g_model
            g_model.appendRow(parent)
            
    def bcCatFile(self, filename, image, dfxmlfile, redirect_file, outfile):
        # Traverse the XML file, get the file_name, extract the inode number
        # of the file and run icat to extract the data.
        ## print(">>D: bcCatFile: Filename: ", filename)
        ## print(">>D: bcCatFile: image: ", image)
        ## print(">>D: bcCatFile: dfxmlfile: ", dfxmlfile)
        ## print(">>D: bcCatFile: outfile: ", outfile)

        # First traverse through dfxmlfile to get the block containing "filename"
        # to extract the inode. Do this just once.

        if len(self.fiDictList) == 0:
            self.bcProcessDfxmlFileUsingSax(dfxmlfile)
            print("D: Length of fiDictList ", len(self.fiDictList))

        # Dictionary is formed. Now traverse through the array and 
        # in each dictionary, get the inode and call iCat command.
        for i in range(0, len(self.fiDictList)-1):
            if (self.fiDictList[i]['filename'] == filename):
                ## print("D: Extracting the contents of the file:inode ", \ 
                ##                  filename, self.fiDictList[i]['inode']) 
                # First get the offset of the 2nd partition using mmls cmd
                # ex: mmls -i aff ~/aaa/jo-favorites-usb-2009-12-11.aff
                if image.endswith(".E01") or image.endswith(".e01"):
                    imgtype = 'ewf'
                elif image.endswith(".aff") or image.endswith(".AFF"):
                    imgtype = 'aff'
                mmls_cmd = "mmls -i " + imgtype +" "+image +" | grep \"02:\""

                ## print("D: Executing mmls command: ", mmls_cmd) 
                f = os.popen(mmls_cmd)
                part2 = f.read()
                ## print("D: Extracting partition-2: ", part2)

                part2_list = part2.split()
                part2_start = part2_list[2]

                ## print("D: Start offset of Partition-2: ", part2_start)
                ## icat_cmd ex: icat -o 1 ~/aaa/charlie-work-usb-2009-12-11.aff 130 
                outfile = outfile.replace("$", "\$")

                # redirect_file is set to True if the contents need to be 
                # written to a file.
                if (redirect_file == True):
                    icat_cmd = "icat -o "+part2_start+ " "+ image + " " + self.fiDictList[i]['inode'] + ' > ' + outfile
                    ## print(">> D: Executing iCAT command: ", icat_cmd)
                    f2 = os.popen(icat_cmd)
                    print(">> Writing to file ", outfile)
                else:
                    icat_cmd = "icat -o "+part2_start+ " "+ image + " " + self.fiDictList[i]['inode']
                    ## print(">> D: Executing iCAT command: ", icat_cmd)
                    f2 = os.popen(icat_cmd)
                    icat_out = f2.read()
                    print(">>> Contents of file :", filename)
                    print(icat_out)
                return
 
    def cb(self, fi):
        self.fiDictList.append({self.acc_dict_array[0]:fi.filename(), \
                           self.acc_dict_array[1]:fi.partition(), \
                           self.acc_dict_array[2]:fi.inode(), \
                           self.acc_dict_array[3]:fi.name_type(), \
                           self.acc_dict_array[4]:fi.filesize() })

        
    def bcProcessDfxmlFileUsingSax(self, dfxmlfile):
        fiwalk.fiwalk_using_sax(xmlfile=open(dfxmlfile, 'rb'),callback=self.cb)
       

if __name__=="__main__":
    import sys, time, re

    parser = ArgumentParser(prog='bc_disk_access.py', description='File Access')
    parser.add_argument('--image', action='store', help="Image file ")
    parser.add_argument('--dfxmlfile', action='store', help="DFXML file ")
    parser.add_argument('--cat',action='store_true',help='list contents ')
    parser.add_argument('--listfiles',action='store_true',help='list file structure ')
    parser.add_argument('--filename',action='store',help='File name to list contents of ')
    parser.add_argument('--outfile',action='store',help='Output File ')

    args = parser.parse_args()

    print("D: dfxmlfile: ", args.dfxmlfile)
    print("D: cat: ", args.cat)
    print("D: listfiles: ", args.listfiles)
    print("D: filename: ", args.filename)
    print("D: output file", args.outfile)
    # FIXME: If dfxmlfile not given, this should run the fiwalk cmd to
    # extract the dfxml file

    filestr = BcFileStructure()


    # The following call is just to test bcCatFile, giving a filename
    # from the dfxml file. In reality, it will be invoked from a click on 
    # a file in the web browser.
    if (args.cat == True):
        if args.filename == None or args.dfxmlfile == None:
            print(">> Filename or dfxml file not provided. Exiting")
            exit(0) 

        if not os.path.exists(args.dfxmlfile):
            print(">> File %s doesnot exist " %args.dfxmlfile) 
            exit(0)

        filestr.bcCatFile(args.filename, args.image, args.dfxmlfile, False, None)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # expand third container
    ## parent0 = BcFileStructure.bcExtractFileStr.parent0
    ## index = model.indexFromItem(parent0)
    ## view.expand(index)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # select last row
    ## selmod = view.selectionModel()
    #index2 = model.indexFromItem(child3)
    ## index2 = model.indexFromItem(parent0)
    ## selmod.select(index2, QtGui.QItemSelectionModel.Select|QtGui.QItemSelectionModel.Rows)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if (args.listfiles == True):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        filestr.bcExtractFileStr(args.image, args.dfxmlfile, args.outfile)
        MainWindow.show()
        sys.exit(app.exec_())

