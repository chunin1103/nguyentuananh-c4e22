user_input = input('Please enter your sentence: ')
sentence = user_input.lower()
char_count = {}

for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

all_chars = list(char_count.items())
all_chars.sort()

print(*all_chars, sep='\n')