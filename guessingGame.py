import random

def guess_the_number():
    secret_number = random.randint(1, 9)
    

    for attempt in range(1, 6):
        guess = int(input(f"Attempt {attempt}: Guess the number (between 1 and 9): "))
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempts.")
            break
        else:
            
            difference = abs(secret_number - guess)
            
            if difference <= 2:
                print("Hint: You are very close!")
            elif difference <= 5:
                print("Hint: You are close.")
            else:
                print("Hint: You are far.")

    else:
        print(f"Sorry, you've run out of chances. The correct number was {secret_number}.")


guess_the_number()
