#!/usr/bin/python
# coding=utf-8


# 基本类的定义和调用，包括类方法、类属性的定义和访问。
class Car():

    def __init__(self, make, model, year):
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0;

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " +str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage;
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage;
        else:
            print("You can't roll back an odometer!");

    def increment_odometer(self, miles):
        self.odometer_reading += miles;


# define a object as my_new_car
my_new_car = Car('audi', 'a4', 2016);
print(my_new_car.get_descriptive_name());

# call a method of class
my_new_car.read_odometer();

# if you want to modify the attributes of class
my_new_car.odometer_reading = 23;
my_new_car.read_odometer();

# if you want to modify the attributes by method in the class
my_new_car.update_odometer(25);
my_new_car.read_odometer();

# if you want to increase odometer only
my_new_car.increment_odometer(100);
my_new_car.read_odometer();