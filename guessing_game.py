import random
import statistics

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    high_score = 0
    
    while True:
        winning_number = random.randint(1, 100)
        print(f'Can you beat the current high score of {high_score} attempts?')
        attempts = []
        while True:
            try:
                guess = int(input("Take a guess: "))
                if guess < 1 or guess > 100:
                    print("Your guess is outside the range of 1-100. Try again.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue
            
            attempts.append(guess)
            if guess < winning_number:
                print("It's higher.")
            elif guess > winning_number:
                print("It's lower.")
            else:
                print(f"Congratulations! You guessed the number in {len(attempts)} attempts.")
                if len(attempts) < high_score:
                    high_score = len(attempts)
                    print(f"New high score! {len(attempts)} attempts.")
                break
                    
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != 'y':
            print("Thanks for playing! Here's summary of your game:")
            print(f"Number of guesses: {len(attempts)}")
            print(f"Mean of guesses: {statistics.mean(attempts)}")
            print(f"Median of guesses: {statistics.median(attempts)}")
            print(f"Mode of guesses: {statistics.mode(attempts)}")
            break  # Exit the game when the player chooses not to play again
        
start_game()