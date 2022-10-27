def decorator(func):
  def wrapper_function(*args, **kwargs):
    func(*args, **kwargs)
    print(*args, **kwargs)
  return wrapper_function

@decorator
def greet(name, a):
  print(F'привет {name}')
  print(F'число {a}')

greet("Анастасия", 10)


def logger(func):
  def wrapper_function(list_of_num):
    result = func(list_of_num)
    with open('log.txt', 'w') as f:
      f.write(str(result))
    return result
  return wrapper_function


@logger
def summator(list_of_num):
  return sum(list_of_num)

summator([1,2,3,4])


# Можем передать название файла, 
# куда будет происходить запись результата суммы

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

# Декоратор logger должен принимать имя файла и возвращать декоратор, 
# который принимает функцию и подменяет её функцией wrapped, как мы делали до этого

@logger('file_log.txt')
def summator(list_of_num):
    return sum(list_of_num)

summator([1,2,3,4])

class MyClass:
    counts = 0

    def __init__(self):
        MyClass.counts = MyClass.counts + 1

    @classmethod
    def classmethod(cls):
        print(cls.counts)


MyClass.classmethod()
mc1 = MyClass()
mc2 = MyClass()
mc3 = MyClass()

MyClass.classmethod()