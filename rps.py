import random

def get_player_choice():
    while True:
        player = input("Choose rock, paper, or scissors: ").lower()
        if player in ['rock', 'paper', 'scissors']:
            return player
        print("Invalid choice. Please try again.")

def get_computer_choice():

    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

def play_game():

    player_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - Player: {player_score} | Computer: {computer_score}")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Score:")
            print(f"Player: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("You won the game!")
            elif computer_score > player_score:
                print("Computer won the game!")
            else:
                print("The game ended in a tie!")
            break

# Start the game
print("Welcome to Rock-Paper-Scissors!")
play_game()