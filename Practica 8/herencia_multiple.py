class A:
    def __init__(self, x,z):
        self.x = x
        self.z = z  
        
    def incrementarXZ(self):
        self.x += 1
        self.z += 1 
        print(f"x: {self.x} , z: {self.z}")
        
    def incrementarZ(self):
        self.z += 1
        print(f"z: {self.z}")
        
class B:
    def __init__(self, y,z):
        self.y = y
        self.z = z
        
    def incrementarYZ(self):
        self.y += 1
        self.z += 1
        print(f"y: {self.y}, z: {self.z}")

    def incrementarZ(self):
        self.z += 1
        print(f"z: {self.z}")
    
class D(A,B):
    def __init__(self,x,y,z):
        A.__init__(self, x,z)
        B.__init__(self, y,z)
    
    def incrementarXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1
        print(f"x: {self.x}, y: {self.y} , z: {self.z}")
        
    
    
#main
d = D(5,10,3)
d.incrementarXZ()
d.incrementarZ()
d.incrementarZ()
d.incrementarYZ()
d.incrementarXYZ()
