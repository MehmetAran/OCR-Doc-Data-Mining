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
        imageDataText = ""
        imageDataText2 = ""

        counter = 0 
        while counter < size:
            #image = cv2.imread(images[counter])
            #gray = imgp.get_grayscale(image)
            #tresh = imgp.thresholding(gray)
            #deskew = imgp.deskew(images[counter])
            imageDataText += pytesseract.image_to_string(image=images[counter] ,lang="tur")
            imageDataText2 += pytesseract.image_to_data(image=images[counter] ,lang="tur")
            counter += 1



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
        targetStringsIsSingle = []
        targetStrings =  ffo.returnStringReadFile(validDocument)
        counter = 0

        while  counter < len(targetStrings):
            targetStringsName.append(targetStrings[counter].split(";")[0])
            targetStringsTop.append(targetStrings[counter].split(";")[1])
            targetStringsLeft.append(targetStrings[counter].split(";")[2])
            targetStringsRight.append(targetStrings[counter].split(";")[3])
            targetStringsBottom.append( targetStrings[counter].split(";")[4]) 
            targetStringsIsSingle.append( targetStrings[counter].split(";")[5]) 

            counter += 1


        parsingData = []
        parsingData.clear()
        for targetStringLeft,targetStringRight,targetStringTop,targetStringBottom ,targetStringIsSingle in zip(targetStringsLeft,targetStringsRight,targetStringsTop,targetStringsBottom,targetStringsIsSingle):
            firstIndex = 0
            lastIndex  = 0

            firstIndex = imageDataText.find(targetStringTop) 
            if firstIndex != 0:
                firstIndex += len(targetStringTop)

            firstIndex  += imageDataText[firstIndex:].find(targetStringLeft) + len(targetStringLeft)
            lastIndex = imageDataText.rfind(targetStringBottom)
            if lastIndex != 0:
                temp = imageDataText[:lastIndex].find(targetStringRight)
                if temp != 0:
                    lastIndex = temp
            else:
                lastIndex = imageDataText.find(targetStringRight)

            targetString = imageDataText[firstIndex:lastIndex]
            if targetStringIsSingle == "!":
                temp = targetString.find('\n')
                targetString = targetString[:temp]
    
            targetString = targetString.replace("!","")
            targetString = targetString.replace(":","")
            targetString = targetString.replace("©","@")
            targetString = targetString.strip()

            parsingData.append(targetString)

        allInformations = []
        allInformations.append(targetStringsName)
        allInformations.append(parsingData)
        print(allInformations)
        return allInformations

    def getAllDataFromPDF(self):
        basepath = os.path.abspath(".")
        Tk().withdraw()
        filename = askopenfilename()
        ffo.delete_all_files_in_folder(basepath+'/resources/images')
        ffo.pdf_to_jpeg(filename,basepath+'/resources/images')
        images = ffo.all_files_in_folder(basepath+'/resources/images')
        
        size = len(images)
        counter = 0
        data = []
        data.clear()
        while counter < size:
            dict = {}
            dict.update (pytesseract.image_to_data(images[counter], output_type=Output.DICT,lang="tur"))
            data.append(dict)
            counter += 1
        return data;
        
