import numpy as np
from point import Point
from random import random
from rectangle import Rectangle
from quadTree import QuadTree
import time
import matplotlib.pyplot as plt
def createPoints(N):
    points=[]
    for i in range(0,N):
        points.append(Point(random()*200,random()*200))
    return points
def main():
    points=createPoints(5000)
    pointCordsX=[p.getCoords()[0] for p in points]
    pointCordsY=[p.getCoords()[1] for p in points]


    boundry=Rectangle(100,100,200,200)
    quad=QuadTree(boundry,4)

    for point in points:
        plt.scatter(point.x, point.y)
        quad.insert(point)
    quad.show()
    plt.show()
    # plt.scatter(pointCordsX,pointCordsY)
    # plt.show()





if __name__ == "__main__":
    main()