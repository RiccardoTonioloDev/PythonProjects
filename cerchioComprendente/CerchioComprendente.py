class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def getX(self):
        return self.X 

    def getY(self):
        return self.Y

    def distanzaPunti(self,Punto):
        diffX = abs(self.getX()-Punto.getX())
        diffY = abs(self.getY()-Punto.getY())
        punteggio = diffX+diffY
        return abs(punteggio)

def findUP(numeroPunti):
        UP = insiemePunti[0]
        for x in range(1,len(insiemePunti)):
            if(UP.getY()<insiemePunti[x].getY()):
                UP = insiemePunti[x]
        return UP

def findDOWN(numeroPunti):
        DOWN = insiemePunti[0]
        for x in range(1,len(insiemePunti)):
            if(DOWN.getY()>insiemePunti[x].getY()):
                DOWN = insiemePunti[x]
        return DOWN

def findLEFT(numeroPunti):
        LEFT = insiemePunti[0]
        for x in range(1,len(insiemePunti)):
            if(LEFT.getX()>insiemePunti[x].getX()):
                LEFT = insiemePunti[x]
        return LEFT

def findRIGHT(numeroPunti):
        RIGHT = insiemePunti[0]
        for x in range(1,len(insiemePunti)):
            if(RIGHT.getX()<insiemePunti[x].getX()):
                RIGHT = insiemePunti[x]
        return RIGHT

def middlePoint(CUPSX,CUPDX,CDOWNSX,CDOWNDX):
    middleP = Punto((CUPDX.getX()+CUPSX.getX())/2,(CUPDX.getY()+CDOWNDX.getY())/2)
    return middleP


BEST_PUNTO1 = Punto(0,0)
BEST_PUNTO2 = Punto(0,0)
BEST_PUNTO3 = Punto(0,0)

CARDINAL_UPSX = Punto(0,0)
CARDINAL_UPDX = Punto(0,0)
CARDINAL_DOWNSX = Punto(0,0)
CARDINAL_UPDX = Punto(0,0)


print("Inserire quanti punti si vuole utilizzare nel suo grafico")
numeroPunti = input()

insiemePunti = []

for x in range(int(numeroPunti)):
    counter= x+1
    print("Inserire la x del punto n.",counter,":")
    x=int(input())
    print("Inserire la y del punto n.",counter,":")
    y=int(input())
    insiemePunti.append(Punto(x,y))

for x in range(len(insiemePunti)):
    counter= x+1
    variableX = insiemePunti[x].getX()
    variableY = insiemePunti[x].getY()
    print("Punto n.",counter," X: ",variableX," Y: ",variableY,"")

BEST_PUNTO1 = insiemePunti[0]
punto1 = 0
BEST_PUNTO2 = insiemePunti[0]
punto2 = 0
BEST_PUNTO3 = insiemePunti[0]
punto3 = 0

CARDINAL_UPSX = Punto(findLEFT(numeroPunti).getX(),findUP(numeroPunti).getY())
CARDINAL_UPDX = Punto(findRIGHT(numeroPunti).getX(),findUP(numeroPunti).getY())
CARDINAL_DOWNSX = Punto(findLEFT(numeroPunti).getX(),findDOWN(numeroPunti).getY())
CARDINAL_DOWNDX = Punto(findRIGHT(numeroPunti).getX(),findDOWN(numeroPunti).getY())

if(insiemePunti[x].getY()>=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()<middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        punto1 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
        punto2 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
        punto3 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
        #in alto a sinistra
elif(insiemePunti[x].getY()>middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()>=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        punto1 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
        punto2 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
        punto3 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
        #in alto a destra
elif(insiemePunti[x].getY()<middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()<=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        punto1 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
        punto2 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
        punto3 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
        #in basso a sinistra
elif(insiemePunti[x].getY()<=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()>middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        punto1 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])
        punto2 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])
        punto3 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])



for x in range(len(insiemePunti)):
    if(insiemePunti[x].getY()>=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()<middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        if(CARDINAL_UPSX.distanzaPunti(insiemePunti[x])<=punto1):
            
            punto3 =punto2
            punto2 = punto1
            punto1 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = BEST_PUNTO1
            BEST_PUNTO1 = insiemePunti[x]
        elif(CARDINAL_UPSX.distanzaPunti(insiemePunti[x])<=punto2):
            punto3 = punto2
            punto2 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = insiemePunti[x]
        elif(CARDINAL_UPSX.distanzaPunti(insiemePunti[x])<=punto3):
            punto3 = CARDINAL_UPSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = insiemePunti[x]
        #in alto a sinistra
    elif(insiemePunti[x].getY()>middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()>=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        
        if(CARDINAL_UPDX.distanzaPunti(insiemePunti[x])<=punto1):
            punto3 =punto2
            punto2 = punto1
            punto1 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = BEST_PUNTO1
            BEST_PUNTO1 = insiemePunti[x]
        elif(CARDINAL_UPDX.distanzaPunti(insiemePunti[x])<=punto2):
            punto3 = punto2
            punto2 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = insiemePunti[x]
        elif(CARDINAL_UPDX.distanzaPunti(insiemePunti[x])<=punto3):
            punto3 = CARDINAL_UPDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = insiemePunti[x]
        #in alto a destra
    elif(insiemePunti[x].getY()<middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()<=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        
        if(CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])<=punto1):
            punto3 =punto2
            punto2 = punto1
            punto1 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = BEST_PUNTO1
            BEST_PUNTO1 = insiemePunti[x]
        elif(CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])<=punto2):
            punto3 = punto2
            punto2 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = insiemePunti[x]
        elif(CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])<=punto3):
            punto3 = CARDINAL_DOWNSX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = insiemePunti[x]
        #in basso a sinistra
    elif(insiemePunti[x].getY()<=middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getY() and insiemePunti[x].getX()>middlePoint(CARDINAL_UPSX,CARDINAL_UPDX,CARDINAL_DOWNSX,CARDINAL_DOWNDX).getX()):
        
        if(CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])<=punto1):
            punto3 =punto2
            punto2 = punto1
            punto1 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = BEST_PUNTO1
            BEST_PUNTO1 = insiemePunti[x]
        elif(CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])<=punto2):
            punto3 = punto2
            punto2 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = BEST_PUNTO2
            BEST_PUNTO2 = insiemePunti[x]
        elif(CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])<=punto3):
            punto3 = CARDINAL_DOWNDX.distanzaPunti(insiemePunti[x])
            BEST_PUNTO3 = insiemePunti[x]
        #in basso a destra

print("")
print("PRIMO X: ",CARDINAL_UPSX.getX()," Y: ",CARDINAL_UPSX.getY(),"")
print(CARDINAL_UPSX.distanzaPunti(BEST_PUNTO1))
print(CARDINAL_UPSX.distanzaPunti(insiemePunti[1]))
print("I tre punti che creano la circonferenza sono:")
print("PRIMO X: ",BEST_PUNTO1.getX()," Y: ",BEST_PUNTO1.getY(),"")
print("SECONDO X: ",BEST_PUNTO2.getX()," Y: ",BEST_PUNTO2.getY(),"")
print("TERZO X: ",BEST_PUNTO3.getX()," Y: ",BEST_PUNTO3.getY(),"")

#print("DOWN X: ",findDOWN(numeroPunti).getX()," Y: ",findDOWN(numeroPunti).getY(),"")
#print("UP X: ",findUP(numeroPunti).getX()," Y: ",findUP(numeroPunti).getY(),"")
#print("LEFT X: ",findLEFT(numeroPunti).getX()," Y: ",findLEFT(numeroPunti).getY(),"")
#print("RIGHT X: ",findRIGHT(numeroPunti).getX()," Y: ",findRIGHT(numeroPunti).getY(),"")
