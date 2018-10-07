# note below code
person = {
    "name": "TA",
    "age": 23
    
}

text    = input("What do you want to add? ")
pair    = text.split(",")
key, value = pair       # key     = pair[0]
                        # value   = pair[1]
                

person[key] = value

print(person)


# >>> text = "type, electric"
# >>> pair = text.split(",")
# >>> print(pair)
# ['type', ' electric']
# >>> print(type(pair))
# <class 'list'>
# >>> key = pair[0]
# >>> value = pair[1]
# >>> print(value
# ... )
#  electric
