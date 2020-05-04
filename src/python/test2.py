import cv2 
import tkinter as tk
from tkinter import simpledialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from Draw import DrawShapsOnImage
# now let's initialize the list of reference point 
ref_point = [] 
crop = False
scalaHeight = 1
scalaWidth  = 1
numberOfRectangles = 0;
tess_point = [[int],[int]]
inputs = []
def shape_selection(event, x, y, flags, param): 
    global ref_point, crop,numberOfRectangles

    if event == cv2.EVENT_LBUTTONDOWN: 
        ref_point = [(x, y)] 
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((int(x), int(y))) 
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image) 
        numberOfRectangles += 1

def copyImage(refpoint):
    print(ref_point)
    print("scalaHeight", scalaHeight)
    print("scalaWidth",scalaWidth)
    tess_point[0] = (int(scalaWidth * ref_point[0][0]) ,int(scalaHeight * ref_point[0][1]));
    tess_point[1] = ( int(scalaWidth * ref_point[1][0]),int(scalaHeight * ref_point[1][1]));
    print(ref_point)
    crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]: 
                                                           ref_point[1][0]]
    cv2.imshow("crop_img", crop_img)
    import tkinter as tk
    from tkinter import simpledialog

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    global inputs;
    def takeinputs():
        name, done = QtWidgets.QInputDialog.getText(
            app , 'Input Dialog', 'Enter your name:')
        if(done):
            inputs.append(name)
            for input in inputs:
                print(input)




basePath = os.path.abspath('.')
imagepath = basePath + "/resources/images/tarama1_0.jpg"
print(imagepath)
image = cv2.imread(imagepath) 
clone = image.copy() 
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 
width = (image.shape[1] )
height = (image.shape[0])

i = 1;
while True :
    if (width/i) > 1100 or (height/i) > 750 :
        scalaWidth = width / (width / (i))
        scalaHeight = height / (height / (i))
        i += (0.02);
    else:
        break;
while True: 
    dsize = (int(width/scalaWidth), int(height/scalaHeight))
    image = cv2.resize(image, dsize)
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
    draw = False;
    if key == 27 and numberOfRectangles == 0: 
        cv2.destroyAllWindows() 
        break; 
    elif key == 27:
        numberOfRectangles -= 1;
        image = clone.copy()
    if key == 0x0D:
        drawed = True;
        draw = True;
        if len(ref_point) == 2: 
           copyImage(ref_point)

    if len(ref_point) == 2 and draw: 
        draw == False;
        print(tess_point)

        ref_point[0] = (int(scalaWidth * ref_point[0][0]) ,int(scalaHeight * ref_point[0][1]));
        ref_point[1] = ( int(scalaWidth * ref_point[1][0]),int(scalaHeight * ref_point[1][1]));

        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]: 
                                                           ref_point[1][0]]
        cv2.imshow("crop_img", crop_img)
        
