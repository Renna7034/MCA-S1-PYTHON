class circle:
    def __init__(self,r):
        self.rad=r
    def parameter(self):
        return 2*3.14*self.rad
    def area(self):
        return 3.14*self.rad*self.rad
r1=int(input('enter the radius of first circle'))
obj_circle1=circle(r1)
a1=obj_circle1.area()
p1=obj_circle1.parameter()
print('area and parameter of first circle is ',a1,'and',p1)
r2=int(input('enter the radius of 2nd circle'))
obj_circle2=circle(r2)
a2=obj_circle2.area()
p2=obj_circle2.parameter()
print('area and parameter of first circle is ',a2,'and',p2)
if a1>a2:
    print('area of c1 is bigger')
else:
    print('area of c2 is bigger')
if p1>p2:
    print('parameter of c1 is bigger')
else:
    print('parameter of c2 is bigger')
    


