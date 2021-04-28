class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def contains(self,point):
        check1=point.x>=self.x-self.w/2 
        check2=point.x<=self.x+self.w/2 
        check3=point.y<=self.y+self.h/2 
        check4=point.y>=self.y-self.h/2 
        return check1 and check2 and check3 and check4
            