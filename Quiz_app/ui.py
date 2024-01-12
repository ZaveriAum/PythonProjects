from tkinter import *

THEME_COLOR = "#345362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Genji's Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(text=f"Score: 0")
        self.score_board.config(bg=THEME_COLOR, fg="white")
        self.score_board.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0)
        self.correct.grid(row=2, column=0, padx=20, pady=20)

        incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect = Button(image=incorrect_image, highlightthickness=0)
        self.incorrect.grid(row=2, column=1, padx=20, pady=20)

        self.canvas.create_text(150, 90, text="Some question", width=300, font=("Arial", 20, "italic"))

        self.window.mainloop()
