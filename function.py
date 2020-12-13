#!/usr/bin/python
# coding=utf-8


# define a simply function
def greet_user():
    print("hello!");
greet_user();


# define a function with a parameter
def greet_user2(username):
    print("hello " + username);
greet_user2('robin');


# define a function with 2 parameters without default value
def greet_user3(username, age):
    print("hello " + username + "\nage is " + str(age));
greet_user3('robin',21);
greet_user3(age=22, username="robinhhli");


# define a function with 2 parameters with default value
def greet_user4(username="lily", age=22):
    print("hello " + username + "\nage is " + str(age));
greet_user4();
greet_user4("jack", 23);
greet_user4(username="jason");
greet_user4(age="24");


# define a function with 2 parameters with default value, parameter without default value first
def greet_user5(username, age=22):
    print("hello " + username + "\nage is " + str(age));
greet_user5("robin");
greet_user5("robin", 23);


# define a function and return a value
def greet_user6(first_name, lastname):
    return( first_name + lastname).title();
name= greet_user6("robin", "hhli");
print(name)


# define a function and return a dict
def greet_user7(first_name, lastname):
    person = {'first': first_name, 'last': lastname};
    return person
name= greet_user7("robin", "hhli");
print(name)


# call a function in while
while True:
    print("\nplease input your first_name:");
    f_name=input("First name: ");
    if f_name == 'q':
        break;
    l_name=input("Last name: ");
    if l_name == 'q':
        break;
    fullname= greet_user6(f_name, l_name);
    print(fullname);


# define a function, parameters are list
def greet_user8(names):
    for name in names:
        msg = "welcom "+ name;
        print(msg);
names = ['robin', 'joe'];
greet_user8(names); # give a list, it will be changed, if needed
greet_user8(names[:]); # give a list copy, it will not changed


# define a function and can receive any parameters to tuple
def get_foods(*toppings):
    print(toppings);
    for topping in toppings:
        print(topping);
get_foods("pizza", "ice");


# define a function and can receive 1 parameter and any parameters to tuple
def get_foods(number, *toppings):
    print(toppings);
    for topping in toppings:
        print(topping);
    print("food count is "+ str(number));
get_foods(2,"pizza", "ice");


# define a function and receive 2 parameters and any 1 dict parameter
def get_profile(first, last, **userinfo):
    profile = {};
    profile["first"] = first;
    profile["last"] = last;
    for key,value in userinfo.items():
        profile[key] = value;
    print(profile);
get_profile('li', 'huanhuan', age=22, city='shanghai');