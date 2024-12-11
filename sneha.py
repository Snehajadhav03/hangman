#Sneha Jadhav
# Import necessary libraries for the game
import random  # Used for choosing a random word from a list
import tkinter as tk  # Used for creating the graphical user interface (GUI)
from tkinter import messagebox  # Used for displaying popup messages

# Function to randomly select a word and its hint
def choose_word():
    # List of word and hint pairs
    word_list = [
        ("python", "A popular programming language."),  # Word and its hint
        ("hangman", "A classic word-guessing game."),
        ("programming", "The process of writing computer code."),
        ("openai", "The AI company behind ChatGPT."),
        ("challenge", "Something that tests your abilities.")
    ]
    # Randomly choose a word and its hint from the list and return them as a tuple
    return random.choice(word_list)

# Function to display the word with guessed letters revealed
def display_word(word, guessed_letters):
    # Return a string where each letter is shown if guessed, otherwise an underscore
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to handle the player's guess
def make_guess():
    global attempts_remaining, guessed_letters  # Access global variables

    # Get the guess from the input box and convert to lowercase
    guess = guess_entry.get().lower()
    # Clear the input box after getting the guess
    guess_entry.delete(0, tk.END)

    # Validate input (only a single alphabetic character is allowed)
    if len(guess) != 1 or not guess.isalpha():
        # Show an error message if input is invalid
        messagebox.showerror("Invalid Input", "Please enter a single letter.")
        return  # Exit the function

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        # Show a message if the letter was guessed previously
        messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'. Try another letter.")
        return  # Exit the function

    # Add the new guess to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guess is correct
    if guess in word_to_guess:
        # Show a message if the guess is correct
        messagebox.showinfo("Correct Guess", f"Good job! '{guess}' is in the word.")
        # Check if the entire word has been guessed
        if all(letter in guessed_letters for letter in word_to_guess):
            # Show a congratulatory message if the word is guessed
            messagebox.showinfo("Congratulations", f"You guessed the word: {word_to_guess}")
            root.destroy()  # Close the game window
    else:
        # Show a message if the guess is incorrect
        messagebox.showinfo("Incorrect Guess", f"Sorry, '{guess}' is not in the word.")
        # Decrease the number of attempts remaining by 1
        global attempts_remaining
        attempts_remaining -= 1
        # Check if attempts have run out
        if attempts_remaining == 0:
            # Show a game over message if no attempts remain
            messagebox.showinfo("Game Over", f"You ran out of attempts! The word was: {word_to_guess}")
            root.destroy()  # Close the game window

    # Update the display with the new state of the game after the guess
    update_display()

# Function to update the display labels dynamically
def update_display():
    # Update the word label with the current state of guessed letters
    word_label.config(text=display_word(word_to_guess, guessed_letters))
    # Update the attempts remaining label
    attempts_label.config(text=f"Attempts Remaining: {attempts_remaining}")
    # Update the guessed letters label with the current guesses
    guessed_label.config(text=f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

# Initialize the game variables
word_to_guess, hint = choose_word()  # Select a random word and hint
guessed_letters = set()  # Set to store letters that have been guessed
attempts_remaining = 6  # Initial number of attempts

# Create the main window for the game
root = tk.Tk()  # Create a new Tkinter window
root.title("Hangman Game")  # Set the title of the window
root.geometry("500x600")  # Set the dimensions of the window

# Label to display the hint for the word
hint_label = tk.Label(root, text=f"Hint: {hint}", font=("Helvetica", 16), fg="blue")  # Create a label for the hint
hint_label.pack(pady=15)  # Pack the label with some vertical padding

# Label to display the word with underscores for unguessed letters
word_label = tk.Label(root, text=display_word(word_to_guess, guessed_letters), font=("Helvetica", 24))  
# Create a label for the word
word_label.pack(pady=15)  # Pack the label with some vertical padding

# Label to display the number of attempts remaining
attempts_label = tk.Label(root, text=f"Attempts Remaining: {attempts_remaining}", font=("Helvetica", 18))  
# Create a label for attempts
attempts_label.pack(pady=10)  # Pack the label with some vertical padding

# Label to display the guessed letters so far
guessed_label = tk.Label(root, text="Guessed Letters: None", font=("Helvetica", 18))  # Create a label for guessed letters
guessed_label.pack(pady=10)  # Pack the label with some vertical padding

# Entry box for the player to input their guess
guess_entry = tk.Entry(root, font=("Helvetica", 18), justify="center", width=5)  # Create an entry widget
guess_entry.pack(pady=15)  # Pack the entry with some vertical padding

# Button to submit the player's guess
guess_button = tk.Button(root, text="Submit Guess", command=make_guess, font=("Helvetica", 18), bg="lightgreen") 
 # Create a button to submit guess
guess_button.pack(pady=15)  # Pack the button with some vertical padding

# Start the main event loop to run the game
root.mainloop()  # Run the Tkinter event loop
