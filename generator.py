#%%
import math 

logBase = 2
text = input("BrainFuck kodu üretilecek dizgiyi girin:\n")


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
        try:
            baseRes = (int(math.log(e,logBase)))
        except:
            baseRes = 0
        if baseRes != 0:
            excessRes = e - (logBase**baseRes)
        else:
            excessRes = e
        arrBase.append(baseRes)
        arrExcess.append(excessRes)
    return arrBase,arrExcess

def loop(maxDepth,currentDepth,file,base,excess):
    step = maxDepth-currentDepth+1
    toFirstCell = currentDepth-1# burada muntazam bir problem var lakin
                                # nasıl yanlışlıkla üstesinden geldiğime dair
                                # bildiğim tek şey var ise
                                # o da hiçbir şey bilmediğimdir...
    charCount = len(base)
    #currentCellIndex = step-1
    tabCount = step-1
    tab = tabCount*"\t"
    file.write(tab+"+"*logBase)
    file.write("\n")
    file.write(tab+"[")
    file.write("\n")
    file.write(tab+">")
    file.write("\n")
    #burada bu derinlikte yapılacak olanlar

    minusArr = getMinusOneArray(base)
    zerosArr = getZeros(minusArr)

    zeroCount = len(zerosArr)
    if(zeroCount > 0):
        file.write(tab+">"*toFirstCell+"\n")
        tab += "\t"
        for cellInd in range(charCount):
            if cellInd in zerosArr:
                file.write(tab+"+"+"\n")
            file.write(tab+">"+"\n")
        file.write(tab+"<"*charCount+"\n")
        tab = tab[:-1]
        file.write(tab+"<"*toFirstCell+"\n")
        
    #bu derinlik sonu
    
    if(currentDepth>1):
        loop(maxDepth,currentDepth-1,file,base,excess)

    file.write(tab+"<")
    file.write("\n")
    file.write(tab+"-")
    file.write("\n")
    file.write(tab+"]")
    file.write("\n")

def goLastFromFirst(depth,file):
        file.write(">"*(depth-1))

def goFirstFromLast(depth,file):
        file.write("<"*(depth-1))
        
def addExcess(exArr,file):
    for e in exArr:
        file.write(">")
        file.write("+"*e)
    file.write("<"*(len(exArr)))

def generateBrainFuck(arr,file):
    base,ex = getBaseAndExcess(myArray)
    maxDepth = max(base)
    loop(maxDepth,maxDepth,file,base,ex)
    
    #second loop
    base,ex = getBaseAndExcess(ex)
    loop(maxDepth,maxDepth,file,base,ex)
    #second loop
    
    #third loop
    # base,ex = getBaseAndExcess(ex)
    # loop(maxDepth,maxDepth,file,base,ex)
    #third loop

    #go
    goLastFromFirst(maxDepth,file)
    addExcess(ex,file)
    goFirstFromLast(maxDepth,file)
    #yazdırma
    file.write("\n"+(">"*(maxDepth-1))+"\n")
    file.write(">[.>]")
    #yazdırma son

myArray = []

for character in text:
    myArray.append(ord(character))

codeFile = open("code_base"+str(logBase)+".bf","w+")
generateBrainFuck(myArray,codeFile)
codeFile.close()


f = open("code_base"+str(logBase)+".bf","r")
withSpace = f.read()
spacelessFile = open("code_spaceless_base"+str(logBase)+".bf","w+")
spacelessCode = withSpace.replace("\n","").replace("\t","")
spacelessFile.write(spacelessCode)