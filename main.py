from dicegame import *

game = DiceGame()

def dice_main(username):
    while True:
        print("\n=== Dice Roll Game!! ===\n")
        print(f"Welcome, {username}")
        print("1. Play Game")
        print("2. Top Scores")
        print("3. Log out")

        choice = input("\nEnter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                game.play_game()
            elif choice == 2:
                game.display_top_scores()
            elif choice == 3:
                print("\nLogging Out...")
                return  # Exit the dice_main function
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    while True:
        print("=== Welcome to Dice Roll Game!! ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                username = input("Enter your username or leave blank to cancel:  ")
                if username == '':
                    print("Cancelled...")
                    continue  # Go back to the main menu
                if len(username) < 4:
                    print("Username should be at least 4 characters long.")
                    continue 
                password = input("Enter your password or leave blank to cancel: ")
                if password == '':
                    print("Cancelled...")
                    continue
                if len(password) < 8:
                    print("Password should be at least 8 characters long.")
                    continue 
                if game.users.register(username, password):
                    print("\nRegistration Successful!")
                else:
                    print("\nUsername already exists.")
            elif choice == 2:
                username = input("Enter your username or leave blank to cancel:  ")
                if username == '':
                    print("Cancelled...")
                    continue
                password = input("Enter your password or leave blank to cancel: ")
                if password == '':
                    print("Cancelled...")
                    continue
                if game.users.login(username, password):
                    game.player = username
                    print("Login Successful!")
                    dice_main(username)
                else:
                    print("\nInvalid username or password")
            elif choice == 3:
                print("\nExiting...")
                break  # Exit the main function
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError as e:
            print(f"\nError: {e}.")

if __name__ == "__main__":
    main()
