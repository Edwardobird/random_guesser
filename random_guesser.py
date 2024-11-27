import random

random_number = random.randint(1, 100)
print(random_number)

def selectDiff():
    print('''Please select your difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)''')
    difficulty = input("Select by typing the number: (1/2/3) \n").strip()
    check = True
    while(check):
        if difficulty not in ['1','2','3']:
            difficulty = input("Wrong input! \n Select by typing the number: (1/2/3)").strip()
            continue
        else:
            check = False
    return int(difficulty)

def againFunc(game_running, num_of_chances):
    game_run = game_running
    num_of_chance = num_of_chances
    againBool = True
    new_rand = random.randint(1, 100)
    while (againBool):
        user_input = input("Play again? (Y/N)")
        cleaned_input = user_input.strip()
        if len(cleaned_input) != 1 or cleaned_input.lower() not in ['y', 'n']:
            print("Invalid input")
            continue
        elif cleaned_input.lower() == 'y':
            game_run = True
            difficulty = selectDiff()
            num_of_chance = diff_dict[difficulty]
            againBool = False
        elif user_input.lower() == 'n':
            game_run = False
            againBool = False
    return game_run, num_of_chance, new_rand
print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')
difficulty = selectDiff()
print(f"You selected: {difficulty}")
game_running = True
diff_dict = {1:10,2:5,3:3}
num_of_chances = diff_dict[int(difficulty)]
while(game_running):
    user_guess = int(input("Guess a number between 1-100\n").strip())
    if not isinstance(user_guess,int) or (user_guess < 1 or user_guess >100):
        print("Incorrect input, try again")
        continue
    if user_guess > random_number:
        print(f'The number is smaller than {user_guess}')
        num_of_chances -= 1
    elif user_guess < random_number:
        print(f'The number is larger than {user_guess}')
        num_of_chances -= 1
    else:
        print("You got it! Do you want to play again?")
        game_running,num_of_chances,random_number = againFunc(game_running,num_of_chances)
        #End of again
    if (game_running):
        print(f'You have {num_of_chances} chances remaining')
    else:
        break
    if num_of_chances == 0:
        print(f"You lost, again? \nThe number is {random_number}\n")
        game_running,num_of_chances,random_number = againFunc(game_running,num_of_chances)
#EOF
        