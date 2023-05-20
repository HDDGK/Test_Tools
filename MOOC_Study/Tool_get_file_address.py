def find_adress(originalAdress,saveName,saveType):
    print(originalAdress)
    for i in range(len(originalAdress)):
        if (originalAdress[-i-1])=="/":
            originalAdress_up=originalAdress[0:len(originalAdress)-i]
            originalAdress_up+=(saveName+"."+saveType)
            print(originalAdress_up)
            return originalAdress_up

def find_File_type(originalAdress):
    for i in range(len(originalAdress)):
        if (originalAdress[-i-1])==".":
            File_type=originalAdress[len(originalAdress)-i::]
            return File_type

