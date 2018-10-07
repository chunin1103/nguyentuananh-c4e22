person = {
    'name': 'Donald Trump',
    'role': 'president',
    'asshole': True,
    'cars': 10000,
}
print(person)

n = input("Want a D or an U? ")

if n.upper() == 'D':
    delete = input("What key do you want to del? ")
    if key not in person:
        print("Not found, sr")
    else:
        del person[delete]
        print(person)

elif n.upper() == 'U':
    key = input("What key do you want to replace? ")
    value = input("Add sth? ")
    person[key] = value
    print(person)

else: 
    print("Only a D or an U, bitch")
