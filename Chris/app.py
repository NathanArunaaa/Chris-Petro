from tkinter import *

root = Tk()
#sets title of window to wtv u want
root.title("Chris's Calculator")
#Set window size (I made it same size as league client)
root.geometry("1024x576")
#setting background colour
root.configure(bg="#000000")

#creating area for answer to go into
answers = Label(root, width = 50, height=2,text="",font=("Gilmer_Heavy",30))
answers.pack()

Button(root, text = "C", width = 5, height = 1, font = ("arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#3697f5").place() 

root.mainloop()