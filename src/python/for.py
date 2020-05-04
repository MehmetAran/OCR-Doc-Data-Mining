"""
import folder_file_operation as ffo
import pytesseract
from docx import Document
from docx2pdf import convert
document = Document('demo.docx')
document.save("demo.docx")
document.add_heading("deneme",1)
convert("demo.docx", "./documents/demo.pdf")

ffo.pdf_to_jpeg('./documents/demo.pdf','./images')
imagesPaths = ffo.all_files_in_folder('./images')
string = ""
for imagePath in imagesPaths:
    string += pytesseract.image_to_string(imagePath);

print(string)
"""
"""
import os
import codecs

input_name = './texts/test.txt'
tmp_name = './texts/tmp.txt'
no = 1000
with codecs.open(input_name, 'r', encoding='utf-8') as fi, \
     codecs.open(tmp_name, 'w', encoding='utf-8') as fo:

    for line in fi:
        new_line = line +" "+str(no)# do your line processing here
        fo.write(new_line)

os.remove(input_name) # remove original
os.rename(tmp_name, input_name) # rename temp to original name
"""

"""
import fileinput,re,sys 

def  modify_file(file_name,pattern,value=""):  
    fh=fileinput.input(file_name,inplace=True)  
    for line in fh:  
        replacement=  line  + " " + value
        line=re.sub(pattern,replacement,line)  
        sys.stdout.write(line)
    fh.close()  

ogrenciNo = "1099";

modify_file("./texts/test.txt",
            "deneme",
            ogrenciNo)


"""


from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import os
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
basePath = os.path.abspath('.')
path = basePath + "/resources/txt-docs/test.txt"
pattern = "Öğrenci No :"
susbt = pattern +" "+ "10099"
replace(path,pattern,susbt)