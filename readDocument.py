import folder_file_operation as ffo
import image_proccesing as imgp
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import pytesseract
import re 
import os


class ReadDocument:
    def readDoc(self):
        Tk().withdraw()
        filename = askopenfilename()
        ffo.delete_all_files_in_folder('./images')
        ffo.pdf_to_jpeg(filename,'./images')
        images = ffo.all_files_in_folder('./images')

        size = len(images)
        imageDataText = ""
        counter = 0 
        while counter < size:
            #image = cv2.imread(images[counter])
            #gray = imgp.get_grayscale(image)
            #tresh = imgp.thresholding(gray)
            #deskew = imgp.deskew(images[counter])
            print(images[counter])
            imageDataText += pytesseract.image_to_string(images[counter],lang="tur")
            counter += 1



        documents = ffo.all_files_in_folder('./documents')
        validDocument = ""
        formIndex = 0
        for document in documents:
            operation_document = document.replace("@","/")
            operation_document = operation_document.replace("./documents\\","")
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
        return allInformations

        