""" class Easy:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "="*len(other.cont)
        print ('\n'.join([self.cont, line, other.cont]))

a = Easy("First line")
b = Easy("Second line")

a/b """