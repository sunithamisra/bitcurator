#!/usr/bin/python3
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
# bc_premis_genxml.py
#
# Generate XML tree for premis events
#

import os, fiwalk, uuid, sys
import lxml.builder as lb
from lxml import etree
try:
    from argparse import ArgumentParser
except ImportError:
    raise ImportError("This script requires ArgumentParser which is in Python 2.7 or Python 3.0")

global root
root = "null"

class BcPremisFile:

    # The first block of disk-image object 
    ##def bcPremisGenXmlObject(self, root, image_name):
    def bcPremisGenXmlObject(self, image_name):
        global root
        object1 = etree.SubElement(root, 'object')
        root.append(object1)

        objectIdentifier = etree.SubElement(object1, "objectIdentifier")
        object1.append(objectIdentifier)

        objectIdentifierType = etree.Element('objectIdentifierType')
        objectIdentifierType.text = str(uuid.uuid1())
        objectIdentifier.append(objectIdentifierType)

        objectIdentifierValue = etree.Element('objectIdentifierValue')
        objectIdentifierValue.text = image_name
        objectIdentifier.append(objectIdentifierValue)

    # Extract the image_name from the dfxml line "command_line"
    def extractImageName(self, dfxml_command_line, dfxml_type):
        # Command_line text looks like this for fiwalk dfxml:
        # <command_line>fiwalk -f -X <pathToXml> <pathToImage>.aff</command_line>
        # it looks like the following for BE reports dfxml:
        # <command_line>cmd/bulk_extractor <image>.aff -o <path_to_eDir></command_line>
        templist = dfxml_command_line.split(" ")
        if (dfxml_type == "fw"):
            # print("D: command_line as list: ", templist[4])
            return templist[4]
        elif dfxml_type == "be":
            # print("D: command_line as list: ", templist[2] )
            return templist[2]

    def bcGenPremisEvent(self, root, eIdType, eIdVal, eType, eDateTime, eOutcome, eoDetail, of_premis, write_to_file = True):
        # Generate the Event:
        event = etree.SubElement(root, 'event')
        root.append(event)
        eventIdentifier = etree.SubElement(event, "eventIdentifier")
        event.append(eventIdentifier)

        eventIdentifierType = etree.SubElement(eventIdentifier, "eventIdentifierType")
        # Use UUID generation if eIDType is set to 0
        if (eIdType == 0):
            eventIdentifierType.text = str(uuid.uuid1())
        else:
            eventIdentifierType.text = str(eIdType)

        eventIdentifier.append(eventIdentifierType)
     
        eventIdentifierValue = etree.SubElement(eventIdentifier, "eventIdentifierValue")
        eventIdentifierValue.text = eIdVal
        eventIdentifier.append(eventIdentifierValue)

        eventType = etree.SubElement(event, "eventType")
        eventType.text = eType
        event.append(eventType)

        eventDateTime = etree.SubElement(event, "eventDateTime")
        eventDateTime.text = eDateTime

        event.append(eventDateTime)
        eventOutcomeInformation = etree.SubElement(event, "eventOutcomeInformation")
        event.append(eventOutcomeInformation)

        eventOutcome = etree.SubElement(eventOutcomeInformation, "eventOutcome")
        eventOutcome.text = eOutcome
        eventOutcomeInformation.append(eventOutcome)

        eventOutcomeDetail = etree.SubElement(eventOutcomeInformation, "eventOutcomeDetail")
        eventOutcomeDetail.text = eoDetail
        eventOutcomeInformation.append(eventOutcomeDetail)

        # pretty string: 
        s = etree.tounicode(root, pretty_print=True)
        
        ## print(s)
        if (write_to_file == True):
            of_premis.write(bytes(s, 'UTF-8'))
 
    # Generate Object and event parts for the disk image
    def bcGenPremisXmlDiskImage(self, image_name, premis_image_info, premis_file):
        # First check if the premis file exists. If not, create a new one.
        ## print("D: bcGenPremisXmlDiskImage: Image: ", image_name)
        ## print("D: bcGenPremisXmlDiskImage: Premis file: ", premis_file)
        if os.path.exists(premis_file):
            of_premis = open(premis_file,"ab")
        else:
            of_premis = open(premis_file,"wb")

        # create XML 
        global root
        root = etree.Element("premis")
        
        # Generate the disk image Object segment 
        self.bcPremisGenXmlObject(image_name)

        # Generate the disk image event segment
        eventIdType = 0  # UUID
        if image_name.endswith(".aff"):
            eventIdVal = "affinfo "+image_name
        elif image_name.endswith(".E01"):
            eventIdVal = "E01"+image_name
        else:
            eventIdVal = image_name

        eventType = "Capture"
        eDateTime = premis_image_info['acq_date']
        eoDetail = 'Version: '+ str(premis_image_info['version']) + ', Image size: '+ str(premis_image_info['imagesize'])
        if image_name.endswith(".aff"):
            eOutcome = "AFF"
        elif image_name.endswith(".E01"):
            eOutcome = "E01"
        else:
            eOutcome = "Unknown image type"

        ## print("D: Geenrating disk image Event: ", root, image_name)

        self.bcGenPremisEvent(root, eventIdType, eventIdVal, eventType, eDateTime, eOutcome, eoDetail, of_premis)
        return root

    # Generate premix XML code for Fiwalk event
    def bcGenPremisXmlFiwalk(self, dfxmlfile, premis_file, outcome=True):
    
        # If dfxmlfile doesn't exist, Fiwalk command probably failed.
        # If outcome is False, it is confirmed to have failed.
        # Generate premis event accordingly.
        # FIXME: Add premis event for failed case here.

        # First check if the premis file exists. If not, create a new one.
        ## print("D: bcGenPremisXmlFiwalk: XmlFile: ", dfxmlfile)
        ## print("D: bcGenPremisXmlFiwalk: Premis file: ", premis_file)
        if os.path.exists(premis_file):
            of_premis = open(premis_file,"ab")
        else:
            of_premis = open(premis_file,"wb")

        # Get the image name from "command_line" part of dfxml file:
        dfxml_command_line = fiwalk.fiwalk_xml_command_line(dfxmlfile)
        image_name = self.extractImageName(dfxml_command_line, "fw")
        
        '''
        if root == "null":
            # create XML 
            root = etree.Element("premis")
        
            # Generate the disk image Object segment 
            self.bcPremisGenXmlObject(root, dfxmlfile, image_name)
        '''
        # Generate the Fiwalk Event:
        eventIdType = 0  # UUID
        eventIdVal = dfxml_command_line
        eDateTime = fiwalk.fiwalk_xml_start_time(dfxmlfile)
        eoDetail = "DFXML File: " + dfxmlfile
        if (outcome == True):
            eOutcome = "Fiwalk Success" 
        else:
            eOutcome = "Fiwalk Failure" 

        print(">> Generating Premis Event: ", root, dfxmlfile)

        self.bcGenPremisEvent(root, eventIdType, eventIdVal,  "File System Analysis", eDateTime, eOutcome, eoDetail, of_premis)
        return root

    def bcGenPremisXmlBulkExtractor(self, beReportFile, premis_file, isFirstEvent=False):

        ## print("D: bcGenPremisXmlBulkExtractor: XmlFile: ", beReportFile)
        ## print("D: bcGenPremisXmlBulkExtractor: Premis file: ", premis_file)

        # Extract some values from the corresponding input XML file
        beReportXml_command_line = fiwalk.fiwalk_xml_command_line(beReportFile)

        image_name = self.extractImageName(beReportXml_command_line, "be")
        be_version = fiwalk.fiwalk_xml_version(beReportFile)

        # Check if this is the first event in the xml file. If so, create the
        # root and the header part of the xml file.
        # FIXME: Revisit isFirstEvent part after making root a global var.

        '''
        if (isFirstEvent == True):
            # create XML 
            # Generate the disk image Object segment 
            self.bcPremisGenXmlObject(image_name)
           
            # The output XML file has to be new: IOW can't be appended
            # to an existing one. If it already exists, flag error
            if os.path.exists(premis_file):
                print(">>> Error: File exists. This cannot be the first event")
                return
            else: 
                # Open the new premis file for writing.
                of_premis = open(premis_file,"wb")
        else:
            # The header and root exist. So append to an existing xml file. 
            of_premis = open(premis_file,"ab")
            root = etree.Element("premis")
        '''
        of_premis = open(premis_file,"ab")
        root = etree.Element("premis")

        print(">>> Generating Bulk Extractor Premis Events XML ")

        eventIdType = 0  # If this is 0, we will generate UUID
        eventIdVal = beReportXml_command_line
        eventType = "Feature Stream Analysis"
        eDateTime = fiwalk.fiwalk_xml_start_time(beReportFile)

        # FIXME: Need more input on what to extract for Details
        eoDetail = "version: "+be_version

        # We don't check the flag for eOutcome as we don't run the 
        # bulk extractor on command line. We already have th feature files
        # from a previous run of the beViewer. We just use the information from
        # the report.xml file for generating premis events.
        eOutcome = "Bulk Extractor Output" 

        self.bcGenPremisEvent(root, eventIdType, eventIdVal,  eventType, eDateTime, eOutcome, eoDetail, of_premis)
        
    def bcGenPremisXmlAllReports(self, dfxmlfile, premis_file):
        print("Generating Fiwalk Premis Events XML ")
        bcGenPremisXmlFiwalk(self, dfxmlfile, premis_file, outcome=True)
        bcGenPremisXmlBulkExtractor(self, reportsFile, premis_file, outcome=True)
        
class XMLDone(Exception):
    def __init__(self,value):
        self.value = value

if __name__=="__main__":
    import sys, time, re

    parser = ArgumentParser(prog='bc_premis_genxml.py', description='Generate PREMIS XML file for BitCurator events')
    parser.add_argument('--dfxmlfile', action='store', help="DFXML file ")
    parser.add_argument('--bulk_extractor', action='store', help=" Bulk-extrator Report file ")
    parser.add_argument('--Allreports', action='store', help=' All Reports')
    parser.add_argument('--premis_file',action='store',help='Output Premis File; Concatinates if exists')

    args = parser.parse_args()
   
    print("D: dfxmlfile: ", args.dfxmlfile)
    print("D: output premis file", args.premis_file)

    premis = BcPremisFile()

    '''
    if (args.bulk_extractor):
        bcGenPremisXmlBulkExtractor(self, reportsFile, premis_file, outcome=True)
    '''
        
    premis.bcGenPremisXmlFiwalk(args.dfxmlfile, args.premis_file)

