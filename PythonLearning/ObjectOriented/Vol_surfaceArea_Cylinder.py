#Volume and surface area of cylender
#volume=pi*r^2*h
#surface area=2*pi*r*h+2*pi*r^2

class Cylinder:

    pi=3.14
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return Cylinder.pi*self.radius**2*self.height
    
    def surface_area(self):
        return (2*Cylinder.pi*self.radius*self.height+2*Cylinder.pi*self.radius**2)

c = Cylinder(2,3)
print("radius of cylinder is {} and height is {}".format(c.radius,c.height))
print("Volume of Cylinder is {} and surface area is {}".format(c.volume(),c.surface_area()))
