def logger(func):
  def wrapper_function(a =0):
    result = func(a + b)
    return result
  return wrapper_function

@logger
def summator(b):
  return sum(b)

summator(4)
