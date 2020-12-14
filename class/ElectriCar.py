#!/usr/bin/python
# coding=utf-8


from Car import Car;


# 类的继承
class ElectriCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


# define a object from super class
my_tesla = ElectriCar('tesla', 'models', 2016);
# call the method of super class
print(my_tesla.get_descriptive_name());