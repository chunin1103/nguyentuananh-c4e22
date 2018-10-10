person = {
    'name': 'Quan',
    'age': 22,
    'locat': 'Hanoi2'

}

for x in person:
    print(x)
    print()

for k in person.keys():
    print(k, person[k])
print()

for v in person.values():
    print(v)
print("------------------")

for k,v in person.items():
    print(k, v, sep=": ")