from math import log2
get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
'''
text = input("Type some text to generate brainfuck code for print that text:\n")

for character in text:
    arr.append(ord(character))
    
for i in range(4):
    arr.append(int(input(f"{i} index : ")))
'''
#%%
arr = [83,69,76,65,77]
arrBase = []
arrExcess = []
codeFile = open("kod.bf","w+")
'''
text = input("Type some text to generate brainfuck code for print that text:\n")

for character in text:
    arr.append(ord(character))
   '''

#create decimal array from char array


print("Decimal Array :",arr)

#find base array
for e in arr:
    baseRes = (int(log2(e)))
    excessRes = e - (2**baseRes)
    arrBase.append(baseRes)
    arrExcess.append(excessRes)

print("Base Array : ",arrBase)
print("Excess Array : ",arrExcess)

numTwo = max(arrBase)

step = 0
for i in range(numTwo):

    codeFile.write("++[>")
    step = step + 1
    rightCount = (numTwo-step)
    #-1 to all elements in arrBase
    for i in range(len(arrBase)):
        arrBase[i] = arrBase[i]-1

    zeroIndexes = get_indexes(0,arrBase)
    
    for zeroIndex in zeroIndexes:
        codeFile.write(">"*rightCount) #rc 0 exception
        
        codeFile.write(">"*(zeroIndex+1))
        codeFile.write("+")
        codeFile.write("<"*(zeroIndex+1))

        codeFile.write("<"*rightCount)

    if(rightCount>0): # son hane aşamasında sağa gitmemeli
        codeFile.write(">")

    codeFile.write("<-]")

for i in range(numTwo):
    codeFile.write("-]")

#bas dizi indexine gel
codeFile.write(">"*(numTwo-1))

for e in arrExcess:
    codeFile.write(">")
    codeFile.write("+"*e)

codeFile.write("[<]") #go to first 0 cell

codeFile.write(">."*len(arr)) # write all cells
    

print(arrBase)
