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

class BcPremisFile:

    # The first block of disk-image object 
    def bcPremisGenXmlObject(self, root, dfxmlfile, image_name):
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
    def extractImageName(self, dfxml_command_line):
        # Command_line text looks like this:
        # <command_line>fiwalk -f -X <pathToXml> <pathToImage>.aff</command_line>
        templist = dfxml_command_line.split(" ")
        print("command_line as list: ", templist[0], templist[1], \
               templist[2], templist[3], templist[4])
        return templist[4]

    # Generate premix XML code for Fiwalk event
    def bcGenPremisXmlFiwalk(self, dfxmlfile, premis_file, outcome=True):
    
        # If dfxmlfile doesn't exist, Fiwalk command probably failed.
        # If outcome is False, it is confirmed to have failed.
        # Generate premis event accordingly.
        # FIXME: Add premis event for failed case here.

        # First check if the premis file exists. If not, create a new one.
        print("D: bcGenPremisXmlFiwalk: XmlFile: ", dfxmlfile)
        print("D: bcGenPremisXmlFiwalk: Premis file: ", premis_file)
        if os.path.exists(premis_file):
            of_premis = open(premis_file,"ab")
        else:
            of_premis = open(premis_file,"wb")

        # Get the image name from "command_line" part of dfxml file:
        dfxml_command_line = fiwalk.fiwalk_xml_command_line(dfxmlfile)
        image_name = self.extractImageName(dfxml_command_line)
        
        # create XML 
        root = etree.Element("premis")
        
        # Generate the disk image Object segment 
        self.bcPremisGenXmlObject(root, dfxmlfile, image_name)

        # Generate the Fiwalk Event:
        event = etree.SubElement(root, 'event')
        root.append(event)
        eventIdentifier = etree.SubElement(event, "eventIdentifier")
        event.append(eventIdentifier)

        eventIdentifierType = etree.SubElement(eventIdentifier, "eventIdentifierType")
        eventIdentifierType.text = str(uuid.uuid1())
        eventIdentifier.append(eventIdentifierType)
     
        eventIdentifierValue = etree.SubElement(eventIdentifier, "eventIdentifierValue")
        eventIdVal = dfxml_command_line
        eventIdentifierValue.text = eventIdVal
        eventIdentifier.append(eventIdentifierValue)

        eventType = etree.SubElement(event, "eventType")
        eventType.text = "File System Analysis"
        event.append(eventType)

        eventDateTime = etree.SubElement(event, "eventDateTime")
        eventDateTime.text = fiwalk.fiwalk_xml_start_time(dfxmlfile)
        event.append(eventDateTime)

        eventOutcomeInformation = etree.SubElement(event, "eventOutcomeInformation")
        event.append(eventOutcomeInformation)

        eventOutcome = etree.SubElement(eventOutcomeInformation, "eventOutcome")
        if (outcome == True):
            eventOutcome.text = "Fiwalk Success" 
        else:
            eventOutcome.text = "Fiwalk Failure" 
        eventOutcomeInformation.append(eventOutcome)

        eventOutcomeDetail = etree.SubElement(eventOutcomeInformation, "eventOutcomeDetail")
        eventOutcomeDetail.text = "DFXML File: " + dfxmlfile
        eventOutcomeInformation.append(eventOutcomeDetail)

        # pretty string: 
        #s = etree.tostring(root, pretty_print=True)
        s = etree.tounicode(root, pretty_print=True)

        # FIXME: Printing the tree during development phase. Remove later.
        print(s)
        of_premis.write(bytes(s, 'UTF-8'))

    ##def bcGenPremisXmlBulkExtractor(self, reportsFile, premis_file):
        
if __name__=="__main__":
    import sys, time, re

    parser = ArgumentParser(prog='bc_premis_genxml.py', description='Generate PREMIS XML file for BitCurator events')
    parser.add_argument('--dfxmlfile', action='store', help="DFXML file ")
    parser.add_argument('--bulk_extractor', action='store', help=" Bulk-extrator Report file ")
    parser.add_argument('--premis_file',action='store',help='Output Premis File; Concatinates if exists')

    args = parser.parse_args()
   
    print("D: dfxmlfile: ", args.dfxmlfile)
    print("D: output premis file", args.premis_file)

    premis = BcPremisFile()
    premis.bcGenPremisXmlFiwalk(args.dfxmlfile, args.premis_file)


    



