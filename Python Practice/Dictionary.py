my_d = {
    'name': "Yash",
    'age': 22
}
print(my_d)
print(my_d['name'])
print(my_d['age'])

my_d['salary'] = 30000
print(my_d)

print(my_d.keys())
print(my_d.values())
print(my_d.items())

my_d.pop('age')
print(my_d)

my_d.popitem()
print(my_d)

my_d.update({'gender': "male"})
print(my_d)
