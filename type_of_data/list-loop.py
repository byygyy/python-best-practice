#!/usr/bin/python
# coding=utf-8

names = ['robin', 'joe', 'john'];


# loop a list
for name in names:
    print(name);
# loop a list and print with string together
for name in names:
    print("i am " + name.title());
print("thanks everyone");

# create number range and loop
for value in range(1,5):
    print(value);

# create number list and give it to a var
numbers = list(range(1, 6));
print(numbers);

# create number list with len and give it to a var
numbers2 = list(range(1, 7, 2));
print(numbers2);

squares =[];
for value in range(1,5):
    squares.append(value**2);
print(squares);

# get max/min item or sum of list
print(max(numbers));
print(min(numbers));
print(sum(numbers));

# create a list quickly
squares=[value**2 for value in range(1, 11)];
print(squares);

# cut a list and show it
print(names[0:2]);
print(names[1:2]);
print(names[:2]);
print(names[0:]);

# loop cut content
for number in names[0:2]:
    print(number);

# copy cut list, 2 list will different object
my_foods= ["cake", "pizza"];
friends_food=my_foods[:]
print(friends_food);
my_foods.append("ice");
friends_food.append("cannoli");
print(my_foods);
print(friends_food);

# if only give list1 to list2, will same object
my_foods1= ["cake", "pizza"];
friends_food1= my_foods1;
my_foods1.append('ice');
friends_food1.append('cannoli');
print(my_foods1);
print(friends_food1);
