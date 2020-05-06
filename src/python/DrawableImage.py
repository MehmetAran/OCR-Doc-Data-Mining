import cv2 
import sys
import os
import MyInputBox
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
    clone = None
    def __init__(self):
        pass

    def shape_selection(self,event, x, y, flags, param): 
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.ref_point = [(x, y)] 
        elif event == cv2.EVENT_LBUTTONUP:
            self.ref_point.append((int(x), int(y))) 
            cv2.rectangle(self.image, self.ref_point[0], self.ref_point[1], (0, 255, 0), 2)
            cv2.imshow("image", self.image) 
            self.size += 1
    def copyImage(self,ref_point):
        self.tess_point[0] = (int(self.scalaWidth * ref_point[0][0]) ,int(self.scalaHeight * ref_point[0][1]));
        self.tess_point[1] = ( int(self.scalaWidth * ref_point[1][0]),int(self.scalaHeight * ref_point[1][1]));
        crop_img = self.clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]: 
                                                               ref_point[1][0]]
        cv2.imshow("crop_img", crop_img)
        MyInputBox.executor()


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
    def run(self,imagePath):
        self.image = cv2.imread(imagePath)
        self.clone = self.image.copy() 
        cv2.namedWindow("image") 
        cv2.setMouseCallback("image", self.shape_selection) 
        self.width = (self.image.shape[1] )
        self.height = (self.image.shape[0])
        self.resize();
        while True: 
            dsize = (int(self.width/self.scalaWidth), int(self.height/self.scalaHeight))
            print("dsize : " + str(dsize))
            self.image = cv2.resize(self.image,dsize)
            cv2.imshow("image", self.image) 
            key = cv2.waitKey(1) & 0xFF
            draw = False;
            if key == 27 and self.size == 0: 
                cv2.destroyAllWindows() 
                break; 
            elif key == 27:
                self.size -= 1;
                self.image = self.clone.copy()
            if key == 0x0D:
                drawed = True;
                draw = True;
                if len(self.ref_point) == 2: 
                   self.copyImage(self.ref_point)
            if len(self.ref_point) == 2 and draw: 
                draw == False;
                self.ref_point[0] = (int(self.scalaWidth * self.ref_point[0][0]) ,int(self.scalaHeight * self.ref_point[0][1]));
                self.ref_point[1] = ( int(self.scalaWidth * self.ref_point[1][0]),int(self.scalaHeight * self.ref_point[1][1]));
                crop_img = self.clone[self.ref_point[0][1]:self.ref_point[1][1], self.ref_point[0][0]: 
                                                                   self.ref_point[1][0]]
                cv2.imshow("crop_img", crop_img)
            
            if cv2.getWindowProperty('image',1) == -1 :
                break

            

a  = DrawableImage()
a.run("C:\\Users\\warri\\Desktop\\computerscience\\OCR-Doc-Data-Mining\\resources\\images\\tarama1_0.jpg")
