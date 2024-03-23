class Cylinder():

    p = 3.14
    
    def __init__(self,height=1,radius=1):
    
        self.radius=radius
        self.height=height
    
    def volume(self):
        
        v = Cylinder.p*(self.radius**2)*self.height
    
        return v
    
    def surface_area(self):
        
        A = (2*Cylinder.p*self.radius*self.height) + (2*Cylinder.p * (self.radius**2))

        return A
    
c = Cylinder(2,3)

c.volume()

c.surface_area()