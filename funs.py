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
    file.write("\t"*tabCount+"++")
    file.write("\n")
    file.write("\t"*tabCount+"[")
    file.write("\n")
    file.write("\t"*tabCount+">")
    file.write("\n")
    #burada bu derinlikte yapılacak olanlar

    minusArr = getMinusOneArray(base)
    zerosArr = getZeros(minusArr)

    if(len(zerosArr) > 0):
        file.write("\t"*tabCount+">"*toFirstCell+"\n")
        for zeroIndex in zerosArr:
            file.write("\t"*tabCount+">"*zeroIndex+"\n")
            #bu zero base cell için yapılacklar
            
            
            file.write("\t"*tabCount+"+"+"\n")
        

            #end zero base cell
            file.write("\t"*tabCount+"<"*zeroIndex+"\n")
        file.write("\t"*tabCount+"<"*toFirstCell+"\n")
        
    #bu derinlik sonu
    
    if(currentDepth>1):
        loop(maxDepth,currentDepth-1,file,base,excess)

    file.write("\t"*tabCount+"<")
    file.write("\n")
    file.write("\t"*tabCount+"-")
    file.write("\n")
    file.write("\t"*tabCount+"]")
    file.write("\n")


def generateBrainFuck(arr,file):
    base,ex = getBaseAndExcess(myArray)
    maxDepth = max(base)
    loop(maxDepth,maxDepth,file,base,ex)

    #yazdırma
    file.write("\n"+(">"*(maxDepth)))
    file.write(">."*len(arr))
    #yazdırma son

myArray = [64,64,64,64,64,64,64]
codeFile = open("kod.bf","w+")
generateBrainFuck(myArray,codeFile)