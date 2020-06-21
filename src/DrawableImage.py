import cv2 
import sys
import os
import time
from functools import partial  
from tkinter  import *
class DrawableImage:
    ref_point = [] 
    crop = False
    scalaHeight = 1.0
    scalaWidth  = 1.0
    size = 0;
    tess_point = [[int],[int]]
    inputs = []
    width = 0
    height = 0
    image = None
    clones = []
    selectedItems = []
    inputs = []
    pageNum = 0
    def __init__(self):
        pass

    def shape_selection(self,event, x, y, flags, param): 
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.ref_point = [(x, y)] 
        elif event == cv2.EVENT_LBUTTONUP:
            self.ref_point.append((int(x), int(y))) 
            self.clones.append(self.image.copy())
            cv2.rectangle(self.image, self.ref_point[0], self.ref_point[1], (0, 255, 0), 2)
            self.size += 1

    def copyImage(self,ref_point):
        self.tess_point[0] = (int(self.scalaWidth * ref_point[0][0]) ,int(self.scalaHeight * ref_point[0][1]));
        self.tess_point[1] = ( int(self.scalaWidth * ref_point[1][0]),int(self.scalaHeight * ref_point[1][1]));
        crop_img = self.clone[self.tess_point[0][1]:self.tess_point[1][1], self.tess_point[0][0]: 
                                                               self.tess_point[1][0]]
        
        cv2.imshow("Kırpılan Yer", crop_img)
        print(self.tess_point)

    def resize(self):
        i = 1;
        while True :
            if  (self.height/i) > 750 or (self.width/i) > 1100 :
                self.scalaHeight =  self.height / ( self.height / (i))
                self.scalaWidth = self.width / ( self.width / (i))
                i += (0.02);
            else:
                break;
        print("scalawidth : " , self.scalaWidth," scalaheight : ",self.scalaHeight)

    def run(self,imagePath,pageNum):
        self.clones.clear()
        self.pageNum = pageNum
        self.image = cv2.imread(imagePath)
        self.clone = self.image.copy() 
        cv2.namedWindow("image") 
        cv2.setMouseCallback("image", self.shape_selection) 
        self.width = (self.image.shape[1] )
        self.height = (self.image.shape[0])
        self.resize();
        dsize = (int(self.width/self.scalaWidth), int(self.height/self.scalaHeight))

        while True:
            self.image = cv2.resize(self.image,dsize)
            cv2.imshow("image", self.image) 
            key = cv2.waitKey(1) & 0xFF
            draw = False;
            if key == 27 and self.size == 0: 
                cv2.destroyAllWindows() 
                break; 
            elif key == 27:

                self.size -= 1;
                self.image = self.clones[self.size].copy()
                self.clones.pop()

            if key == 0x0D:
                drawed = True;
                draw = True;
                if len(self.ref_point) == 2: 
                    self.copyImage(self.ref_point)
                    self.takeInput(self.tess_point)
            if cv2.getWindowProperty('image',1) == -1 :
                return self.selectedItems
                

            
    def takeInput(self,inputs):
        window = Tk()

        window.title("Kırpma işlemi")

        window.geometry('320x140')

        lbl = Label(window, text="İsim")

        lbl.grid(column=0, row=0)

        txt = Entry(window,width=30)

        txt.grid(column=1, row=0)

        def clicked():
            res =txt.get()
            self.selectedItems.append([self.pageNum,res,inputs[0][0],inputs[1][0],inputs[0][1],inputs[1][1]])
            print("************************ Veriler ********************** ")
            for input in self.selectedItems:
                print(input)
            window.destroy()
            window.quit()

        btn = Button(window, text="Tamam", command=clicked)

        btn.grid(column=2, row=0)

        window.mainloop()

#a  = DrawableImage()
#a.run("C:\\Users\\warri\\Desktop\\computerscience\\OCR-Doc-Data-Mining\\resources\\images\\tarama1_1.jpg")
# x1,y1 ,x2,y2,
# sayfa numarası(0'dan başla) , index adı , x1,x2,y1,y2 olacak şekilde
#self.inputs.append([num1,inputs[0][0],inputs[1][0],inputs[0][1],inputs[1][1]])
