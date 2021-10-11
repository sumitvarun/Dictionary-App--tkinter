# @sumitvarun
# Import Required Library
from tkinter import *
import tkinter
from PyDictionary import PyDictionary
import webbrowser

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


#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# Add Labels, Button and Frames
Label(root, text="Dictionary", font=(
	"Helvetica 20 bold"), fg="#900431", bg= "#DE3163").pack(pady=10)


#Create a Label to display the link
link = Label(root, text="SUMITVARUN",font=('Helveticabold', 10), cursor="hand2",fg="#784212", bg= "#D68910")
link.pack()
link.bind("<Button-1>", lambda e:
callback("https://github.com/sumitvarun"))

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

Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict,fg="#DCE775", bg= "#1E8449").pack()
frame3.pack(pady=10)

#Create a Label to display the link
#link = Label(root, text="GitHub",font=('Helveticabold', 15), cursor="hand2",fg="#000000", bg= "#BDBDBD")
#link.pack()
#link.bind("<Button-1>", lambda e:
#callback("https://github.com/sumitvarun"))




# Execute Tkinter
root.mainloop()
