import folder_file_operation as ffo
import image_proccesing as imgp
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import pytesseract
import re 
import os
from pytesseract import Output
import numpy
import os

class DocumentOperation:
    
    def readDoc(self):

        Tk().withdraw()
        filename = askopenfilename()
        basepath = os.path.abspath(".")
        ffo.delete_all_files_in_folder(basepath+'/resources/images')
        ffo.pdf_to_jpeg(filename,basepath+'/resources/images')
        images = ffo.all_files_in_folder(basepath+'/resources/images')

        size = len(images)
        imageDataTexts = []
        imageDataText = ""
        pureImageDataTexts = []
        counter = 0 
        while counter < size:
            #image = cv2.imread(images[counter])
            #gray = imgp.get_grayscale(image)
            #tresh = imgp.thresholding(gray)
            #deskew = imgp.deskew(images[counter])
            text = ""
            text = pytesseract.image_to_string(image=images[counter] ,lang="tur")
            imageDataText += text
            pureImageDataTexts.append(text)
            text = text.replace('\n','').replace(' ','').replace('\t','')
            imageDataTexts.append(text)
            counter += 1
        
        documents = ffo.all_files_in_folder(basepath+'/resources/documents')
        documents = ffo.all_files_in_folder(basepath+'/resources/documents')
        validDocument = ""
        formIndex = 0
        for document in documents:
            operation_document = document.replace("@","/")
            operation_document = operation_document.replace(basepath+"/resources/documents\\","")
            operation_document = operation_document.replace(".txt","")
            operation_document = operation_document.strip()
            if imageDataText.find(operation_document) != -1 :
                validDocument = document
        targetStringsLeft = []
        targetStringsRight = []
        targetStringsName = []
        targetStringsTop = []
        targetStringsBottom = []
        pageNums = []
        targetStrings =  ffo.returnStringReadFile(validDocument)
        counter = 0

        while  counter < len(targetStrings):
            targetStringsName.append(targetStrings[counter].split(";")[0])
            targetStringsTop.append(targetStrings[counter].split(";")[1])
            targetStringsLeft.append(targetStrings[counter].split(";")[2])
            targetStringsRight.append(targetStrings[counter].split(";")[3])
            targetStringsBottom.append( targetStrings[counter].split(";")[4]) 
            pageNums.append( (int)(targetStrings[counter].split(";")[5])) 


            counter += 1
        

        parsingData = []
        targetStringLeft = ""
        targetStringRight = ""
        targetStringTop = ""
        targetStringBottom = ""
        imageDataText = imageDataText.replace('\n',"").replace('\t',"").replace(' ','')

        for targetStringLeft,targetStringRight,targetStringTop,targetStringBottom,pageNum  in zip(targetStringsLeft,targetStringsRight,targetStringsTop,targetStringsBottom,pageNums):
            targetStringTop = targetStringTop.replace('\n','').replace('\t','').replace(' ','')
            targetStringBottom = targetStringBottom.replace('\n','').replace('\t','').replace(' ','')
            targetStringLeft = targetStringLeft.replace('\n','').replace('\t','').replace(' ','')
            targetStringRight = targetStringRight.replace('\n','').replace('\t','').replace(' ','')

            print("top değeri döndü",targetStringTop)
            print("bottom değeri döndü",targetStringBottom)
            print("left değeri döndü",targetStringLeft)
            print("right değeri döndü",targetStringRight)
            
            firstIndex = 0
            lastIndex = len(imageDataTexts[pageNum])

            temp = imageDataTexts[pageNum].find(targetStringTop)
            if(temp != -1):
                firstIndex = temp + len(targetStringTop)

            temp = imageDataTexts[pageNum][firstIndex:].find(targetStringLeft)
            if(temp != -1):
                firstIndex += temp + len(targetStringLeft)

            temp = imageDataTexts[pageNum][firstIndex:].find(targetStringBottom)
            if(temp != -1):
                lastIndex = temp + firstIndex

            temp = imageDataTexts[pageNum][firstIndex:lastIndex].find(targetStringRight)

            if(temp != -1):
                lastIndex = temp + firstIndex


            lastParsedData = imageDataTexts[pageNum][firstIndex+1:lastIndex]
            print(lastParsedData)
            
            size = len(pureImageDataTexts[pageNum]) #enter , space vs 
            size2 = len(lastParsedData)  #bariscilkez
            print("lastParsedData",lastParsedData)
            last,first = 0,0
            print("size : ",size)
            print("size2 : ",size2)
            i = 0
            while i < size :
                j = 0
                while j < size2 : 
                    letterOfBigText = pureImageDataTexts[pageNum][i]
                    letterOfLittleText = lastParsedData[j]
                    if(letterOfBigText == "\n" or letterOfBigText == "\t" or letterOfBigText == " " ):
                        i += 1
                        continue
                    
                    if(letterOfBigText == letterOfLittleText):
                        if(j == 0):
                            first = i
                        i += 1
                        j += 1
                        continue    
                    else :
                        break
                    
                if(j == size2):
                    last = i 
                    break
                i += 1

            print("first : ",first)
            print("last : ",last)
            print("sonuç",pureImageDataTexts[pageNum][first:last])


