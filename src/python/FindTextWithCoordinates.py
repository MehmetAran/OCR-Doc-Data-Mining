from DocumentOperation import DocumentOperation

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

## data[0] = ad , x1 , y1 , x2 , y2
## data[1] = no , x1 , y1 , x2 , y2


class FindTextWithCoordinates:
    left = []
    width = []
    top = []
    height = []
    doc = DocumentOperation() 
    data = None
    text = []
    counter = 0
    selectedItems = None
    def __init__(self): 
        self.data = self.doc.getAllDataFromPDF()
        for d in self.data:
            self.left.append(d['left'])
            self.width.append(d['width'])
            self.top.append(d['top'])
            self.height.append(d['height'])
            self.text.append(d['text'])
        

    def operations(self,selectedItems):
        self.selectedItems = selectedItems
        for one in self.selectedItems:
            size = len(self.width)
            for i in range(size):
                size2 = len(self.width[i])
                for j in range(size2):
                    if(self.isExist(i,j)):
                        print(self.text[i][j])
            self.counter += 1    
            
    def isExist(self,i,j):
        leftLocation = self.left[i][j]
        rightLocation = self.left[i][j] + self.width[i][j]
        topLocation = self.top[i][j] 
        bottomLocation = self.top[i][j] +  self.height[i][j]

        selectedLeft = self.selectedItems[self.counter][1]
        selectedRight = self.selectedItems[self.counter][2]
        selectedTop = self.selectedItems[self.counter][3]
        selectedBottom = self.selectedItems[self.counter][4]

        #print(leftLocation," ",rightLocation," ",topLocation," ",bottomLocation," ",self.text[i][j])
        if(rightLocation <= selectedRight and leftLocation >= selectedLeft 
        and bottomLocation <= selectedBottom  and topLocation >= selectedTop ):
            #print(self.text[i][j])
            return True
        return False



a = FindTextWithCoordinates()
selectedItems = []

selectedItems.append(["Ad soyad",1045,1472,1009,1047])


a.operations(selectedItems)