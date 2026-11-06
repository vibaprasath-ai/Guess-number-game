import random

def Guess(number):
    random_value = random.randint(1,10)
    guess = None

    if(number < random_value):
        print(f"{number} is too low")

    elif(number > random_value):
        print(f"{number} is too high")

    else:
        print(f"guess {number} is correct, You Win")

while(True):
    print("\nGuess the number")
    print("--------------------")
    guess_number = int(input("Enter number between 1 to 10 :"))
    Guess(guess_number)