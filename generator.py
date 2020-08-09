#%%
import math 

get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

def getZeros(baseArray):
    zeros = get_indexes(0,baseArray)
    return zeros

def getMinusOneArray(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]-1
    return arr

def getBaseAndExcess(arr):
    arrBase = []
    arrExcess = []
    for e in arr:
        baseRes = (int(math.log2(e)))
        excessRes = e - (2**baseRes)
        arrBase.append(baseRes)
        arrExcess.append(excessRes)
    return arrBase,arrExcess

def loop(maxDepth,currentDepth,file,base,excess):
    step = maxDepth-currentDepth+1
    toFirstCell = currentDepth
    charCount = len(base)
    #currentCellIndex = step-1
    tabCount = step-1
    file.write("\t"*tabCount+"++")
    file.write("\n")
    file.write("\t"*tabCount+"[")
    file.write("\n")
    file.write("\t"*tabCount+">")
    file.write("\n")
    #burada bu derinlikte yapılacak olanlar

    minusArr = getMinusOneArray(base)
    zerosArr = getZeros(minusArr)

    zeroCount = len(zerosArr)
    if(zeroCount > 0):
        tab = tabCount*"\t"
        file.write(tab+">"*toFirstCell+"\n")
        cellNo = 0
        for cellInd in range(charCount):
            if cellInd in zerosArr:
                file.write(tab+"+"+"\n")
            file.write(tab+">"+"\n")
        file.write(tab+"<"*charCount+"\n")
                
        '''
        for zeroIndex in zerosArr:
            if
            file.write(tab+">")
            file.write(tab+">"*zeroIndex+"\n")
            #bu zero base cell için yapılacklar
            
            
            file.write(tab+"+"+"\n")
        

            #end zero base cell
            file.write(tab+"<"*zeroIndex+"\n")
        '''
        file.write(tab+"<"*toFirstCell+"\n")
        

        '''
        tab = "\t"*tabCount
        command = (tab+">+"+"\n")

        file.write(tab+">"*toFirstCell+"\n")
        file.write(command*zeroCount)
        file.write(tab+"<"*zeroCount)
        file.write(tab+"<"*toFirstCell+"\n")
        '''
    #bu derinlik sonu
    
    if(currentDepth>1):
        loop(maxDepth,currentDepth-1,file,base,excess)

    file.write("\t"*tabCount+"<")
    file.write("\n")
    file.write("\t"*tabCount+"-")
    file.write("\n")
    file.write("\t"*tabCount+"]")
    file.write("\n")

def goLastFromFirst(depth,file):
        file.write(">"*(depth))

def goFirstFromLast(depth,file):
        file.write("<"*(depth))
        
def addExcess(exArr,file):
    for e in exArr:
        file.write(">")
        file.write("+"*e)
    file.write("<"*(len(exArr)))

def generateBrainFuck(arr,file):
    base,ex = getBaseAndExcess(myArray)
    maxDepth = max(base)
    loop(maxDepth,maxDepth,file,base,ex)
    
    #go
    goLastFromFirst(maxDepth,file)
    addExcess(ex,file)
    goFirstFromLast(maxDepth,file)
    #yazdırma
    file.write("\n"+(">"*(maxDepth)))
    file.write(">."*len(arr))
    #yazdırma son

myArray = []
text = input("BrainFuck kodu üretilecek dizgiyi girin:\n")

for character in text:
    myArray.append(ord(character))

codeFile = open("code.bf","w+")
generateBrainFuck(myArray,codeFile)
codeFile.close()


f = open("code.bf","r")
withSpace = f.read()
spacelessFile = open("code_spaceless.bf","w+")
spacelessCode = withSpace.replace("\n","").replace("\t","")
spacelessFile.write(spacelessCode)