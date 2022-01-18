class Window:
    def __init__(self,x1,y1,x2,y2):
        self.xwmin = x1
        self.ywmin = y1
        self.xwmax = x2
        self.ywmax = y2

class Ponto:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


class Reta:
    def __init__(self):
        self.pontos = []
    def addponto(self,p):
        self.pontos.append(p)


class Poligono:
    def __init__(self):
        self.pontos = []
    def addponto(self,p):
        self.pontos.append(p)