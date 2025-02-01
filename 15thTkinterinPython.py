
# ! Tkinter

from tkinter import *

from tkinter import messagebox

# * Tkinter is one of the GUI libraries in Python

# * As we have imported tkinter to variable t (Refer Line 6), let's not mess around by creating any new variable named t

# * If we use 'import tkinter as t' then above comment is in matter

# * But here we are just importing everything from tkinter to access all the widgets

# * So, no need to write root = t.Tk()

def click():

    # * For messagebox, we again have to import it separately cause it's Python :)

    messagebox.showinfo('Message', 'Button clicked') # * New window which will print the message i.e. Button clicked

def submittion():

    messagebox.askquestion('Form', 'Do you want to end this life?')

root = Tk() # * This is what creates the window

root.title('New BOI') # * The Name of the window

root.geometry('500x500') # * The Dimensions of the window (breath x length)

root.config(bg = 'white')

# ! Button in Tkinter

# * This creates the button widget

button = Button(root, text = 'Submit', command=click, pady=5, activebackground='orange',bg='white') 

# * command takes in func. name which will be called when the button is clicked

# * pady creates some space b/w text inside the button and the button

# * activebg changes the colour of the button in the duration it is clicked

# * bg is the const. colour of button

# ! Canvas in Tkinter

# * This creates the canvas window

# * Canvas is just the Drawing area in the window

canvas = Canvas(root, bg = 'white', height=300, width=300)

# * We are creating the circle in the window

coord = (10, 10, 300, 300)

arc1 = canvas.create_arc(coord, start=0,extent=150, fill='red')

arc2 = canvas.create_arc(coord, start=150,extent=215, fill='green')

# * We are adding an image to the window

canvas1 = Canvas(root, height=700,width=800)

filename = PhotoImage(file=r'C:\Users\Admin\Pictures\ip.png')

image = canvas1.create_image(20, 20, anchor=NW, image= filename)

# ! Checkbutton in Tkinter

# * User can enter more than one option

checkbutton = Checkbutton(root, command=click)

labellllll = Label(root, text = 'Select your hobbies')

checkbutton1 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

checkbutton2 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

checkbutton3 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

# * IntVar is used to store, retrieve and manage integer variables in Python 

cb1 = Checkbutton(root, text='Painting', variable = checkbutton1, onvalue = 1, offvalue=0)

cb2 = Checkbutton(root, text='Reading', variable = checkbutton2, onvalue = 1, offvalue=0)

cb3 = Checkbutton(root, text='Horse Riding', variable = checkbutton3, onvalue = 1, offvalue=0)

# ! Label in Tkinter

# * Label is used to print any text on the tkinter window

username = Label(root, text = 'Username')

password = Label(root, text = 'Password')

submitbutton = Button(root, text = 'Submit', command=submittion)

e1 = Entry(root, width = 20)

e2 = Entry(root, width = 20)

# ! Frame in Tkinter

# * Frame is used to make a region inside the window itself

# * And that becomes another window by itself

# * A window inside a window

# * And that helps us arrange stuff in a more better manner

# * And we can put as many widgets as we want in the frame

frame = Frame(root)

frame.pack(side=BOTTOM)

bb = Button(frame, text='Yes')

# ! Nested Frames

# * As the name suggests, It's a frame inside a frame

frame1 = Frame(root, bg='black',width=500,height=300)

frame2 = Frame(root, bg='Grey',width=100,height=100)

# ! Packing

button.pack(side=BOTTOM) # * This places the button on the window

# canvas.pack()

# canvas1.pack()

checkbutton.pack(side=BOTTOM)

labellllll.pack()

cb1.pack()

cb2.pack()

cb3.pack()

username.place(x = 30, y = 50)

password.place(x = 30, y= 90)

submitbutton.place(x = 30, y = 120)

e1.place(x = 100, y = 50)

e2.place(x = 100, y = 90)

bb.pack() # * This will be placed at the bottom of the window as the frame it is related to is packed at the bottom

frame1.pack()

frame2.pack(pady=20,padx=20)

# * pack(side=TOP) puts the widget on top of the window (default)

# * pack(side=BOTTOM) puts the widget on the bottom of the window 

root.mainloop() # * This keeps the window alive until we close it (this is always at end of the code)