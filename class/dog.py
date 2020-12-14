#!/usr/bin/python
# coding=utf-8


class Dog(object):
    """模拟一只小狗"""

    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def sit(self):
        """模拟小狗被命令蹲下时"""
        print(self.name.title() + " is now sitting. ");

    def roll_over(self):
        """模拟小狗被命令打滚时"""
        print(self.name.title() + " rolled over!");

    def get_desc(self):
        return(self.name + str(self.age));


my_dog = Dog("kate", 6);
print("My dog's name is " + my_dog.name.title() + ".");
print("My dog is " + str(my_dog.age) + " years old.");
my_dog.sit();
my_dog.roll_over();

your_dog = Dog('lily',1);
print("Your dog's name is " + your_dog.name.title() + ".");
print("Your dog is " + str(your_dog.age) + " years old.");
your_dog.age=2;
your_dog.sit();
your_dog.roll_over();
print(your_dog.get_desc());