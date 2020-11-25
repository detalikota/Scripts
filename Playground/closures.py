import logging
logging.basicConfig(filename='logs.log', level=logging.INFO)
def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print (func(*args))
    return log_func

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
x = logger(add)
y = logger(sub)

x(3,5)
y(5,3)