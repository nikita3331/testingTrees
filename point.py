class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def printSelf(self):
        print(self.x,self.y)
    def getCoords(self):
        return (self.x,self.y)