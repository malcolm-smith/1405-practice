trivia = {
    "What is the capital of Canada: ": ["OTTAWA"],
    "What is the capital of Ontario: ": ["TORONTO"],
    "Carleton is superior to Ottawa U:": ["YES", "TRUE"]
}

score = 0
for question in trivia:
    if input(question).upper() in trivia[question]:
        print('CORRECT')
        score += 1
    else:
        print('INCORRECT')

print('\nYou got %d of %d questions right!' % (score, len(trivia)))
