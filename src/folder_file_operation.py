import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import cv2
from PIL import Image
import math
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import os

def pdf_to_jpeg(filepath,outpath):
    base=os.path.basename(filepath)
    pages = convert_from_path(filepath, dpi=200)
    for idx,page in enumerate(pages):
        page.save(outpath +"/"+ os.path.splitext(base)[0]+"_"+str(idx)+'.jpg', 'JPEG')
        page_idx = 0
        page = pages[page_idx]

def delete_all_files_in_folder(folderPath) : 
    filelist = [ f for f in os.listdir(folderPath)  ]
    for f in filelist:
        os.remove(os.path.join(folderPath, f))
        
def delete_file_in_folder(filePath) :
    os.remove(os.path.join(filePath))


def all_files_in_folder(folderpath):
    files = []
    for r, d, f in os.walk(folderpath):
        for file in f:
                files.append(os.path.join(r, file))

    return files

    
    

def long_slice(image_path, out_name, outdir, slice_size):
    base=os.path.basename(image_path)

    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  

        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir +"/"+ os.path.splitext(base)[0] + out_name + "_" + str(count)+".jpg"))
        count +=1


def returnStringReadFile(fileName):
    strings = []
    f = open(fileName, "r",encoding='UTF-8')
    for x in f:
        strings.append(x.replace("\n",""))
    return strings

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w',encoding="utf-8") as new_file:
        with open(file_path,encoding="utf-8") as old_file:
            for line in old_file:
                
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)