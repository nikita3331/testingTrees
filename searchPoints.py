import numpy as np
from point import Point
from random import random
from rectangle import Rectangle
from quadTree import QuadTree
from time import time_ns
import matplotlib.pyplot as plt
from rectangle import Rectangle

def createPoints(N):
    points=[]
    for i in range(0,N):
        points.append(Point(random()*200,random()*200))
    return points
def traditionalSearch(range,points):
    foundPoints1=[]
    for p in points:
        if range.contains(p):
            foundPoints1.append(p)
    return foundPoints1

def main():
    treeTimes=[]
    tradTimes=[]
    points=createPoints(50000)


#/////////////
    capacity=5000
    boundry=Rectangle(100,100,200,200)

    quad=QuadTree(boundry,capacity-1)
    for point in points:
        quad.insert(point)

#//////////

    for pointNum in range(1,100):
        querryRange=Rectangle(random()*40, random()*40, 100, 100)
        startTree=time_ns()

        foundPoints=[]
        quad.querry(querryRange,foundPoints)
        foundPoints=[p for p in foundPoints if p != None]
        endTree=time_ns()

        tradPoints=traditionalSearch(querryRange,points)
        endTradPoints=time_ns()
        treeTimes.append(endTree-startTree)
        tradTimes.append(endTradPoints-endTree)
    plt.plot(treeTimes,label='tree')
    plt.plot(tradTimes,label='tarditional')
    plt.legend()
    plt.show()
    # pointCordsX=[p.getCoords()[0] for p in points]
    # pointCordsY=[p.getCoords()[1] for p in points]
    # plt.scatter(pointCordsX,pointCordsY)
    # quad.show()
    # querryRange.showRect()
    # plt.show()





if __name__ == "__main__":
    main()