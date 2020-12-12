#!/usr/bin/python
# coding=utf-8

list1 = ['robin', 'joe', 'john'];
list2 = []

# read a list
# got the whole list
print(list1);
# got the first item of list
print(list1[0]);
# got the second item of list
print(list1[1].title());
# got the last item of list
print(list1[-1]);
# give list item to new var
name = list1[0];
print(name);

# update any item of list
list1[0] = 'lily';
print(list1);

# add new item at the end of the list
list1.append('ivy');
print(list1);
list2.append('jack');
print(list2);

# insert new item in the list
list1.insert(0, 'alex');
print(list1);

# remove current item from list
del list1[-1];
print(list1);

# remove last item from list and get it
print(list1.pop())
print(list1)

# remove any item by index from list and get it
print(list1.pop(1));
print(list1);

# remove any item by value 1 time from list and get it
print(list1.remove('alex'));
print(list1);

# sort for list forever
list3 = ['ab', 'cd', 'ef', '1'];
print(list3);
list3.sort();
print(list3);
list3.sort(reverse=True);
print(list3);

# sort for list but does not change it
print(sorted(list3));
print(list3);

# reverse a list forever
list3.reverse();
print(list3);
list3.reverse();
print(list3);

# get length of list
print(len(list3));