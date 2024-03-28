from random import randint
from tkinter import Tk, Label
from PIL import Image, ImageTk
from pygame import mixer

mixer.init()
son_roue = mixer.Sound("./resources/roue-fortune.mp3")
son_chevre = mixer.Sound("./resources/chevre.wav")

doublon = [0]

try:
    save = open("save.txt")
except FileNotFoundError:
    save = open("save.txt", "w")
    save.close()
    save = open("save.txt")

for line in save:
    try:
        doublon = eval(line.split("\t")[0])
    except:
        pass
save.close()

if type(doublon) is not list:
    doublon = [0]

while len(doublon) > 10:
    doublon.pop(0)

root = Tk()
root.title("Les voix de la Recherche - La question mystère")
root.geometry("900x600")
root.attributes("-fullscreen", True)
root.config(bg="white")
root.call('tk', 'scaling', 2)

image = Image.open("./resources/logo_sadapt.png")
img = ImageTk.PhotoImage(image)

_ = Label(root, text="", bg="white", font=("Avenir", 50))
_.pack()
title = Label(root, text="Les voix de la Recherche", fg="black", bg="white", font=("Avenir", 35))
title.pack()
_ = Label(root, text="", bg="white", font=("Avenir", 0))
_.pack()
question = Label(root, text="La question mystère numéro ?", fg="black", bg="white", font=("Avenir", 25))
question.pack()
label = Label(root, text=str(doublon[-1]))
label.config(fg="black", bg="white", font=("Avenir", 130))
label.pack(fill="both", expand=True)
label_image = Label(root, image=img)
label_image.config(bg="white")
label_image.pack()
_ = Label(root, text="", bg="white", font=("Avenir", 100))
_.pack()

def alea_i(event):
    global idx, idy, a, x, y
    label_image.unbind('<Button-1>')
    root.unbind('<space>')
    son_roue.play()
    idx = 0
    idy = 0
    a = randint(1, 50)
    while a in doublon:
        a = randint(1, 50)
    if len(doublon) < 10:
        doublon.append(a)
    else:
        doublon.pop(0)
        doublon.append(a)
    if a < 25:
        x, y = 351, 300
    else:
        x, y = 301, 250
    alea()

def alea():
    global idx, idy, a, x, y
    idx += 1
    idy += 1
    if idx > 50:
        idx = 1
    if idy < x and idy > y:
        if idx == a:
            son_roue.stop()
            son_chevre.play()
            label.config(text=str(idx))
            save = open("save.txt", "w")
            save.write(str(doublon))
            save.close()
            label_image.bind('<Button-1>', alea_i)
            root.bind('<space>', alea_i)
        else:
            label.config(text=str(idx))
            label.after(10, alea)
    else:
        label.config(text=str(idx))
        label.after(10, alea)

label_image.bind('<Button-1>', alea_i)
root.bind('<space>', alea_i)
root. bind('<Escape>',lambda e: root. destroy())

root.mainloop()
