count = 0
total_correct_ans = 0

quiz = {
    'stimulus': [
        'Answer the following algebra question:',
        'Estimate the answer (exact calculation not needed)'
        ],
    'stem'    : [
        'If x = 8, then what is the value of 4(x + 3) ?',
        'Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is this mean ?'
        ],
    'choices'  : [
        [35,36, 40, 44],
        ['About 55','About 65', 'About 75', 'About 85']
        ],
    'right_choice': [4,2]
}
#Quiz 1
print(quiz['stimulus'][0])
print(quiz['stem'][0])
print(*quiz['choices'][0], sep = "\n")
user_input = int(input('Your choice: '))
if user_input == 4:
    print('bingo')
    total_correct_ans += 1

else:
    print(':(')

#Quiz 2
print(quiz['stimulus'][1])
print(quiz['stem'][1])
print(*quiz['choices'][1], sep = "\n")
user_input = int(input('Your choice: '))
if user_input == 4:
    print('bingo')
    total_correct_ans += 1

else:
    print(':(')

print('You correctly answer', total_correct_ans, 'out of 2 questions')