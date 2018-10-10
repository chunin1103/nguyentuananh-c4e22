pokemon = {
    'name': 'aefafasdf',
    'owner': 'fuck you',
}

key = input("what? ")
if key not in pokemon:
    print("Not found")
else:
    value = pokemon[key]
    print(value)