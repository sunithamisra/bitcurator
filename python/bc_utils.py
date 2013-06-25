#!/usr/bin/python
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
# This is a python file containing some utility functions for
# generate_reports script

import re

reportFileList = [None]*35

def is_comment_line(line):
    if len(line)==0: return False
    if line[0:4]==b'\xef\xbb\xbf#': return True
    if line[0:1]=='\ufeff':
        line=line[1:]       # ignore unicode BOM
    try:
        if ord(line[0])==65279:
            line=line[1:]       # ignore unicode BOM
    except TypeError:
        pass
    if line[0:1]==b'#' or line[0:1]=='#':
        return True
    return False

def bc_addToReportFileList(pdf_file, PdfReport):
    try:
        reportFileList[PdfReport.reportFiles] = pdf_file
        PdfReport.reportFiles += 1
    except IndexError:
        print("Warning: Exceeded generating 100 format files") 

def bc_printReportFileList(PdfReport, FiwalkReport):
    if (FiwalkReport.noLibMagic == True):
        print("\n>>>> The XML input file has missing LibMagic information. \n" \
                ">>>> So the format reports are not generated \n")
    print("The following report files are generated: ")
    for i in range(0, PdfReport.reportFiles):
        print("%d)  %s" % (i+1, reportFileList[i])) 

#
# From fiwalk outout file, the image-information reported on the 
# top is read into the dict image_info
#
def fw_get_image_info(line1, image_info):
    for key in image_info:
        if line1[0] == key:
            image_info[key] = line1[1]
            break
        
#
# is_special_file returns True if the file starts with a dot. Other
# criteria to label it a special file can be added as needed.
#
def is_special_file(filename):
    trimmed_filename = filename.lstrip()
    if trimmed_filename[0] == '.':
        return(True)
    return(False)

def match_and_write(of, line, pattern, separator):
    if re.match(pattern,line):
        line1 = re.split(":", line.rstrip('\n'))
        of.write(bytes(line1[1], 'UTF-8')) 
        if (separator):
            of.write(b";") 
        else:
            of.write(b"\n") 

def filename_from_path(path):
    templist = str(path)
    templist = templist.split("/")
    length = len(templist)
    return(templist[length-1]) 

def dir_from_path(path):
    templist = str(path)
    templist = templist.split("/")
    length = len(templist)
    return(templist[0:length-1]) 

def stringfix(strname):
    return(re.sub('_',' ',strname.upper()))

def print_dict(FiwalkReport):
    print(" LENGTH: ", len(FiwalkReport.fiDictList))
    for index in range(len(FiwalkReport.fiDictList)):
        print("PrintDict: INDEX: filename", FiwalkReport.fiDictList[index]['filename'])
        if index == 10:
            break

def match_file_write(of, line, pattern, linenum):
        print("Fn:match_file_write:", linenum)
        if re.match("filename: ",line):
            line1 = re.split(":", line)
            of.write(bytes(line1[1], 'UTF-8')) 

# Normalizing function. Here we need just the stripping.
def normalize(s):
    #for p in string.punctuation:
        #s = s.replace(p, '')
 
    #return s.lower().strip()
    return s.strip()
#
# Function: get_file_info()
# Parses the line and populates the FiwalkReport class with the info.
#
def get_file_info(line, FiwalkReport):
    if re.match("name_type: ",line):
        line1 = re.split(":", line)
        if "r" in line1[1]:
            FiwalkReport.numfiles = FiwalkReport.numfiles + 1
        elif "d" in line1[1]:
            FiwalkReport.dirs = FiwalkReport.dirs + 1
    elif re.match("unalloc", line):
        line1 = re.split(":", line)
        if int(line1[1]) == 1:
            FiwalkReport.deletedFiles = FiwalkReport.deletedFiles + 1
    elif re.match("libmagic", line):
        line1 = re.split(":", line)
        fileformat = normalize(line1[1])

        # If fileformat is not alrady present in format array, add it
        FiwalkReport.bcAddToFmtList(FiwalkReport, fileformat)

        ## DEBUG: Print the Format Dict
        ## FiwalkReport.bcPrintFormatDict()
        ## print("FORMAT DICT ************ ")
        ## print(FiwalkReport.bcFmtDict)

    elif re.match("filesize", line):
        line1 = re.split(":", line)
        if int(line1[1]) == 0:
            FiwalkReport.emptyFiles = FiwalkReport.emptyFiles + 1
        if int(line1[1]) > 1024*1024:
            FiwalkReport.bigFiles = FiwalkReport.bigFiles + 1

# bc_get_reports: Since the report-generating functions expect parameters in the "args" form,
# the data is converted into an artificially creted args list. this is done so the command-line
# option of running the reports is intact.

from collections import namedtuple
def bc_get_reports(PdfReport, FiwalkReport, fiwalk_xmlfile, annotated_dir, outdir, config_file):

        fiwalk_txtfile = "null"
        fiwalk_xlsx = True  # By default, xlsx files are generated

        argStruct = namedtuple("argStruct", "outdir fiwalk_xmlfile annotated_dir")
        args = argStruct(outdir=outdir, fiwalk_xmlfile=fiwalk_xmlfile, annotated_dir=annotated_dir)

        use_config_file = True
        fiwalk_txtfile = None

        print(">> config_file: ", config_file)
        print(">> fiwalk_xmlfile: ", args.fiwalk_xmlfile)
        print(">> annotated Directory: ", args.annotated_dir)
        print(">> Output Directory: ", args.outdir)

        report = PdfReport(args.annotated_dir, args.outdir, use_config_file, config_file)
        report.be_process_generate_report(args, use_config_file)

        if fiwalk_txtfile:
            ###fiwalk_txtfile = args.fiwalk_txtfile
            ## print("D: Using Fiwalk TXT file ", fiwalk_txtfile)

            report_fi = FiwalkReport(fiwalk_txtfile)
            report_fi.process_generate_report_fiwalk_from_text(args)
        elif args.fiwalk_xmlfile:
            fiwalk_xmlfile = args.fiwalk_xmlfile

            ## print("D: Using Fiwalk XML file ", fiwalk_xmlfile)

            report_fi = FiwalkReport(args.fiwalk_xmlfile)
            report_fi.process_generate_report_fiwalk_from_xml(args)

        ##exit(1)

