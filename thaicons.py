Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... from random import shuffle
... 
... # Thai consonants and their pronunciation
... thai_consonants = [
...     ("ก", "gor kai"), ("ข", "khor khai"), ("ฃ", "khor khuad"),
...     ("ค", "khor khwai"), ("ฅ", "khor khon"), ("ฆ", "khor ra-khang"),
...     ("ง", "ngor ngu"), ("จ", "jor jan"), ("ฉ", "chor ching"),
...     ("ช", "chor chang"), ("ซ", "sor so"), ("ฌ", "chor cher"),
... ]
... shuffle(thai_consonants)  # Shuffle flashcards
... 
... class FlashcardApp:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("Thai Consonant Flashcards")
...         self.current_index = 0
...         self.flipped = False
...         
...         self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, bd=3)
...         self.card_frame.pack(pady=20)
...         
...         self.label = tk.Label(self.card_frame, text="", font=("Arial", 40), bg="white")
...         self.label.pack(expand=True)
...         
...         self.card_frame.bind("<Button-1>", self.flip_card)
...         self.label.bind("<Button-1>", self.flip_card)
...         
...         self.next_button = tk.Button(root, text="Next", command=self.next_card)
...         self.next_button.pack()
...         
...         self.show_card()
...     
...     def show_card(self):
...         self.label.config(text=thai_consonants[self.current_index][0])
...         self.flipped = False
...     
...     def flip_card(self, event):
...         if not self.flipped:
...             self.label.config(text=thai_consonants[self.current_index][1])
...             self.flipped = True
...         else:
...             self.label.config(text=thai_consonants[self.current_index][0])
...             self.flipped = False
...     
...     def next_card(self):
...         self.current_index = (self.current_index + 1) % len(thai_consonants)
...         self.show_card()
... 
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = FlashcardApp(root)
...     root.mainloop()
