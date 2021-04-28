from rectangle import Rectangle
import matplotlib.pyplot as plt

class QuadTree:
    def __init__(self,boundry,capacity):
        self.boundry=boundry
        self.capacity=capacity
        self.points=[]
        self.divided=False
        self.ne=None
        self.nw=None
        self.sw=None
        self.se=None
    def subdivide(self):
        currX=self.boundry.x
        curry=self.boundry.y
        currW=self.boundry.w
        currH=self.boundry.h
        neBoundry=Rectangle(currX+currW/4,curry+currH/4,currW/2,currH/2)
        nwBoundry=Rectangle(currX-currW/4,curry+currH/4,currW/2,currH/2)
        swBoundry=Rectangle(currX-currW/4,curry-currH/4,currW/2,currH/2)
        seBoundry=Rectangle(currX+currW/4,curry-currH/4,currW/2,currH/2)

        self.ne=QuadTree(neBoundry, self.capacity)
        self.nw=QuadTree(nwBoundry, self.capacity)
        self.sw=QuadTree(swBoundry, self.capacity)
        self.se=QuadTree(seBoundry, self.capacity)
        self.divided=True


    def insert(self,point):
        if not self.boundry.contains(point):
            return True
        if len(self.points)<self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()
            if self.ne.insert(point):
                return True
            if self.nw.insert(point):
                return True
            if self.sw.insert(point):
                return True
            if self.se.insert(point):
                return True
    def show(self):
        x0=self.boundry.x-self.boundry.w/2
        y0=self.boundry.y-self.boundry.h/2
        x1=self.boundry.x+self.boundry.w/2
        y1=self.boundry.y-self.boundry.h/2
        x2=self.boundry.x+self.boundry.w/2
        y2=self.boundry.y+self.boundry.h/2
        x3=self.boundry.x-self.boundry.w/2
        y3=self.boundry.y+self.boundry.h/2
        plt.plot([x0,x1,x2,x3,x0],[y0,y1,y2,y3,y0])
        if self.divided:
            self.se.show()
            self.sw.show()
            self.ne.show()
            self.nw.show()
            
