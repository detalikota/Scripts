""" def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

@decor
def print_text():
  print("Hello world!")

print_text() """


""" def func(original_function):
  def wrapper(*args, **kwargs):
    print ("LUL")
    original_function(*args, **kwargs)
    print ("LUL")
  return wrapper

@func
def lul(name, age):
  print (name, age)

lul("Magomed", 25) """

""" def decorator(func):
  def wrapper(*args, **kwargs):
    print ("----------------")
    func(*args, **kwargs)
    print ("----------------")
  return wrapper

@decorator
def display():
  print ("yeah")

display() """

from functools import wraps
def logger(func):
  import logging
  logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)
  @wraps(func)
  def wrapper(*args, **kwargs):
    logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
    return func(*args,**kwargs)

  return wrapper

def timer(func):
  import time
  @wraps(func)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    result = func(*args, **kwargs)
    t2 = time.time() - t1
    print ('{} ran in: {} sec'.format(func.__name__, t2))
    return result
  return wrapper

import time
@logger
@timer
def display(name, age):
  """ time.sleep(1) """
  print('this function ran with arguments {} and {}'.format(name, age))


display("magomed", "25")