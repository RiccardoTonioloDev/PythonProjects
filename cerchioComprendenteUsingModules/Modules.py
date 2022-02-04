from point import Point

def inputPoint():
    numeroPunti = 0
    listaPunti = []
    while (True):
        numeroPunti = input("Quanti punti vuole inserire nel calcolo della circonferenza?(Mi raccomando un minimo di 3 punti)")
        if(int(numeroPunti)>=3):
            break
        else:
            print("Non hai inserito il numero di punti minimo richiesto")
    for x in range(int(numeroPunti)):
        punto = Point(0,0)
        punto.setX(int(input(f"[PUNTO n.{x+1}] Inserire la X:")))
        punto.setY(int(input(f"[PUNTO n.{x+1}] Inserire la Y:")))
        listaPunti.append(punto)

    return listaPunti


def extremesFinder(points):
    UP_point = Point(0,0)
    DOWN_point = Point(0,0)
    LEFT_point = Point(0,0)
    RIGHT_point = Point(0,0)
    counter = 0
    for point in points:
        if (counter == 0):
            UP_point = point
            DOWN_point = point
            LEFT_point = point
            RIGHT_point = point
        else:
            if(point.getY()>UP_point.getY()):
                #for the upper part
                UP_point=point
            if(point.getY()<DOWN_point.getY()):
                #for the lower part
                DOWN_point=point
            if(point.getX()>RIGHT_point.getX()):
                #for the right part
                RIGHT_point=point
            if(point.getX()<LEFT_point.getX()):
                #for the left part
                LEFT_point=point
        counter+=1
    return UP_point,DOWN_point,LEFT_point,RIGHT_point

def cardinalPointsFinder(extremes):
    UPLEFT_point = Point(extremes[2].getX(),extremes[0].getY())
    UPRIGHT_point = Point(extremes[3].getX(),extremes[0].getY())
    DOWNLEFT_point = Point(extremes[2].getX(),extremes[1].getY())
    DOWNRIGHT_point = Point(extremes[3].getX(),extremes[1].getY())
    return UPLEFT_point,UPRIGHT_point,DOWNLEFT_point,DOWNRIGHT_point

def rectangleCenter(extremes):
    cardinals = cardinalPointsFinder(extremes)
    center = Point((cardinals[0].getX()+cardinals[1].getX())/2,(cardinals[0].getY()+cardinals[2].getY())/2)
    return center

def findFace(center, point):
    if((point.getX()>center.getX()) and (point.getY()>=center.getY())):
        # first Face
        return "first"
    elif((point.getX()<=center.getX()) and (point.getY()>center.getY())):
        # second Face
        return "second"
    elif((point.getX()<center.getX()) and (point.getY()<=center.getY())):
        # third Face
        return "third"
    elif((point.getX()>=center.getX()) and (point.getY()<center.getY())):
        # fourth Face
        return "fourth"
    else:
        return "first"

def referenceCardinalScore(face,cardinals,point):
    score=0
    if(face == "first"):
        score = cardinals[1].distanceFromAPoint(point)
    elif(face == "second"):
        score = cardinals[0].distanceFromAPoint(point)
    elif(face == "third"):
        score = cardinals[2].distanceFromAPoint(point)
    elif(face == "fourth"):
        score = cardinals[3].distanceFromAPoint(point)
    return score

def TOPBestScores(points):
    cardinals = cardinalPointsFinder(extremesFinder(points))
    center = rectangleCenter(extremesFinder(points))

    TOP1 = center
    TOP2 = center
    TOP3 = center
    for point in points:
        if(referenceCardinalScore(findFace(center,point),cardinals,point)<=referenceCardinalScore(findFace(center,TOP1),cardinals,TOP1)):
            TOP3=TOP2
            TOP2=TOP1
            TOP1=point
        elif(referenceCardinalScore(findFace(center,point),cardinals,point)<=referenceCardinalScore(findFace(center,TOP2),cardinals,TOP2)):
            TOP3=TOP2
            TOP2=point
        elif(referenceCardinalScore(findFace(center,point),cardinals,point)<=referenceCardinalScore(findFace(center,TOP3),cardinals,TOP3)):
            TOP3=point
    return TOP1,TOP2,TOP3
