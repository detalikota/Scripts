class Decor():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print ("something")
        return self.func(*args, **kwargs)

@Decor
def display():
    print ('yo')

display()