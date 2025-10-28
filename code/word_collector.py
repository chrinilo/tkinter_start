"""
Simple Tkinter app to collect 10 words from user input and display them.

The user types a word in the entry box, clicks the button, and the word is
added to a list. After 10 words are collected, they are displayed in a label.
"""

import tkinter as tk


class WordCollectorApp(tk.Tk):
    """Main application window that collects 10 words from user input."""

    def __init__(self):
        super().__init__()
        self.title("Word Collector")
        self.geometry("400x300")
        self.resizable(False, False)

        # Internal state: list of words and max count
        self.words = []
        self.max_words = 10

        # Create widgets
        self._create_widgets()

    def _create_widgets(self):
        """Build the UI: instruction label, entry, button, result label."""
        # Instruction label at top
        instruction_text = f"Enter words below and click Add (0/{self.max_words})"
        self.instruction_label = tk.Label(
            self, text=instruction_text, font=("Arial", 11)
        )
        self.instruction_label.pack(pady=(20, 10))

        # Entry widget for text input
        self.entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.entry.pack(pady=10)
        self.entry.focus()  # start with cursor in entry
        # Bind Enter key to add_word
        self.entry.bind("<Return>", lambda event: self.add_word())

        # Button to add word to list
        self.add_button = tk.Button(
            self,
            text="Add Word",
            command=self.add_word,
            font=("Arial", 11),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5,
        )
        self.add_button.pack(pady=10)

        # Label to display the final list of words (hidden until done)
        self.result_label = tk.Label(
            self, text="", font=("Arial", 10), wraplength=350, justify="left", fg="blue"
        )
        self.result_label.pack(pady=20)

    def add_word(self):
        """Add the text from the entry to the word list and update UI."""
        word = self.entry.get().strip()

        # Ignore empty input
        if not word:
            return

        # Add the word to the list
        self.words.append(word)

        # Clear the entry for the next word
        self.entry.delete(0, tk.END)

        # Update the instruction label with progress
        count = len(self.words)
        self.instruction_label.config(
            text=f"Enter words below and click Add ({count}/{self.max_words})"
        )

        # If we have 10 words, display them and disable further input
        if count >= self.max_words:
            self._display_words()

    def _display_words(self):
        """Show all collected words in the result label and disable input."""
        # Disable entry and button
        self.entry.config(state="disabled")
        self.add_button.config(state="disabled", bg="gray")

        # Build the display text
        words_text = "Your 10 words:\n" + ", ".join(self.words)
        self.result_label.config(text=words_text)

        # Update instruction label
        self.instruction_label.config(text=f"Done! You entered {self.max_words} words.")


if __name__ == "__main__":
    app = WordCollectorApp()
    app.mainloop()
