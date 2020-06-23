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

# Dokumandaki bütün metinler tesseract yardımıyla alınır 
# ve bazı filtrelemeler uygulanır.
# Bu filtrelemeler sonucunda ortaya çıkan son metinler 
# başka bir belgeye aktarılmaya hazır şekilde döndürülür. 
class DocumentOperation:
    def __init__(self):
        pass

    def readDoc(self,filePath):
        basepath = os.path.abspath(".")
        ffo.delete_all_files_in_folder(basepath+'/resource/images')
        ffo.pdf_to_jpeg(filePath,basepath+'/resource/images')
        images = ffo.all_files_in_folder(basepath+'/resource/images')

        size = len(images)
        imageDataText = ""
        indexOfDocument = -1
        replacedText = ""
        parsedDataFromAllDocument = []
        for image in images:
            text = pytesseract.image_to_string(image=image ,lang="tur")
            imageDataText = text
            text = text.replace('\n','').replace(' ','').replace('\t','')
            replacedText = text
        
            documents = SqliteOperations().getAll()
            validDocument = ""
            for document in documents:
                operation_document = document[1].replace("\n","").replace("\t","").replace(" ","")
                if replacedText.find(operation_document) != -1 :
                    validDocument = document
                    continue
            if(validDocument == ""):
                continue
            else : 
                indexOfDocument +=1

            targetStringsLeft   = [] ;  
            targetStringsRight  = [] ; 
            targetStringsName   = [] ;  
            targetStringsTop    = [] ;   
            targetStringsBottom = [] ; 
            targetStrings =  SqliteOperations().findByDocumentName(validDocument[1])

            for  ts  in targetStrings:
                targetStringsName.append(ts[3])
                targetStringsTop.append(ts[6])
                targetStringsLeft.append(ts[4])
                targetStringsRight.append(ts[5])
                targetStringsBottom.append( ts[7]) 

            parsedDataFromOneDocument = []
            targetStringLeft = ""
            targetStringRight = ""
            targetStringTop = ""
            targetStringBottom = ""
            for targetStringName,targetStringLeft,targetStringRight,targetStringTop,targetStringBottom , in zip(targetStringsName,targetStringsLeft,targetStringsRight,targetStringsTop,targetStringsBottom):
                targetStringTop = targetStringTop.replace('\n','').replace('\t','').replace(' ','')
                targetStringBottom = targetStringBottom.replace('\n','').replace('\t','').replace(' ','')
                targetStringLeft = targetStringLeft.replace('\n','').replace('\t','').replace(' ','')
                targetStringRight = targetStringRight.replace('\n','').replace('\t','').replace(' ','')
                firstIndex = 0
                lastIndex = len(replacedText)

                temp = replacedText.find(targetStringTop)
                if(temp != -1 and targetStringTop !=""):
                    firstIndex = temp + len(targetStringTop)

                temp = replacedText[firstIndex:].find(targetStringLeft)
                if(temp != -1 and targetStringLeft != "") :
                    firstIndex += temp + len(targetStringLeft)

                temp = replacedText[firstIndex:].find(targetStringBottom)
                if(temp != -1 and targetStringBottom !=""):
                    lastIndex = temp + firstIndex

                temp = replacedText[firstIndex:lastIndex].find(targetStringRight)
                if(temp != -1 and targetStringRight != ""):
                    lastIndex = temp + firstIndex

                lastParsedData = replacedText[firstIndex:lastIndex]

                size = len(imageDataText) 
                size2 = len(lastParsedData)  
                last,first = 0,0
                i = 0
                while i < size :
                    j = 0
                    while j < size2 : 
                        letterOfBigText = imageDataText[i]
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
                result = imageDataText[first:last]
                parsedDataFromOneDocument.append([validDocument[1],targetStringName,result])
            parsedDataFromAllDocument.append(parsedDataFromOneDocument)
        return parsedDataFromAllDocument


    def getAllDataFromImage(self,imagePath):
        dict = {}
        data = []
        data.clear()
        dict.update (pytesseract.image_to_data(imagePath, output_type=Output.DICT,lang="tur"))
        data.append(dict)
        return data