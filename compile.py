#!/usr/bin/env python

import sys
import re
from subprocess import call

def replaceFunc(matchobj):
    return "."

def fileExtension(matchobj):
    return ".pdf"

reArgs = re.compile(r"^([^\/]*)\/(.+)$")
reReplace = re.compile(r"/")
reFileExt = re.compile(r".md")

args = re.search(reArgs, sys.argv[1])
folder = args.group(1)
fileName = re.sub(reReplace, replaceFunc, args.group(2))
fileName = re.sub(reFileExt, fileExtension, fileName)
outputFile = "%s/%s" % (folder, fileName)

call(["hermes", sys.argv[1], outputFile])