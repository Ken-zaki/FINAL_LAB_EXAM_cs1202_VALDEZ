import os
from user import User

class UserManager:
    def __init__(self):
        self.users = {} # Initialize an empty dictionary to store user information
        self.load_users() # Load users when initializing the UserManager instance

    def load_users(self):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file: #open the users.txt "r" (readmode), for this system to load the text within the txt file
                for line in file:
                    username, password = line.strip().split(",") # to ensure remove leading whitespace and split username and password using .split coma
                    self.users[username] = User(username, password) #to access the part of dictionary and username as a key, and User being assigned as an instance object and created calling by class constructor with username, password argument
    
    def save_users(self):
        with open("users.txt", "w") as file: #open the users. txt "w" (writemode), for this system to write a new text in the txt file 
            for user in self.users.values():  # Iterate over each user in the users dictionary
                file.write(f"{user.username},{user.password}\n") # Write the username and password of each user to the file

    def login(self, username, password):
        return username in self.users and self.users[username].password == password  # Check if the username exists in the users dictionary and if the password matches

    def register(self, username, password):
        if username not in self.users: # Check if the username is not already in use
            self.users[username] = User(username, password) # If the username is available, create a new user and add it to the users dictionary
            self.save_users() # Save the updated user information to the users.txt file
            return True # Return True to indicate successful registration
        return False  # If the username is already in use, return False to indicate registration failure