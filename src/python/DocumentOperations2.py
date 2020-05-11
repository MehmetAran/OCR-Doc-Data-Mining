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
from sqliteOperations import SqliteOperations
import locale

class DocumentOperation:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

    def readDoc(self):

        Tk().withdraw()
        filename = askopenfilename()
        basepath = os.path.abspath(".")
        ffo.delete_all_files_in_folder(basepath+'/resources/images')
        ffo.pdf_to_jpeg(filename,basepath+'/resources/images')
        images = ffo.all_files_in_folder(basepath+'/resources/images')

        size = len(images)
        imageDataTexts = []
        imageDataTexts.clear()
        imageDataText = ""
        pureImageDataTexts = []
        pureImageDataTexts.clear()
        counter = 0 
        replacedText = ""
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
            replacedText += text
            imageDataTexts.append(text)
            counter += 1
        
        documents = SqliteOperations().getAll()
        validDocument = ""
        formIndex = 0
        for document in documents:
            operation_document = document[1].replace("\n","").replace("\t","").replace(" ","")
            if replacedText.find(operation_document) != -1 :
                validDocument = document
                break
        targetStringsLeft = []
        targetStringsLeft.clear()
        targetStringsRight = []
        targetStringsRight.clear()
        targetStringsName = []
        targetStringsName.clear()
        targetStringsTop = []
        targetStringsTop.clear()
        targetStringsBottom = []
        targetStringsBottom.clear()
        pageNums = []
        pageNums.clear()
        targetStrings =  SqliteOperations().findByDocumentName(validDocument[1])
        counter = 0

        for  ts  in targetStrings:
            pageNums.append( (int)(ts[2])) 
            targetStringsName.append(ts[3])
            targetStringsTop.append(ts[6])
            targetStringsLeft.append(ts[4])
            targetStringsRight.append(ts[5])
            targetStringsBottom.append( ts[7]) 


            counter += 1
        

        parsingData = []
        parsingData.clear()
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


            lastParsedData = imageDataTexts[pageNum][firstIndex:lastIndex]
            
            size = len(pureImageDataTexts[pageNum]) 
            size2 = len(lastParsedData)  
            last,first = 0,0
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
                            
                    else :
                        break
                    
                if(j == size2):
                    last = i 
                    break
                i += 1
            result = pureImageDataTexts[pageNum][first:last]
            parsingData.append(result)
            print(result)
            print("pureImageDataTexts[first] : ",pureImageDataTexts[pageNum][first])
            print("first : ",first)
            print("last : ",last)


    def getAllDataFromImage(self,imagePath):
        dict = {}
        data = []
        dict.update (pytesseract.image_to_data(imagePath, output_type=Output.DICT,lang="tur"))
        data.append(dict)
        return data