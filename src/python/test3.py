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
#data[i][indexes in here ][1][j]

doc = DocumentOperation() 
data = doc.getAllDataFromPDF()



isFirst = True
i = 0 
lastWordNum = 0                                                                            
                          
for i in range(len(data)):
    for j in range (len(data[i][0][1])):
        x1 =int(data[i][6][1][j])
        y1 = int( data[i][7][1][j])
        x2 = x1 + int(data[i][8][1][j])
        y2 = y1 + int(data[i][9][1][j]) 
        line_num = 0
        word_num = 0

        if (x1 >= 1125 and x2 <= 1255 and y1 >= 1004 and y2 <= 1038 and isFirst and data[i][11][1][j] != ""):

            lastWordNum = data[i][5][1][j]
            # level = 5 word_num = 1 
            if(isFirst):
                line_num = data[i][4][1][j]
                word_num = data[i][5][1][j]
                text = data[i][11][1][j]
                block_num = data[i][2][1][j]
                print("line_num : ",line_num , "word_num : ", word_num , "text : " , text)
            
            k = j
            for k in range(len(data[0][0][1])):
                xx1 =int(data[i][6][1][k])
                yy1 = int( data[i][7][1][k])
                xx2 = x1 + int(data[i][8][1][k])
                yy2 = y1 + int(data[i][9][1][k]) 
                if( xx1 >= 1128 and xx2 <= 1007 and yy1 >= 1252 and yy2 <= 1041 and data[i][11][1][k] != "") :
                    lastWordNum = data[i][5][1][k]

            leftText = ""
            rightText = ""
            topText = ""
            bottomText = ""
            leftFirstIndex = 0
            isFirst2 = False
            k = 0
            for k in range(int(j)):
                if(data[i][4][1][k] == line_num and data[i][2][1][k] == block_num):
                    print("line_num : " , data[i][4][1][k]," text : ",data[i][11][1][k])
                    leftText += data[i][11][1][k] + " "
                if(isFirst2):
                    leftFirstIndex = k
                    isFirst2 = True
            k = j + 1
            for k in range(len(data[0][0][1])):
                if(data[i][4][1][k] == line_num and data[i][2][1][k] == block_num and lastWordNum < data[i][5][1][k]):
                    print("line_num : " , data[i][4][1][k]," text : ",data[i][11][1][k])
                    rightText += data[i][11][1][k] + " "                    
                if(data[i][4][1][k] == line_num + 1 and data[i][2][1][k] == block_num) :
                    print("line_num : " , data[i][4][1][k]," text : ",data[i][11][1][k],"block_num",data[i][2][1][k])
                    bottomText += data[i][11][1][k] + " "
                if(data[i][4][1][k] == block_num + 1):
                    bottomText += data[i][4][1][k] 
                elif(data[i][2][1][k] == block_num+2 and data[i][4][1][k] and data[i][4][1][k] == line_num + 2 ):
                    break;
            
            k = 0
            for k in range(len(data[0][0][1])):
                if(int(block_num) == int(data[i][2][1][k]) + 1 ):
                    topText += data[i][11][1][k] +" "
                elif(int(block_num) -1 == int(data[i][2][1][k])):
                    break



            print("leftText : " ,leftText)
            print("rightText : ",rightText)
            print("bottomText : ",bottomText)
            print("topText : ",topText) 
            print("lastWordNum",lastWordNum)


            isFirst = False

            #isFirst = False