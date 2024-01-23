import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x400")  
        self.master.configure(bg="black")

        self.categories = ["Color", "Language", "Animal"]
        self.category = random.choice(self.categories)

        self.word_bank = {
            "Color": ["Red", "Blue", "Yellow", "Green", "Pink", "Black", "White", "Grey", "Purple"],
            "Language": ["French", "Spanish", "Polish", "English", "Hindi", "German", "Russian"],
            "Animal": ["Tiger", "Lion", "Dog", "Cat", "Zebra", "Elephant"]
        }

        self.word = random.choice(self.word_bank[self.category])
        self.word_progress = ["-" for _ in self.word]
        self.guessed = []
        self.incorrect = 0

        self.draw_man_canvas = tk.Canvas(self.master, width=200, height=200, bg="black")  # Set canvas size
        self.draw_man_canvas.pack()

        self.category_label = tk.Label(self.master, text=f"Category: {self.category}", font=("Helvetica", 14), bg="black", fg="white")
        self.category_label.pack()

        self.word_label = tk.Label(self.master, text=self.display_word(), font=("Helvetica", 16, "bold"), fg="white", bg="black")
        self.word_label.pack()

        self.guess_label = tk.Label(self.master, text="Guessed letters: ", font=("Helvetica", 12, "italic"), fg="white", bg="black")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master, bg="white", fg="black")  # Set entry background and foreground color
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, bg="white", fg="black",
                                      font=("Helvetica", 12, "bold"))
        self.guess_button.pack()

    def display_word(self):
        return " ".join(self.word_progress)

    def draw_man(self):
        parts = ["O", "/|\\", "/ \\", "Yikes :("]
        for i in range(self.incorrect):
            self.draw_man_canvas.create_text(100, 20 * i + 10, text=parts[i], font=("Helvetica", 22), fill="white")

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if guess == self.word.lower():
            messagebox.showinfo("Congratulations!", "You guessed the right word! You win!")
            self.master.destroy()
            return  # Exit the function to prevent further execution

        if len(guess) > 1 or guess in self.guessed:
            messagebox.showwarning("Invalid Guess", "Sorry, that's not a valid guess.")
            self.incorrect += 1
        elif guess not in self.word.lower():
            messagebox.showinfo("Incorrect Guess", f"{guess} is not in the word.")
            self.incorrect += 1
            self.guessed.append(guess)
        else:
            messagebox.showinfo("Correct Guess", f"{guess} is in the word!")
            self.guessed.append(guess)
            self.word_progress = [letter if self.word[i].lower() == guess else self.word_progress[i]
                                  for i, letter in enumerate(self.word)]

        self.guess_label.config(text="Guessed letters: " + " ".join(self.guessed))
        self.word_label.config(text=self.display_word())
        self.draw_man()

        if "-" not in self.word_progress:  # Check if all letters are guessed
            messagebox.showinfo("Congratulations!", "You guessed the right word! You win!")
            self.master.destroy()

        if self.incorrect == 4:  # Adjusted the incorrect count for testing purposes
            messagebox.showinfo("Game Over", f"You lost!\nThe word was: {self.word}")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()
