import numpy as np
from point import Point
from random import random
import matplotlib.pyplot as plt
def createPoints(N):
    points=[]
    for i in range(0,N):
        points.append(Point(random(),random()))
    return points
def main():
    points=createPoints(100)
    pointCordsX=[p.getCoords()[0] for p in points]
    pointCordsY=[p.getCoords()[1] for p in points]

    plt.scatter(pointCordsX,pointCordsY)
    plt.show()





if __name__ == "__main__":
    main()