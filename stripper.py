#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, urllib2


os.system("cls")

print "Oversized NC File Conversion Engine."
print "Copyright 2014 Dave Finch.\n\n"

fName = "test.nc"
oName = "dome_out.nc"
acuStr = "%.2f"

sGM = 0
sSpace = 0

def quitOnError(es, en):
    print es
    if en:
        print "I/O error({0}): {1}".format(en.errno, en.strerror)
    os._exit(0)

def stripDecimals(srcStr):
    fl = float(srcStr[1:])
    retStr = srcStr[0] + acuStr % fl
    return retStr

def stripTrailingZeros(srcStr):
    while srcStr[len(srcStr) - 1] == "0":
        srcStr = srcStr[0:len(srcStr) - 1]
    if srcStr[len(srcStr) - 1] == ".":
        srcStr = srcStr[0:len(srcStr) - 1]
    return srcStr

def shortenGMCode(srcStr):
    if len(srcStr) < 3: return srcStr
    newStr = srcStr[0] + srcStr[2:]
    return newStr

def authenticateUse():
    try:
        page = urllib2.urlopen("http://www.domain.com")
        content = page.read()
        if "dominicanhall" in content:
            return
        else:
            quitOnError("Failed to authenticate program.", 0)
    except urllib2.HTTPError as e:
        quitOnError("Failed to authenticate program.", e)

#authenticateUse()

sac = 1
while True:
    try:
        if sys.argv[sac] == "-i":
            fName = sys.argv[sac + 1]
            sac += 2
        if sys.argv[sac] == "-o":
            oName = sys.argv[sac + 1]
            sac += 2
        if sys.argv[sac] == "-a":
            if int(sys.argv[sac +1]) < 1:
                quitOnError("Error. Accuracy argument '-a' must be a positive integer.", 0)
            acuStr = "%." + sys.argv[sac + 1] + "f"
            sac += 2
    except:
        break

try:    
    inFile = open(fName, "r")
except IOError as e:
    quitOnError("Error. Can't open input file : " + fName, e)
inSize = os.path.getsize(fName)

strList = []
while True:
    strList.append(inFile.readline())
    if len(strList[len(strList)-1]) == 0: break
inFile.close()

try:
    outFile = open(oName, "w")
except IOError as e:
    quitOnError("Error creating or opening output file.", e)

print "Working....."

saveOut = 0
for line in strList:
    outStr = ""
    
    for code in line.split(" "):
        try:
            if code[0] in "XYZIJK":
                code = stripDecimals(code)
                code = stripTrailingZeros(code)
            if code[0] in "GM":
                ret = code
                code = shortenGMCode(code)
                if ret != code: sGM += 1
        except:
            pass
        outStr += code
        sSpace += 1
        
    try:
        if len(outStr) > 0:
            outFile.write(outStr)
            saveOut += 1
    except IOError as e:
        quitOnError("Error. Can't write to output file.", e)
        
outFile.close()

outSize = os.path.getsize(oName)

print "Done.\n"
print "{:,}".format(inSize), "bytes read."
print "{:,}".format(outSize), "bytes written.\n"


