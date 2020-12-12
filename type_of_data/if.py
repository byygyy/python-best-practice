#!/usr/bin/python
# coding=utf-8

# simple example
names = ['robin', 'jack', 'lily'];
for name in names:
    if name == 'robin':
        print(name.upper());
    else:
        print(name);

# a will different with A
if 'a' == 'A':
    print('same');
else:
    print('different');

# if want to compare but ingore upper or lower
if 'a'.upper() == 'A':
    print('same');

# check 2 items different or not
if names[0] != 'lily':
    print("first item is not lily");

# check 2 numbers different or not
if 12 != 11:
    print("12 is different with 11")
if 12 >= 11:
    print("12 is more than 11")
if 11 == 11:
    print("11 == 11")

# check items with and/or
if 1 < 2 or 1 > 2:
    print("or");

if names[0] == 'robin' and names[1] == 'jack':
    print("and");

# check item in list
if 'robin' in names:
    print("robin in list");

# check item not in list
if 'tom' not in names:
    print("tom not in list");

# check bool
game_running = True
can_edit = False
if game_running is True and can_edit is False:
    print("correct");

# if-elif-else
if names[0] == 'robin':
    print("1st is robin");
elif name[0] == 'ivy':
    print("1st is ivy");
else:
    print("1st is not robin and ivy")

# check list is empty or not
if names:
    print("names not empty");
names2 = []
if names2:
    print("names2 not empty");
else:
    print("names2 empty");