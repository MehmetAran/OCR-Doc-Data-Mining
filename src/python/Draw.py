import cv2 

class DrawShapsOnImage():
    def drawShape(self,image,event,x,y):
        if event == cv2.EVENT_LBUTTONDOWN: 
            ref_point = [(x, y)] 
        elif event == cv2.EVENT_LBUTTONUP:
            ref_point.append((int(x), int(y))) 
            cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
            cv2.imshow("image", image) 

    def copyImage(self,ref_point,scalaWidth,scalaHeight):
        clone = None
        tess_point[0] = (int(scalaWidth * ref_point[0][0]) ,int(scalaHeight * ref_point[0][1]));
        tess_point[1] = ( int(scalaWidth * ref_point[1][0]),int(scalaHeight * ref_point[1][1]));
        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]: 
                                                           ref_point[1][0]]
        cv2.imshow("crop_img", crop_img)