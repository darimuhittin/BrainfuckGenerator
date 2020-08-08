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
    currentCellIndex = step-1
    tabCount = step-1
    file.write("++")
    file.write("[")
    file.write(">")
    #burada bu derinlikte yapılacak olanlar

    minusArr = getMinusOneArray(base)
    zerosArr = getZeros(minusArr)

    if(len(zerosArr) > 0):
        file.write(">"*toFirstCell)
        for zeroIndex in zerosArr:
            file.write(">"*zeroIndex)
            #bu zero base cell için yapılacklar
            
            
            file.write("+")
        

            #end zero base cell
            file.write("<"*zeroIndex)
        file.write("<"*toFirstCell)
        
    #bu derinlik sonu
    
    if(currentDepth>1):
        loop(maxDepth,currentDepth-1,file,base,excess)

    file.write("<")
    file.write("-")
    file.write("]")
    

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
    file.write((">"*(maxDepth)))
    file.write(">."*len(arr))
    #yazdırma son

myArray = []
text = input("BrainFuck kodu üretilecek dizgiyi girin:\n")

for character in text:
    myArray.append(ord(character))

codeFile = open("kod_bosluksuz.bf","w+")
generateBrainFuck(myArray,codeFile)
