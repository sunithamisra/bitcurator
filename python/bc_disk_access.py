#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# disk_access --dfxmlfile <file> --filename <oufile>
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
#    --filename Email/Charlie_2009-12-04_0941_Sent.txt --listfiles
# 

import os, fiwalk, sys
from PyQt4 import QtCore, QtGui

try:
    from argparse import ArgumentParser
except ImportError:
    raise ImportError("This script requires ArgumentParser which is in Python 2.7 or Python 3.0")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = QtGui.QApplication(sys.argv)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# init widgets
view = QtGui.QTreeView()
view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
model = QtGui.QStandardItemModel()
##model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
view.setModel(model)
view.setUniformRowHeights(True)

class BcFileStructure:

    acc_dict_array = ["filename", "partition", "inode", "name_type", "filesize"]
    fiDictList = []
    parentlist = []
    

    def bcExtractFileStr(self, image, dfxmlfile, outfile):
        self.bcProcessDfxmlFileUsingSax(dfxmlfile)
        print("D: Length of dictionary fiDictList: ", len(self.fiDictList))
        parent0 = QtGui.QStandardItem('Disk Image: {}'.format(image))
        current_fileordir = image
        parent_dir_item = parent0

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
                ## print("D: FILE = ", pathlist[pathlen-1])
                ## print("D: PARENT: Pathlen ", pathlist[pathlen-2], pathlen)
                current_fileordir = pathlist[pathlen-1]
                current_item = QtGui.QStandardItem(current_fileordir)
                current_item.setCheckable(True)
                ## print("D: Adding child to parent: ", pathlist[pathlen-2], parent0)

                if pathlen > 1:
                    parent_dir_item = item_of[pathlist[pathlen-2]]
                else:
                    parent_dir_item = parent0
            
                parent_dir_item.appendRow(current_item)

            parent = parent_dir_item
            model.appendRow(parent)
            
    def bcCatFile(self, filename, image, dfxmlfile):
        # Traverse the XML file, get the file_name, extract the inode number
        # of the file and run icat to extract the data.
        print("bcCatFile: Filename: ", filename)
        print("bcCatFile: image: ", image)
        print("bcCatFile: dfxmlfile: ", dfxmlfile)

        # First traverse through fdxmlfile to get the block containing "filename"
        # to extract the inode.

        self.bcProcessDfxmlFileUsingSax(dfxmlfile)
        ## print("D: Length of fiDictList ", len(self.fiDictList))

        # Dictionary is formed. Now traverse through the array and 
        # in each dictionary, get the inode and call iCat command.
        for i in range(0, len(self.fiDictList)):
            if (self.fiDictList[i]['filename'] == filename):
                print("D: Extracting the contents of the file:inode ", filename,
                                           self.fiDictList[i]['inode']) 
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
                icat_cmd = "icat -o "+part2_start+ " "+ image + " " + self.fiDictList[i]['inode']
                print("D: Executing iCAT command: ", icat_cmd)

                f2 = os.popen(icat_cmd)
                icat_out = f2.read()
                print(">>> Contents of file :", filename)
                print(icat_out)
 
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

    parser = ArgumentParser(prog='bc_premis_genxml.py', description='Generate PREMIS XML file for BitCurator events')
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

        filestr.bcCatFile(args.filename, args.image, args.dfxmlfile)

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
        filestr.bcExtractFileStr(args.image, args.dfxmlfile, args.outfile)

        view.show()
        sys.exit(app.exec_())

    
