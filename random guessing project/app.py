import random

# Writing a code to guess the random numbers


# def guess(x):
#     randomNUmber = random.randint(1, x)
#     guess = 0
#     while guess != randomNUmber:
#         try:
#             guess = int(input(f'Guess the number between 1 and {x}:'))
#             if guess < 1 or guess > 10:
#                 print("sorry! you are guessing out of range, guess between 1 and 10")
#             elif guess > randomNUmber:
#                 print("sorry!too high")
#             elif guess < randomNUmber:
#                 print("sorry! too low")
#         except ValueError:
#             print("Sorry! only numbers are allowed!")
#         except Exception as e:
#             print("Something went wrong!")
#     print("congrtulation! yes you guessed the right number")


# guess(10)


# computer guessing or secret number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            low = high

        feedback = input(
            f'Is {guess} too high (H) or too low (L) or correct (H)?').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f'yay! The computer your number {guess} correctly.')


computer_guess(10)
