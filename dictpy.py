# @sumitvarun
# Import Required Library
from tkinter import *
from PyDictionary import PyDictionary

# Create Objects
dictionary = PyDictionary()
root = Tk()

# Set geometry
root.geometry("400x400")

# Set Background Color
root.configure(background='grey')




def dict():
	meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
	synonym.config(text=dictionary.synonym(word.get()))
	antonym.config(text=dictionary.antonym(word.get()))


# Add Labels, Button and Frames
Label(root, text="Dictionary", font=(
	"Helvetica 20 bold"), fg="#900431", bg= "#DE3163").pack(pady=10)

# Add Labels, Button and Frames
Label(root, text="SUMITVARUN", font=(
	"Helvetica 10"), fg="#784212", bg= "#D68910").pack(pady=10)

# Frame 1
frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold"), bg= "#3498DB", fg="#043247").pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"),)
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold"),fg="white", bg= "#5B2C6F").pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

# Frame 3
frame2 = Frame(root)
Label(frame2, text="Synonym:- ", font=("Helvetica 10 bold"),fg="white", bg= "#5B2C6F").pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

# Frame 4
frame3 = Frame(root)
Label(frame3, text="Antonym:- ", font=("Helvetica 10 bold"),fg="white", bg= "#5B2C6F").pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict,fg="white", bg= "#1E8449").pack()

# Execute Tkinter
root.mainloop()
