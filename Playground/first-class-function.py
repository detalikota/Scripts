""" def square(x):
    return x*x

def square_all(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

x = square_all(square, [1,2,3,4,5])

print(x) """


""" 
def a(msg):
    def b():
        print ("LOG:", msg)
    return b

a = a("hi")
a() """



def html(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text

h1 = html("h1")
h1("sdfaskjf")
p = html("p")
p("sldfkjlsdjf")