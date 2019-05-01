from tkinter import *
master = Tk()

def var_states():
   print("Human: %d,\nAlien: %d,\nSpider: %d,\nDeamon: %d" % (var1.get(), var2.get(), var3.get(), var4.get()))


master.geometry('450x200')
Label(master, text="Your species:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Human", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Alien", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Spider", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Deamon", variable=var4).grid(row=4, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=6, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=7, sticky=W, pady=4)

mainloop()
