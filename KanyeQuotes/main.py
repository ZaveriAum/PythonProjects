from tkinter import *
import requests


# Function
def get_quoted():
    # Getting data from API
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()['quote']
    print(quote.split())
    canvas.itemconfig(quote_text, text="")
    canvas.itemconfig(quote_text, text=f"{quote}")


# Interface
window = Tk()
window.config(padx=30, pady=30)

canvas = Canvas(width=250, height=600)

quote_box = PhotoImage(file="background.png")
canvas.create_image(125, 200, image=quote_box)

canvas.grid(row=0, column=0)

kanye_memoji = PhotoImage(file="kanye.png")
kanye = Button(image=kanye_memoji, highlightthickness=0, command=get_quoted)
kanye.grid(row=1, column=0)

quote_text = canvas.create_text(100, 200, text="", font=("Ariel", 20, "normal"), width=200)

window.mainloop()
