# mood.py
#  Project: Mood of the Day
# Author: Hamdah Omotosho

from termcolor import colored

def show_mood_message(mood):
    """
    Prints a colored message based on the user's mood.
    Parameters:
        mood (str): The mood entered by the user.
    """
    mood = mood.lower()

    if mood == "happy":
        print(colored("Keep smiling! Today is bright and beautiful 🌞", "magenta"))
    elif mood == "sad":
        print(colored("It's okay to rest and feel. Better days are ahead 💙", "blue"))
    elif mood == "angry":
        print(colored("Take a deep breath. You’re stronger than this ❤️", "red"))
    elif mood == "tired":
        print(colored("Rest is productive too 😴", "cyan"))
    else:
        print(colored("Mood not recognized, but stay positive anyway 💚", "green"))

# ---- main program ----
if __name__ == "__main__":
    user_mood = input("How are you feeling today? (happy/sad/angry/tired): ")
    show_mood_message(user_mood)
