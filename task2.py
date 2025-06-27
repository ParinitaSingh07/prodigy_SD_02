import tkinter
from tkinter import Tk
import pygame

pygame.mixer.init()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

import random
number_toguess = random.randint(1, 100)
attempts = 0
def guess_thenumber():
    global attempts
    try:
        guess =int(userinput_textbook.get())
        attempts +=1
 # Compare the guess to the number
        if guess < number_toguess:
            label_result.config(text="Too low! Try again.")
            play_sound("wrong.mp3")
        elif guess > number_toguess:
            label_result.config(text="Too high! Try again.")
            play_sound("wrong.mp3")
        else:
            label_result.config(text=f"Congratulations! You guessed the number {number_toguess} correctly in {attempts} attempts.")
            play_sound("correct.mp3")
            sumbit_button.config(state="disabled")
        
    except ValueError:
            label_result.config(text="Please enter a valid number.")

# Run the game
# guess_thenumber()
#guisetup
root=tkinter.Tk()
root.geometry("600x600")
root.title("guess the number game")
root.configure(bg="#E3A1A1")

game_label=tkinter.Label(root, text="welcome to the game of guessing the number",font=("georgia",22)).pack(pady=10)
userinput_label=tkinter.Label(root, text="Enter the number between 1 to 100 you want to guess",font=("georgia",20)).pack()
userinput_textbook=tkinter.Entry(root, font=('Georgia', 16), width=30)
userinput_textbook.pack(pady=15)

sumbit_button=tkinter.Button(root, text="Sumbit Your Guess", font=("georgia",18) , command=guess_thenumber)
sumbit_button.pack(pady=15)
label_result = tkinter.Label(root, text="", font=("Arial", 18))
label_result.pack()


# sumbit_button.pack()

root.mainloop()

