#Klarify.tech
#We will build a console based sudoku solver





class sudokuBoard:
    box = []
    rowValues = []
    columnValues = []
    subValues = []
    value = " "
    
    def __init__(self,value):
        for x in range(81):
            self.box.append(value[x])

    def drawBoard(self):
        count=0
        while(count < 81):
            print(f" {self.box[count]} |",end="")
            count +=1
            if(count%9 == 0):
                print("")
    
    def setValue(self,value,position):
        self.box[position] = value

    def returnColumn(self,number):
        tempList = []
        for i in range (number,81,9):
            tempList.append(self.box[i])

        return tempList
        

    def returnRow(self,number):
        tempList = []
        rowIndex = number * 9
        for i in range(rowIndex,rowIndex+9):
            tempList.append(self.box[i])
        
        return tempList
        

    def returnSub(self,number):
        tempList = []
        subIndex = number
        cycle = 0
        while(subIndex <= number + 20):
            tempList.append(self.box[subIndex])
            if(cycle>=2):
                subIndex = subIndex + 7
                cycle=0
            else:
                subIndex = subIndex +1
                cycle = cycle + 1
        
        return tempList
    
   

    def subMapValue(self,listIndex):
        #subkey indexes
        list1= [0,1,2,9,10,11,18,19,20]
        list2 =[3,4,5,12,13,14,21,22,23]
        list3 =[6,7,8,15,16,17,24,25,26]
        list4 =[27,28,29,36,37,38,45,46,47]
        list5 =[30,31,32,39,40,41,48,49,50]
        list6 =[33,34,35,42,43,44,51,52,53]
        list7 =[54,55,56,63,64,65,72,73,74]
        list8= [57,58,59,66,67,68,75,76,77]
        list9 = [60,61,62,69,70,71,78,79,80]

        if listIndex in list1:
            return 0
        elif listIndex in list2:
            return 3
        elif listIndex in list3:
            return 6
        elif listIndex in list4:
            return 27
        elif listIndex in list5:
            return 30
        elif listIndex in list6:
            return 33
        elif listIndex in list7:
            return 54
        elif listIndex in list8:
            return 57
        elif listIndex in list9:
            return 60
        
    def checkEmpty(self):
        count =0
        for i in range(81):
            if self.box[i] == 0:
                count += 1
        
        return count
        
    
    def applyRules(self,val,testIndex,testListInRules,rowNumber):
        localTestList = testListInRules
       
    
        tempBoxIndex = rowNumber*9+testIndex
       
        
        subIndex = self.subMapValue(tempBoxIndex)
        columnList = self.returnColumn(testIndex)
       
        subList = self.returnSub(subIndex)
       
        if val in columnList or val in subList:
            localTestList =[]
        else:
            localTestList[testIndex]= val

        return localTestList
       
        
    def fillValues(self,testList,rowNumber):
        tempList =[]
        masterSet ={1,2,3,4,5,6,7,8,9}
        testSet = set(testList)
        diffSet = masterSet-testSet
        expectedVal= (list(diffSet))
        
        position=0
       
        
        for val in expectedVal:
            position = 0
            storeIndex= 0
           
            for testIndex in range (0,len(testList)):
                
                if testList[testIndex] == 0:
                    
                    tempList=self.applyRules(val,testIndex,testList,rowNumber)
                  
                    testList = self.returnRow(rowNumber)
                    
                    if tempList == []:
                        pass
                    else:
                    
                        position = position + 1
                        storeIndex = testIndex
                        
                    
                if position == 1 and testIndex >= len(testList)-1:
                   
                    storeIndex= rowNumber*9+storeIndex
                    self.setValue(val,storeIndex)
                    self.drawBoard()
                    testList = self.returnRow(rowNumber)
                    

                    

        
a = list(map(int,input("\nEnter the sudoku numbers : ").strip().split()))
testBoard = sudokuBoard(a)
testBoard.drawBoard()
print("")

while testBoard.checkEmpty() > 0:
    for i in range (0,9):
        row = testBoard.returnRow(i)
        testBoard.fillValues(row,i)
        print(" ")
        

