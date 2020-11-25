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


def func(original_function):
  def wrapper(*args, **kwargs):
    print ("LUL")
    original_function(*args, **kwargs)
    print ("LUL")
  return wrapper

@func
def lul(name, age):
  print (name, age)

lul("Magomed", 25)