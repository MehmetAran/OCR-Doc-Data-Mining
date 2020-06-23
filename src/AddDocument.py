from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import folder_file_operation as ffo
import os
from DrawableImage import DrawableImage 
from FindTextWithCoordinates import FindTextWithCoordinates
from sqliteOperations import SqliteOperations


from ApproveScreen import ApproveScreen


# Dokuman tanımlama işlemleri bu class tarafında yürütülür.
class AddDocumentToSqlite:
    images = []
    documentKey = ""
    def __init__(self):
        window = Tk()

        window.title("Doküman Ekle")

        window.geometry('320x140')

        lbl = Label(window, text="Doküman ismi")

        lbl.grid(column=0, row=0)

        txt = Entry(window,width=30)

        txt.grid(column=1, row=0)

        def clicked():
            self.documentKey =txt.get()
            window.destroy()
            window.quit()

        btn = Button(window, text="Tamam", command=clicked)

        btn.grid(column=2, row=0)

        window.mainloop()



    def start(self,filePath): 
        basepath = os.path.abspath(".")
        ffo.delete_all_files_in_folder(basepath+'/resource/images')
        ffo.pdf_to_jpeg(filePath,basepath+'/resource/images')
        self.images = ffo.all_files_in_folder(basepath +'/resource/images')
        k = 0
        for image in self.images:
            print(image)
            print(self.images)
            selectedItems = DrawableImage().run(image,k)
            k += 1
        counter = 0
        size = len(selectedItems)
        k = 0
        selected = []
        names = []
        lastResult = []
        for i in selectedItems :
            print(i)
            if(i[0] == k):
                results = selected.append([i[1],i[2],i[3],i[4],i[5]]),
                names.append(i[1])
            else:
                if(len(selected) != 0):
                    results = FindTextWithCoordinates().operations(selected,self.images[k])
                    for j in range(len(names)):
                        lastResult.append([names[j],results[j][0],results[j][1],results[j][2],results[j][3]])
                        """db = SqliteOperations()
                        db.insert(self.documentKey,k,names[j],results[j][0],results[j][1],results[j][2],results[j][3])"""

                k += 1
                selected.clear()
                names.clear()
                names.append(i[1])
                selected.append([i[1],i[2],i[3],i[4],i[5]])
        if(len(selected) != 0):
            results = FindTextWithCoordinates().operations(selected,self.images[k])
            for j in range(len(selected)):
                lastResult.append([names[j],results[j][0],results[j][1],results[j][2],results[j][3]])
                    


        print("lastResult : ",lastResult)
        a = ApproveScreen(lastResult,self.documentKey)
        a.exec_()

        selected.clear()
        selectedItems.clear()
        names.clear()