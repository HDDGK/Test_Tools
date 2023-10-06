str_k="-"*12
def mainMenu(mainList):
    for i in range(len(mainList)):
        if i==0 or i==len(mainList)-1:
            print(str_k,mainList[i],str_k)
        else:
            print('\t\t\t',i,mainList[i])