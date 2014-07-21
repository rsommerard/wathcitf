#!/usr/bin/Python3
#
#   Wathcitf script : What are the hexa colors in this file ?
#
#   Romain SOMMERARD
#   Distributed under the GPL version 3 licence.
#
#   Search all hexa colors in the css file.
#   Script for Linux system.
#
#   Don't use the ~ in the FOLDER_PATH !
#
#   Usage:  Replace the PATH_FILE by the path of
#           your file name and run this script.
#
#   Example of configuration: 	FOLDER_PATH='../Downloads/FolderCss/'
#				FILE_NAME='theme.css'
#
#   Syntax: 	# Python3 wathcitf
#
#		OR
#
#               If python 3 is the only version of python in your computer.
#		# Python wathcitf
#
#		OR
#
#               You can run the script like application.
#		# chmod +x wathcitf
#               # ./wathcitf
#

import re
import os


# The path of folder where is the file. Don't use the ~ !
FOLDER_PATH = ''

# The css file name.
FILE_NAME = ''


if FILE_NAME == '' or (FOLDER_PATH == '' and FILE_NAME == ''):
    print('Error: FILE_NAME or/and FOLDER_PATH empty')
    exit(1)

colors = set()

expression = r'(.*)(#[0-9a-fA-F]{3,6})(.*)'

if FOLDER_PATH != '':
    os.chdir(FOLDER_PATH)

try:
    with open(FILE_NAME, 'r') as file:
        for line in file:
            color = re.match(expression, line)
            if color:
                colors.add(color.group(2))
except FileNotFoundError:
    print('Error: File not found (',FOLDER_PATH,FILE_NAME,')',sep='')
    exit(1)

for color in colors:
    print(color)
