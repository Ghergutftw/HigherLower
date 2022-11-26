import random

import art
from game_data import data


def format_data(account) :
    """"Return the formatted text"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} , from {account_country}"


def check_answer(guess, follower_count_a, follower_count_b) :
    """Return true if follower_count_a > follower_count_b , false otherwise"""
    if follower_count_a > follower_count_b and guess == "A" :
        return True
    elif follower_count_a > follower_count_b and guess != "A" :
        return False
    elif follower_count_b > follower_count_a and guess == "B" :
        return True
    elif follower_count_b > follower_count_a and guess != "B" :
        return False


# Display art
print ( art.logo )
score = 0
game_continues = True

account_b = random.choice ( data )

while game_continues :
    account_a = account_b
    account_b = random.choice ( data )

    while account_b == account_a :
        account_b = random.choice ( data )

    print ( f"Compare A :{format_data ( account_a )} " )

    print ( art.vs )

    print ( f"Compare B :{format_data ( account_b )} " )

    guess = input ( "Who has more followers ? A or B : " ).upper ()
    if guess == "STOP" :
        game_continues = False

    # print ( "Type STOP if you want to stop" )
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    is_correct = check_answer ( guess, follower_count_a, follower_count_b )

    if is_correct :
        print ( "CORRECT" )
        score = score + 1
        print ( f"Current score is : {score}" )
    else :
        print ( "WRONG" )
        game_continues = False
        print ( f"Your final score is : {score}" )
