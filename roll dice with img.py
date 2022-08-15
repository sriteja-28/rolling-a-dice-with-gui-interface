import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
#root.geometry('200x200')
root.title('Roll Dice')

# image
# make sure image is in path or specify specific path
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for each image
label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)
# keep a reference, if needed
label1.image = image1
label2.image = image2
# pack a widget in the parent widget with placement
label1.pack(side=tkinter.LEFT )
label2.pack(side=tkinter.RIGHT)

# function activated by button
def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label2.configure(image=image2)
    # keep a reference
    label2.image = image2

# button
# command will use roll_dice function
button = tkinter.Button(root, text='ROLL DICE', foreground='blue', command=roll_dice)

# pack a widget in the parent widget
button.pack()

# call the mainloop of Tk
# keeps window open
root.mainloop()
