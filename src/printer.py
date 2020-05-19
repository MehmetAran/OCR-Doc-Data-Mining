
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import os
def replaceText(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
        
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

"""
basePath = os.path.abspath('.')
path = "C:\\Users\\warri\\Desktop\\computerscience\\CodeFolder\\OCR-Doc-Data-Mining\\resource\\txt-docs\\test.txt"
pattern = "Öğrenci No :"
susbt = pattern +" "+ "10099"
replaceText(path,pattern,susbt)
"""

def replaceText2(path):
    fin = open(path, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('pyton', 'python')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("data.txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()