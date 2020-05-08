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
                        self.firstAndLastIndexes(i,j)
                        if(isFirstEntry):
                            self.leftText = self.findLeftText(i,j)
                            self.topText = self.findTopText(i,j)
                            self.foundedTexts.append([])
                            isFirstEntry = False
                        self.rightText = self.findRightText(i,j)
                        self.bottomText = self.findBottomText(i,j)
                        self.foundedTexts[self.counter] = [self.leftText , self.rightText,self.topText,self.bottomText]
            self.counter += 1    
        for item in self.foundedTexts:
            print(item[3])       


    def isExist(self,i,j):
        leftLocation = self.left[i][j]
        rightLocation = self.left[i][j] + self.width[i][j]
        topLocation = self.top[i][j] 
        bottomLocation = self.top[i][j] +  self.height[i][j]

        selectedLeft = self.selectedItems[self.counter][1]
        selectedRight = self.selectedItems[self.counter][2]
        selectedTop = self.selectedItems[self.counter][3]
        selectedBottom = self.selectedItems[self.counter][4]

        if(rightLocation <= selectedRight and leftLocation >= selectedLeft 
        and bottomLocation <= selectedBottom  and topLocation >= selectedTop ):
            return True
        return False

    def initFindText(self,i,j):
        lineNum = self.line_num[i][j]
        wordNum = self.word_num[i][j]
        blockNum = self.block_num[i][j]

        return (blockNum,lineNum,wordNum)

    def findLeftText(self,i,j):
        [blockNum,lineNum,wordNum] = self.initFindText(i,j)

        if(wordNum == 1):
            return ""

        [firstBlockIndex , lastBlockIndex ] = self.firstAndLastIndex(i,blockNum,0,self.block_num)
        [firstLineIndex,  lastLineIndex   ] = self.firstAndLastIndex(i,lineNum,firstBlockIndex,self.line_num)
        [firstWordIndex,  lastWordIndex   ] = self.firstAndLastIndex(i,wordNum,firstLineIndex,self.word_num)

        left = ""
        k = firstLineIndex
        while k < j:
            left += self.text[i][k] +"  "
            k += 1
        return left;
    def findRightText(self,i,j):
        [blockNum,lineNum,wordNum] = self.initFindText(i,j)

        [firstBlockIndex , lastBlockIndex ] = self.firstAndLastIndex(i,blockNum,0,self.block_num)
        [firstLineIndex,  lastLineIndex   ] = self.firstAndLastIndex(i,lineNum,firstBlockIndex,self.line_num)
        [firstWordIndex,  lastWordIndex   ] = self.firstAndLastIndex(i,wordNum,firstLineIndex,self.word_num)
        right = ""
        k = j+1
        while k < lastLineIndex:
            if(self.line_num[i][k] == lineNum):
                right += self.text[i][k] + "  "
            else : 
                break
            k += 1
        return right;

    def findTopText(self,i,j):
        [blockNum,lineNum,wordNum] = self.initFindText(i,j)

        [firstBlockIndex , lastBlockIndex ] = self.firstAndLastIndex(i,blockNum,0,self.block_num)
        [firstLineIndex,  lastLineIndex   ] = self.firstAndLastIndex(i,lineNum,firstBlockIndex,self.line_num)
        [firstWordIndex,  lastWordIndex   ] = self.firstAndLastIndex(i,wordNum,firstLineIndex,self.word_num)
        top = ""

        if(lineNum -1 > 0):
            k = firstBlockIndex
            while (lineNum-1) !=  self.line_num[i][k]:
                k += 1
            while k < firstLineIndex:
                top += self.text[i][k] +"  "
                k += 1
            return top
        else :
            if (j == 0):
                return ""
            else :
                mockLineNum = self.line_num[i][firstLineIndex-2]
                mockBlockNum = blockNum - 1
                if(mockBlockNum == 0):
                    return ""
                k = 0
                while mockBlockNum != self.block_num[i][k]:
                    k += 1
                while mockLineNum != self.line_num[i][k]:
                    k += 1
                while k != firstBlockIndex:
                    top += self.text[i][k]
                    k += 1
                return top + "  "
                
    def findBottomText(self,i,j):
        [blockNum,lineNum,wordNum] = self.initFindText(i,j)
        [firstBlockIndex,lastBlockIndex,firstLineIndex,lastLineIndex ] = self.firstAndLastIndexes(i,j)

        size  = len(self.text[i])
        
        if(j+1 >= size):
            return ""
        bottom = ""
        if(blockNum+1 == self.block_num[i][lastLineIndex+1]):
            k = lastBlockIndex+3
            while self.line_num[i][k] == 1 and  k < size  :
                bottom += self.text[i][k] + "  "
                k += 1
            return bottom;
        else : 
            k = lastLineIndex+2
            while self.line_num[i][k] == lineNum + 1 and k < size:
                bottom += self.text[i][k] +"  "
                k += 1
            return bottom
       
    def firstAndLastIndex(self,i,param,startIndex,data):
        size = len(data[i])
        firstParam = 0
        lastParam = 0
        isFirstEntry = True
        k = startIndex
        while  k < size:
            if(param == data[i][k]):
                if(isFirstEntry):
                    firstParam = k 
                    isFirstEntry = False
                lastParam = k 
            k += 1
        return [(firstParam ),(lastParam )] 


    def firstAndLastIndexes(self,i,j):
        [blockNum,lineNum,wordNum] = self.initFindText(i,j)
        size =len(self.block_num[i])
        firstBlockIndex = 0
        lastBlockIndex = 0
        k = 0
        isFirstEntry = True

        

        while k < size :
            if(self.block_num[i][k] == blockNum ):
                if(isFirstEntry):
                    firstBlockIndex = k
                    isFirstEntry = False
                lastBlockIndex = k
            if(self.block_num[i][k] > blockNum):
                break
            k += 1
    
        k = firstBlockIndex+2
        firstLineIndex = 0
        lastLineIndex = 0
        isFirstEntry = True

        while k < size :
            if(self.line_num[i][k] == lineNum):
                if(isFirstEntry):
                    firstLineIndex = k
                    isFirstEntry = False
                lastLineIndex = k
            if(size-1 == k ):
                break
            if(self.data[i]['conf'][k+1] == -1 or self.line_num[i][k+1] == 0):
                break
            k += 1
        k = firstLineIndex 
        while k < lastLineIndex:
            k += 1
        return [firstBlockIndex,lastBlockIndex,firstLineIndex,lastLineIndex]


a = FindTextWithCoordinates()
selectedItems = []

selectedItems.append(["tamamlayarak",493,493+157,1332,1332+25])
selectedItems.append(["Mehmet",1131,1131+117,1015,1015+23])
selectedItems.append(["Anabilim",1025,1025+132,1052,1052+24])
selectedItems.append([":http://fbe.kocaeli.edu.tr/",605,605+233,2247,2247+20])
selectedItems.append(["anlaşıldığından,",806,806+174,1332,1332+25])

a.operations(selectedItems)