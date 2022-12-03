# import module
import random
from art import logo
from art import vs
from game_data import data

# score = 0


def start():    # start game
    print(logo)
    game(score=0)   # set starting score

def game(score):
    random_data = random.choice(data)   # choose random data
    """print data information"""
    print(f"Compare A: {random_data['name']}, {random_data['description']}, from {random_data['country']}")
    num = random_data['follower_count'] # first number
    print(vs)
    random_target = random.choice(data) # choose random data
    while random_target == random_data: # if two data is same, change target data
        random_target = random.choice(data)
    """print data information"""
    print(f"Against B: {random_target['name']}, {random_target['description']}, from {random_target['country']}")
    c_num = random_target['follower_count'] # second number
    compare(num, c_num, score)

def compare(num, c_num, score):     # compare first and second number 
    comp = input("Who has more followers? Type 'A' or 'B': ")
    if comp == 'A':
        if num > c_num:
            score += 1  # if answer is right, plus one score
            next(score)
        else:
            print(f"Sorry, that's wrong. Final score: {score}") # if answer is wrong, print final score
    elif comp == 'B':
        if num < c_num:
            score += 1
            next(score)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        compare(num, c_num)

def next(score):
    print(logo)
    print(f"You're right! Current score: {score}")
    game(score)

start()