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
    print("Welcome to Rock-Paper-Scissors!")
    
    
    while True:
        try:
            max_rounds = int(input("Choose game length (3 or 5 rounds): "))
            if max_rounds in [3, 5]:
                break
            print("Please enter either 3 or 5")
        except ValueError:
            print("Please enter a valid number")
    
    player_score = 0
    computer_score = 0
    round_num = 1
    
    while round_num <= max_rounds:
        print(f"\n--- Round {round_num} of {max_rounds} ---")
        print(f"Current Score - Player: {player_score} | Computer: {computer_score}")
        
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
        
        
        needed_to_win = (max_rounds // 2) + 1
        if player_score >= needed_to_win or computer_score >= needed_to_win:
            break
            
        round_num += 1
    
    
    print("\n=== GAME OVER ===")
    print(f"Final Score - Player: {player_score} | Computer: {computer_score}")
    
    if player_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("😢 The computer won the game. Better luck next time!")
    else:
        print("🤝 It's a tie game!")
    
    
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'")
    
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()