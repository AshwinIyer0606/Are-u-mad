from tkinter import *
import random
window = Tk()
window.title("Are u mad")
window.config(padx=30, pady=50)

opt = random.randint(0, 16)

def Yes():
	Question.config(text="I knew it :)")
	
	
Question = Label(text="Are u\nmad?", font="Helvetica, 20")
Yes = Button(text="Yes", command=Yes)
No = Button(text="No")

Question.grid(row=1, column=2)
Yes.grid(row=2, column=1)
No.grid(row=2, column=3)


window.mainloop()
