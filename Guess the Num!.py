import random

guess = input("Type a Number: ")

if guess.isdigit():
    guess = int(guess)

    if guess <= 0:
        print("Put a larger number than 0!")
        quit()
else:
    print("Please put a number!")
    quit()


num = random.randint(0, guess)
times_rolled = 0

while True:
    times_rolled +=1
    guessing = input("Make a guess: ")
    if guessing.isdigit():
        guessing = int(guessing)
    else:
        print("Put a number NOT a WORD!")
        continue

    if guessing == num:
        print("You've Got the Correct Number! ")
        break
    else:
        if guessing < guess:
            print("You need a lower value")
        else:
            print("You need a higher value")

print("You got the correct answer after rolling: ", str(times_rolled))

