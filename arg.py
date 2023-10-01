
#workimn with many arguments using the *args mainly a positional argument
def add(*args):
    print(args[1])
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,5,4,7,8,9)

#workimn with many arguments using the **kwargs mainly a keyword argument
def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    #for n in kwargs:
     #   print(kwargs[n])
    
calculate(2,add=3, multiply=5)

#using kwargs in classes
class Car:
    def __init__(self, **kwarg):
        self.make = kwarg["make"]
        self.model = kwarg["model"]
        
my_car = Car(make="Bugatti", model="GT-R")
print(my_car.make)

    