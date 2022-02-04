import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distanceFromAPoint(self, point2):
        distance = math.sqrt(abs(self.x - point2.x)**2+abs(self.y - point2.y)**2)
        return distance

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y