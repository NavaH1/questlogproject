import tkinter

butt1 = False
whatever = input()

def myButton():
    label_1.configure(text = whatever)
    global butt1
    butt1 = True

Nava = tkinter.Tk()
Nava.geometry('450x200')
Nava.title("Learn my name")

label_1 = tkinter.Label(Nava, text="To know my name")
label_1.pack()

button_1 = tkinter.Button(Nava, text="press here", command=myButton)
button_1.pack()

Nava.mainloop()
