import pathlib
import os

def subDr(pathName,minus):
    dirs = os.listdir(pathName)
    if (len(dirs)>=1):
        for file in dirs:
            if (os.path.isdir(pathName+file)):
                peso = getSize(pathName+file+"\\")
                print(minus+file+"   "+str(round(peso,2))+" MB")
                subDr(pathName+file+"\\",minus+"---")
                
def getSize(pathName):
    somma = 0
    dirs = os.listdir(pathName)
    if (len(dirs)>=1):
        for file in dirs:
            if (os.path.isdir(pathName+file)):
                somma = somma + getSize(pathName+file+"\\")
            else:
                somma = somma +(os.stat(pathName+file).st_size)/1048576
    return somma


PATH = pathlib.Path(__file__).parent.absolute()
PATH = str(PATH) + "\\"
subDr(PATH,"")

