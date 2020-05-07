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
    word_num =[]
    block_num = []
    line_num=[]
    counter = 0
    leftText = ""
    rightText= ""
    topText = ""
    bottomText = "" 
    selectedItems = None
    foundedTexts = []
    def __init__(self): 
        self.data = self.doc.getAllDataFromPDF()
        for d in self.data:
            self.left.append(d['left'])
            self.width.append(d['width'])
            self.top.append(d['top'])
            self.height.append(d['height'])
            self.text.append(d['text'])
            self.block_num.append(d['block_num'])
            self.word_num.append(d['word_num'])
            self.line_num.append(d['line_num'])
    def operations(self,selectedItems):
        self.selectedItems = selectedItems
        for one in self.selectedItems:
            isFirstEntry = True
            size = len(self.width)
            for i in range(size):
                size2 = len(self.width[i])
                for j in range(size2):
                    if(self.isExist(i,j)):
                        if(isFirstEntry):
                            self.leftText = self.findLeftText(i,j)
                            self.topText = self.findTopText(i,j)
                            self.foundedTexts.append([])
                            isFirstEntry = False
                        self.rightText = self.findRightText(i,j)
                        self.bottomText = self.findBottomText(i,j)
                        self.foundedTexts[self.counter] = [self.leftText , self.rightText,self.topText,self.bottomText]
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

    def initFindText(self,i,j):
        lineNum = self.line_num[i][j]
        wordNum = self.word_num[i][j]
        blockNum = self.block_num[i][j]

        return (lineNum,wordNum,blockNum)

    def findLeftText(self,i,j):
        [lineNum,wordNum,blockNum] = self.initFindText(i,j)

        if(wordNum == 1):
            return ""

        [firstBlockIndex , lastBlockIndex ] = self.firstAndLastIndex(i,blockNum,0,self.block_num)
        [firstLineIndex,  lastLineIndex   ] = self.firstAndLastIndex(i,lineNum,firstBlockIndex,self.line_num)
        [firstWordIndex,  lastWordIndex   ] = self.firstAndLastIndex(i,wordNum,firstLineIndex,self.word_num)

        left = ""
        k = firstLineIndex
        while k < j:
            left += self.text[i][k]
            print("left : ",left)
            k += 1
        return left;
    def findRightText(self,i,j):
        [lineNum,wordNum,blockNum] = self.initFindText(i,j)

        [firstBlockIndex , lastBlockIndex ] = self.firstAndLastIndex(i,blockNum,0,self.block_num)
        [firstLineIndex,  lastLineIndex   ] = self.firstAndLastIndex(i,lineNum,firstBlockIndex,self.line_num)
        [firstWordIndex,  lastWordIndex   ] = self.firstAndLastIndex(i,wordNum,firstLineIndex,self.word_num)

        right = ""
        k = j+1
        while k < lastLineIndex:
            if(self.line_num[i][k] == lineNum):
                right += self.text[i][k]
            else : 
                break
            k += 1
        print("right : ",right)
        return right;

    def findTopText(self,i,j):
        [lineNum,wordNum,blockNum] = self.initFindText(i,j)
    def findBottomText(self,i,j):
        [lineNum,wordNum,blockNum] = self.initFindText(i,j)

        
        #print(self.text[i][j])      
    def firstAndLastIndex(self,i,param,startIndex,data):
        size = len(data[i])
        firstParam = 0
        lastParam = 0
        isFirstEntry = True
        k = startIndex
        while  k < size:
            if(param == data[i][k] ):
                if(isFirstEntry):
                    firstParam = k 
                    isFirstEntry = False
                lastParam = k 
            k += 1
        return [(firstParam ),(lastParam )] 

a = FindTextWithCoordinates()
selectedItems = []

selectedItems.append(["Ad soyad",1035,1339,998,1050])


a.operations(selectedItems)