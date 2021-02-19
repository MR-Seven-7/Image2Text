from random import randint
import cv2 as cv
from time import sleep
import numpy
from pyperclip import copy

def rescale(frame, width, height):
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

path = input("Enter Path of the Image : ")
iwidth = int(input("Enter Width of the Image : "))
iheight = int(input("Enter Height of the Image : "))
print("This takes some time!")
print("Please wait while processing...")
EMINEM_grayscale = rescale(cv.imread(path, 0), iwidth, iheight)
ilen = (iwidth * iheight) + iheight
print(ilen)
img_str = ""
symbols_list = ''' _-`.,*'"<>{}[]!^()@#$%|abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVYZXW'''
symbols = ""
for i in range(len(symbols_list)):
    symbols += symbols_list[-(i + 1)]
shade_symbols = {}
invert_shade_symbols = {}
complexity = 1
invert_img = ""
erect_img = ""
for row in EMINEM_grayscale:
    invert_img += "\n"
    erect_img += "\n"
    for col in row:
        print(str(round((len(erect_img)/ilen)*100, 2)) + " %")
        if shade_symbols.get(col//complexity) == None:
            shade_symbols[col//complexity] = symbols[col//len(symbols)]
            symbols.replace(shade_symbols[col//complexity], "")
        erect_img += shade_symbols[col//complexity]

        if invert_shade_symbols.get(col//complexity) == None:
            invert_shade_symbols[col//complexity] = symbols_list[col//len(symbols)]
            symbols_list.replace(shade_symbols[col//complexity], "")
        invert_img += invert_shade_symbols[col//complexity]


img_str = erect_img + "\n\n\n\n\n\n\n\n\n\n\n\n" + invert_img
copy(img_str)
print("Done")