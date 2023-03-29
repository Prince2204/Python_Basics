#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        #distance=d = √[(x2 − x1)2 + (y2 − y1)2]
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5        
    
    def slope(self):
        #slope=(y2-y1)/(x2-x1)
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1)/(x2-x1)

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

l1=Line(coordinate1,coordinate2)
print("coordinates are : ",l1.coor1,l1.coor2)
print("Distance between two points: ",l1.distance())
print("Slope is: ",l1.slope())
