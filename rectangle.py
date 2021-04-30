from __future__ import annotations
from point import Point
import matplotlib.pyplot as plt
from random import random

class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def contains(self,point:Point)->bool:
        check1=point.x>=self.x-self.w/2 
        check2=point.x<=self.x+self.w/2 
        check3=point.y<=self.y+self.h/2 
        check4=point.y>=self.y-self.h/2 
        return check1 and check2 and check3 and check4
    def intersects(self,rect:Rectangle)->bool:
        return not (
            self.x+self.w/2 < rect.x-rect.w/2 or 
            self.x-self.w/2 > rect.x+rect.w/2 or 
            self.y+self.h/2 < rect.y-rect.h/2 or 
            self.y-self.h/2 > rect.y+rect.h/2
            )
    def showRect(self):
        x0=self.x-self.w/2
        y0=self.y-self.h/2
        x1=self.x+self.w/2
        y1=self.y-self.h/2
        x2=self.x+self.w/2
        y2=self.y+self.h/2
        x3=self.x-self.w/2
        y3=self.y+self.h/2
        color=[random(),random(),random()]
        plt.plot([x0,x1,x2,x3,x0],[y0,y1,y2,y3,y0],color=color)
    def printSelf(self):
        x0=self.x-self.w/2
        y0=self.y-self.h/2
        x1=self.x+self.w/2
        y1=self.y-self.h/2
        x2=self.x+self.w/2
        y2=self.y+self.h/2
        x3=self.x-self.w/2
        y3=self.y+self.h/2
        print('(',x0,y0,')','(',x1,y1,')','(',x2,y2,')','(',x3,y3,')')

            