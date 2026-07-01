import random


def play_game():
    print("=" * 40)
    print("🎯 WELCOME TO GUESS THE NUMBER GAME")
    print("=" * 40)

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too Low! Try Again.")

            elif guess > secret_number:
                print("📈 Too High! Try Again.")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the number {secret_number} correctly.")
                print(f"Total Attempts: {attempts}")
                break

        except ValueError:
            print("❌ Please enter a valid integer.")

    while True:
        choice = input("\nDo you want to play again? (Y/N): ").strip().upper()

        if choice == "Y":
            print()
            play_game()
            return

        elif choice == "N":
            print("\n👋 Thank you for playing!")
            return

        else:
            print("Please enter Y or N.")


if __name__ == "__main__":
    play_game()