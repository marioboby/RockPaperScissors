import random

def win_check(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r') :
        return True


def game():

    isRunning = True
    while isRunning:
        choices = ['r' , 'p', 's']
                
        user = input("Choose --> 'r' for rock, 'p' for paper, 's' for scissors: ")

        while user not in choices :
            user = input("Please Enter a Valid choice: ")

        computer = random.choice(choices)

        print(f"Player: {user}")
        print(f"Computer: {computer}")

        if user == computer:
            print("Draw!")
        
        elif win_check(user,computer):
            print("You Won!")
        
        else:
            print("Computer Won!")

        if not input("Play again ? ('y' for YES, otherwise for NO) ").lower() == 'y' :
            isRunning = False
    
    print("Thanks for playing!")



game()
