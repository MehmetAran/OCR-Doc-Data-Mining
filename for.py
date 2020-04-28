import folder_file_operation as ffo
import pytesseract


ffo.pdf_to_jpeg("C:\\Users\\warri\\Downloads\\Documents\\esrarileiliskilibozukluklar-bab9021e.pdf",'./images')
images = ffo.all_files_in_folder('./images')

string = ""
for image in images:
    string += pytesseract.image_to_string(image,lang="tur")


print(string)

file1 = open("./documents/aysenin ödevi.txt","w",encoding="utf-8") 
  
file1.write("Hello \n") 
file1.writelines(string) 
file1.close() 