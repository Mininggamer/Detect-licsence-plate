# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image
from os import listdir
from remake import DetectBS
DetectBS()

def forward(img_no):
    global smt
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(root,image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_for = Button(root, text="forward",
                        command=lambda: forward(img_no + 1))

    if img_no == 25:
        button_forward = Button(root, text="Forward",
                                state=DISABLED)


    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))
    button_exit = Button(root, text="Detect",
                         command=lambda: DetectLP(img_no-1))

    button_back.grid(row=7, column=0)
    button_exit.grid(row=7, column=1)
    button_for.grid(row=7, column=2)


def back(img_no):
    global smt
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(root,image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                            command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))
    print(img_no)
    button_exit = Button(root, text="Detect",
                         command=lambda: DetectLP(img_no-1))

    if img_no == 1:
        button_back = Button(root, Text="Back", state=DISABLED)


    label.grid(row=1, column=0, columnspan=3)


    button_back.grid(row=7, column=0)
    button_exit.grid(row=7, column=1)
    button_forward.grid(row=7, column=2)
    smt = img_no

def DetectLP(img_no):
    #window = Toplevel(root)
    #window.title("License plates")
    LicsenPlate_pil = ImageTk.PhotoImage(Image.open("Save/" + List_name[img_no][22:]))
    label_licsen = Label(image=LicsenPlate_pil).grid(row=1, column=4)
    label_licsen.grid(row=1, column=4)
root = Tk()
root.title("Detect license plates")

smt = 0
List_images = []
List_name = []
for filename in listdir("image"):
    img = ImageTk.PhotoImage(Image.open("image/" + filename))
    List_images.append(img)
    List_name.append(filename)
label = Label(root,image=List_images[0])

label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text="Back", command=back,
                     state=DISABLED)

button_exit = Button(root, text="Exit",
                     command=lambda: DetectLP(0))

button_forward = Button(root, text="Forward",
                        command=lambda: forward(1))

button_back.grid(row=7, column=0)
button_exit.grid(row=7, column=1)
button_forward.grid(row=7, column=2)

root.mainloop()