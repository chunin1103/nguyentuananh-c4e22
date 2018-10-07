quiz = {
    "stimulus": "Answer the following algebra questions:",
    "stem": "If x = 8, then what is the value of 4(x + 3)? ",
    "choices": ["1.35","2.36","3.40","4.44"],
    "right_choice": 4,
}
print(quiz["stimulus"])
print(quiz["stem"])   
print(*quiz["choices"], sep ="\n")

answer = int(input("And your choice is: "))

if answer == quiz["right_choice"]:
    print("Bingo ringo")
else:
    print(":(")