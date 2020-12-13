#!/usr/bin/python
# coding=utf-8

# a simply dict and access it
guys_0 = {"name": "robin", "age": 22};
print(guys_0);
print(guys_0["name"]);
print(guys_0["age"]);

# add new item for dict
guys_0["city"] = "xi'an";
print(guys_0);

# create a empty dict and add new item
guys_1 = {};
guys_1["name"] = "jack";
print(guys_1)

# modify the key:value
guys_0["city"] = 'shanghai';
print(guys_0)

# delete item of dict
del guys_0["city"];
print(guys_0);

# define a dict like object
favorite_language = {
    'jen': 'java',
    'robin': 'python'
}
print(favorite_language);
print("robin's favorite language is " +
      favorite_language['robin']
      );


# list a dict all key/value
user_0 = {
    "username": "robin",
    "age": 22,
    "city": "xi'an"
};
for key, value in user_0.items():
    print("\nkey is " + key);
    print("value is " + str(value));

# list a dict all key no sorted
for key in user_0.keys():
    print("\nkey is " + key);
# list a dict all key sorted
for key in sorted(user_0.keys()):
    print("\nkey is " + key);

# list a dict all value can show duplicate item
for value in user_0.values():
    print("\nvalue is " + str(value));
# list a dict all value duplicate item show once
for value in set(user_0.values()):
    print("\nvalue is " + str(value));

# dict nested in list
machines = [];
for i in range(30):
    machines.append({"name": "joe", "color": "green"});
print(machines);

for i in machines[:3]:
    i["color"]= "red";
print(machines[:3]);

# list nested in dict
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
};
print(pizza);

# dict nested in dict
users = {
    'robin': {
        "name": "robin",
        "age": 22
    },
    'joe': {
        "name": "joe",
        "age": 21
    }
}
print(users);
for name in users.keys():
    print("name is " + name);