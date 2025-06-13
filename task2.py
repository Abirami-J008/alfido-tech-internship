import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Ask the user for their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is valid
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Check if the guess is correct
            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif user_guess < number_to_guess:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        number_guessing_game()
        play_again = input("Would you like to play again? (y/n): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
