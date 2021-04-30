from rectangle import Rectangle
import matplotlib.pyplot as plt
import numpy as np
class QuadTree:
    def __init__(self,boundry:Rectangle,capacity:int):
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
        nextW=currW/2
        nextH=currH/2
        offsetW=currW/4
        offsetH=currH/4
        neBoundry=Rectangle(currX+offsetW,curry+offsetH,nextW,nextH)
        nwBoundry=Rectangle(currX-offsetW,curry+offsetH,nextW,nextH)
        swBoundry=Rectangle(currX-offsetW,curry-offsetH,nextW,nextH)
        seBoundry=Rectangle(currX+offsetW,curry-offsetH,nextW,nextH)
        self.ne=QuadTree(neBoundry, self.capacity)
        self.nw=QuadTree(nwBoundry, self.capacity)
        self.sw=QuadTree(swBoundry, self.capacity)
        self.se=QuadTree(seBoundry, self.capacity)
        self.divided=True


    def insert(self,point):
        if not self.boundry.contains(point):
            return False

        if len(self.points)<self.capacity and self.nw==None:
            self.points.append(point)
            return True
        if self.nw==None:
            self.subdivide()

        if self.nw.insert(point):
            return True
        if self.sw.insert(point):
            return True
        if self.se.insert(point):
            return True
        if self.ne.insert(point):
            return True
        return False
    def querry(self,searchBoundry:Rectangle,pointsInRange):
        # searchBoundry.printSelf()
        # self.boundry.printSelf()
        # print('-----')
        if self.boundry.intersects(searchBoundry):
            for point in self.points:
                if(searchBoundry.contains(point)):
                    pointsInRange.append(point)
            if not self.nw==None:
                pointsInRange.append(self.nw.querry(searchBoundry,pointsInRange))
                pointsInRange.append(self.ne.querry(searchBoundry,pointsInRange))
                pointsInRange.append(self.se.querry(searchBoundry,pointsInRange))
                pointsInRange.append(self.sw.querry(searchBoundry,pointsInRange))
                pointsInRange = np.array(pointsInRange)
                pointsInRange.flatten()


    def show(self):
        self.boundry.showRect()
        if self.divided:
            self.se.show()
            self.sw.show()
            self.ne.show()
            self.nw.show()
    def plotOwnPoints(self):
        pXs=[p.x for p in self.points]
        pYs=[p.y for p in self.points]
        color=[0,0,0]
        plt.scatter(pXs, pYs,color=color)
    def countTrees(self,count=0):
        if self.divided:
            count+=self.nw.countTrees(count)
            count+=self.ne.countTrees(count)
            count+=self.se.countTrees(count)
            count+=self.sw.countTrees(count)
        else:
            count+=1
        return count
    def countTotalPoints(self):
        internalValue=len(self.points)
        if self.divided:
            internalValue+=self.nw.countTrees()
            internalValue+=self.ne.countTrees()
            internalValue+=self.se.countTrees()
            internalValue+=self.sw.countTrees()
        return internalValue
            
