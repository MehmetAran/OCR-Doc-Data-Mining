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


''' 
        index       data
        0           page_num
        1           level
        2           block_num
        3           par_num
        4           line_num
        5           word_num
        6           left
        7           top
        8           width
        9           height
        10          conf
        11          text


'''


def printData():
    Tk().withdraw()
    filename = askopenfilename()
    basepath = os.path.abspath(".")
    ffo.delete_all_files_in_folder(basepath+'/resource/images')
    ffo.pdf_to_jpeg(filename,basepath+'/resource/images')
    images = ffo.all_files_in_folder(basepath+'/resource/images')
    i = 0
    for image in images:
        if(i == 7):
                dict = pytesseract.image_to_data(image,lang="tur")
                print(dict)
        i += 1
"""text = "EmreDemirtaşMimarlıkLIYüksekLisans(TEZLİ)8Doktora|Adı,SoyadıAnabilimDaliProgramıTEZBAŞLIĞIMekanın|Biyo)Politikası:İnsanOlmayanınTeşebbüsleştirilmesindeMekunınRolüÜzerineBirİncelemeTezbaşlığındadeğişiklikvarmı?Eva)HâyırlLi|TEZBAŞLIĞI(İngilizce)TheBiopoliticsofSpace:AnInvestigationontheRoleoftheSpaceintheEnterprised-upNöon-HumanYENİTEZBAŞLIĞI(Tezbaşlığındadeğişiklikvarsadoldurulacaktır)MelenninLp:NXJPolHtay—doğanaNS:z>İpTeşvbbideşkidlmesine«aoMekamaKskiTEZSAVUNMAJÜRİSİÖğretimÜyesiİmzaDoç,Dr.MehtapÖZBAYRAKTARhieenp|(Mehim2Düzeltme(RetProfDr.BülentTanjuETZiDüzelmeORetProl.Dr.AyşenCiravoğlu3jAKabul(ODüzeltmeLU)RetDoç.Dr.SonayAyyıldızESKabulLİDüzeltme|RetDr.Öğr.Üyesi.ErdemCeylan|5Kabul(1DüzeltmeLIRetJÜRİORTAKKARARIYukarıdaaçıkkimliğiverilenöğrencinintezsınavı31/01/2020tarihindesant11:00'deyapılmışveNİNdakikasürmüştür.AdayıntezihakkındaKabul/DüzelmeRetküsanOybirliği/Oygekkiğerileverilmiştir."
index = text.find("Mimarlık")
print("index : ",index)
"""
printData()