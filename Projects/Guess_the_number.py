import random  

logo = """
 ___  __  __  ____  ___  ___    ____  _   _  ____    _  _  __  __  __  __  ____  ____  ____ 
/ __)(  )(  )( ___)/ __)/ __)  (_  _)( )_( )( ___)  ( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \\
( (_-. )(__)(  )__) \__ \\__ \    )(   ) _ (  )__)    )  (  )(__)(  )    (  ) _ < )__)  )   /
 \___/(______)(____)(___/(___/   (__) (_) (_)(____)  (_)\_)(______)(_/\/\_)(____/(____)(_)\_)

"""                 

# game start
def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")   
    print("I'm thinking of a number between `1 and 100.")   # rule of the game.
    game()  # Load game method

# game define
def game():
    answer = random.randint(1, 100) # answer is a number between 1 and 100.
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")    # Choose the game difficulty
    # easy mode
    if diff == 'easy':  
        for i in range(10): # 10 times repeat
            print(f"You have {10-i} attempts remaining to guess the number.")
            guess = int(input("Make a guess: ")) # input your answer
            if guess == answer:
                print("Correct!")   # if your answer and real answer is correct
                return  # if you correct the answer. quit method
            elif guess > answer:
                print("Too high!")
                if i < 9:
                    print("Guess again.")
                else:   # if attempt is run out.
                    print("You've run out of guesses, You lose.")
                    print(f"The answer is {answer}")
            elif guess < answer:
                print("Too low!")
                if i < 9:
                    print("Guess again.")
                else:
                    print("You've run out of guesses, You lose.")
                    print(f"The answer is {answer}")

    elif diff == 'hard':
        for i in range(5):
            print(f"You have {5-i} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == answer:
                print("Correct!")
                return
            elif guess > answer:
                print("Too high!")
                if i < 4:
                    print("Guess again.")
                else:
                    print("You've run out of guesses, You lose")
                    print(f"The answer is {answer}")
            elif guess < answer:
                print("Too low!")
                if i < 4:
                    print("Guess again.")
                else:
                    print("You've run out of guesses, You lose")
                    print(f"The answer is {answer}")
    else:   # if user type wrong difiiculty
        ch = input("Do you want to quit the game? (y/n): ")
        if ch == 'y':
            print("Okay! See you again!")
            return 
        else:
            print("You must choose 'easy' or 'hard'")
            game()

guess_the_number()