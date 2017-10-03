import os
from xml.dom import minidom
from Tkinter import Tk
from tkFileDialog import askdirectory

def ParseXml():

    Tk().withdraw()                     #dont want a GUI.so keepwondow from appearing
    filesinFolder = askdirectory()      #selecting the folder with
    path = os.listdir(filesinFolder)    # list of files

    for file in path:  # looping through the files
        if file.endswith('.xml'):
            print (file)
            if os.path.abspath(file):
                findtheTag = raw_input("What tag would you like to find out?")
                xmldoc = minidom.parse(os.path.join(filesinFolder, file))
                itemlist = xmldoc.getElementsByTagName(findtheTag)
                if len(itemlist) >= 1:
                    for moreThanOneTagPresent in itemlist:
                        getTagValue = moreThanOneTagPresent.firstChild.nodeValue
                        print "The Tag is ", (getTagValue)
                else:
                    getTagValue = itemlist[0].firstChild.nodeValue
                    print "The Tag is ", (getTagValue)
                print "It occurs ", (len(xmldoc.getElementsByTagName(findtheTag))), "time\n"
            else:
                print "File doesnt exist."
        else:
            print "Not an xml file"

