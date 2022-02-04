from Modules import *
from point import Point

#print("-------------TEST-------------")
#print("[PRINTING EXTREMES]: Up, Down, Left, Right")
#points = [Point(1,0),Point(0,1),Point(-1,0),Point(0,-1),Point(2,2),Point(-2,-2)]
points = inputPoint()
extremes = extremesFinder(points)
#for extreme in extremes:
#    print(f"X: {extreme.getX()}; Y: {extreme.getY()}")
#print("[PRINTING CARDINALS]: UpLeft, UpRight, DownLeft, DownRight")
cardinals = cardinalPointsFinder(extremes)
#for cardinal in cardinals:
#    print(f"X: {cardinal.getX()}; Y: {cardinal.getY()}")
#print("[PRINTING Center]: Central point")
center = Point(rectangleCenter(extremes).getX(),rectangleCenter(extremes).getY())
#print(f"X: {center.getX()}; Y: {center.getY()}")
#print("[PRINTING FACES OF EVERY POINT]: Every point")
#for point in points:
#    print(findFace(center,point))
#print("[PRINTING SCORES FOR EVERY POINT]: Every point")
#for point in points:
#    print(f"SCORE: {referenceCardinalScore(findFace(center,point),cardinals,point)}")
print("[PRINTING BEST 3 SCORES FOR CIRCLE]: Using every point")
print(f"TOP1: -> X:{TOPBestScores(points)[0].getX()} Y:{TOPBestScores(points)[0].getY()};\nTOP2: -> X:{TOPBestScores(points)[1].getX()} Y:{TOPBestScores(points)[1].getY()};\nTOP3: -> X:{TOPBestScores(points)[2].getX()} Y:{TOPBestScores(points)[2].getY()}.")