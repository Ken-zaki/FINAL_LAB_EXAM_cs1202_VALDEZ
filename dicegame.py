import random
import os
from usermanager import UserManager
from score import Score

class DiceGame:
    def __init__(self): 
        self.users = UserManager() # To access usermanager function from usermanager.py
        self.player = None #to store information about the current user
        self.scores = {}  # to store scores in empty dictionary
        self.load_scores()  # Load scores when initializing

    def logout(self):
        self.player = None #indicate the user is being logged out. as None typically presence of absence of a value
        print("Logged out successfully.")

    def play_game(self):       
        user_score = 0
        cpu_score = 0 #to keep track of the scores for the user and cpu 
        rounds = 0
        while True:
            input("Press Enter to roll the dice...")
            for _ in range(3): # _ indicate that the value of the variable is not going to be used within the loop.
                user_roll = random.randint(1, 6) # generate a random dice roll both user and cpu
                cpu_roll = random.randint(1, 6)
                print(f"{self.player} rolled: {user_roll}")
                print("CPU rolled:", cpu_roll)
                if user_roll > cpu_roll: # to check whether who win the game
                    print(f"{self.player} wins this round!")
                    user_score += 4 # 1 point for playing + 3 points for winning
                    rounds += 1
                elif cpu_roll > user_roll: 
                    print("CPU wins this round!")
                    cpu_score += 1 # 1 point for cpu
                elif user_roll == cpu_roll:
                    print("It's a tie!")
                    user_score += 1  # 1 point for playing
                elif rounds == 0:
                    print("Game Over you didnt win any game.")
                else:
                    print("game over")
                

            print(f"\n{self.player}")
            print(f"points : {user_score}, wins : {rounds}")
            self.update_scores(user_score // 4) # win count is user_score // 4                   
            while True:
                choice = input("\nDo you want to continue to the next stage? 1 for Yes , 0 for No: ")
                try:
                    choice = int(choice)
                    if choice == 1:
                        break
                    elif choice == 0:
                        print("Game Over!!")
                        return
                except ValueError as e:
                    print(f"Error: {e}")

    def load_scores(self):
        if os.path.exists("scores.txt"): # Check if the scores file exists
            with open("scores.txt", "r") as file: # Open the scores file in read mode 
                for line in file:  # Iterate over each line in the file
                    username, points, wins = line.strip().split(",")  # Split the line into username, points, and wins
                    self.scores[username] = Score(username, int(points), int(wins))  # Create a new Score object and add it to the scores dictionary in intiger
    
    def save_scores(self):
        with open("scores.txt", "w") as file: # Open the scores file in write mode, creating it if it doesn't exist
            for score in self.scores.values(): # Iterate over each score in the scores dictionary
                file.write(f"{score.username},{score.points},{score.wins}\n") # Write the score's information to the file

    def update_scores(self, win):
        if self.player in self.scores: # Check if the player exists in the scores dictionary
            self.scores[self.player].points += win * 4 # To Update the player's points and wins
            self.scores[self.player].wins += win
        else:
            self.scores[self.player] = Score(self.player, win * 4, win)  # If the player doesn't exist, create a new Score object for the player
        self.save_scores() # Save the updated scores to the scores file

    def display_top_scores(self):
        if not self.scores: # Check if the scores dictionary is empty
            print("No game played yet. Play game to see top scores.")
            return
        
        sorted_scores = sorted(self.scores.values(), key = self.sort_key, reverse = True) # Sort the scores dictionary values based on the specified sort key and in descending order
        print("\nTop Scores:") #Show the top score
        for rank, score in enumerate(sorted_scores[:10], start = 1): 
            print(f"{rank}. {score.username}, points: {score.points}, wins: {score.wins}\n")

    def sort_key(self, score): #this one is just for sorting the score and wins, wherein the points is the primarily an wins as secondary as returning value
        return (score.points, score.wins)
    
    
    