#!/usr/bin/python
# coding=utf-8

# get string from user
name = input("please input your name: ");
print("hello " + name);
# if need compare with int, need int(string)
age = input("please input your age: ");
age = int(age);
if age > 18:
    print("you need ticket");
elif age < 18:
    print("you are young, no need ticket");


# if you are using python2.7, please use raw_input()
# input() will help you run a python command at python2.7

# use while loop check the user input
current_number = 1;
while current_number <=5:
    print(current_number);
    current_number += 1;
prompt = "please input any string, and will show you:";
prompt += "\nEnter exit to end the program. ";
message = "";
while message != 'exit':
    message = input(prompt);
    if message != 'exit':
        print(message);

# use while with break
prompt = "please input your city, and will show you:";
prompt += "\nEnter exit to end the program. ";
while True:
    city = input(prompt);
    if city == 'exit':
        break;

# use while with continue
current_number = 0;
while current_number < 10:
    current_number += 1;
    if current_number % 2 == 0:
        continue;
    print(current_number)

count = 0;
while True:
    print("hello world!")
    count += 10000000000;
    print(count);
