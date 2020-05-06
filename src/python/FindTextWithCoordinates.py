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
    def __init__(self): 
        self.data = self.doc.getAllDataFromPDF()    
        for d in self.data:
            self.left.append(d['left'])
            self.width.append(d['width'])
            self.top.append(d['top'])
            self.height.append(d['height'])
            self.text.append(d['text'])

    def operations(self,selectedItems):
        size = len(self.width[self.counter])
        for one in selectedItems:
            for j in range(size):
                self.isExist(self.counter,j)
            self.counter += 1

    def isExist(self,i,j):
        leftLocation = self.left[i][j]
        rightLocation = self.left[i][j] + self.width[self.counter][j]
        topLocation = self.top[i][j] 
        bottomLocation = self.top[i][j] +  self.height[self.counter][j]
        print("leftLocation",leftLocation,)
        print("rightLocation",rightLocation,)
        print("topLocation",topLocation,)
        print("bottomLocation",bottomLocation)

a = FindTextWithCoordinates()
selectedItems = []

selectedItems.append(["Ad soyad",1125,1255,1004,1038])


a.operations(selectedItems)