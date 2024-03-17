from art_compare import logo, vs
import random
import os
from game_data import data


def number_a(compare_data):
    name, follower_count, description, country = compare_data.values()
    print(f"Compare A: {name}, a {description}, from {country}.")   
    return follower_count

def number_b(against_data):
    name, follower_count, description, country = against_data.values()
    print(f"Against B: {name}, a {description}, from {country}.")   
    return follower_count

print(logo)
compare_a = random.choice(data)
number_a(compare_a)

print(vs)

against_b = random.choice(data)
number_b(against_b)

user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

current_score = 0

while True:
    if user_guess == 'a':
        if compare_a["follower_count"] > against_b["follower_count"]:
            current_score += 1
            os.system('clear')
            print(logo)
            print(f"You're right! Current score: {current_score}.")
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break

    elif user_guess == 'b':
        if compare_a["follower_count"] < against_b["follower_count"]:
            current_score += 1
            os.system('clear')
            print(logo)
            print(f"You're right! Current score: {current_score}.")  
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break
        
    else:
        os.system('clear')
        print(logo)

    compare_a = random.choice(data)
    number_a(compare_a)

    print(vs)

    against_b = random.choice(data)
    number_b(against_b)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()


