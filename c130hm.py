from tkinter import *

root = Tk()
root.title('ATM')
root.geometry('500x600')
top_frame = Frame(root, bg="#ffffff")
top_frame.grid(row=0, column=0, columnspan=3, pady=10)

lbl1 = Label(top_frame, text="Account Name", bg="#5daad1")
lbl2 = Label(top_frame, text="Enter PIN", bg="#5daad1")

acount = Entry(top_frame)
pin = Entry(top_frame, show='*')

lbl1.grid(row=0, column=0, padx=5, pady=5)
acount.grid(row=0, column=1, padx=5, pady=5)

lbl2.grid(row=1, column=0, padx=5, pady=5)
pin.grid(row=1, column=1, padx=5, pady=5)
textbox = Text(root, bg="#6E6C6C", fg="black", height=8, width=40)
textbox.grid(row=1, column=0, columnspan=3, pady=10)
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
    for j in range(3):
        cell = Frame(root, relief=SUNKEN, borderwidth=1, bg="#ffffff")
        cell.grid(row=i+2, column=j, sticky="nsew", padx=2, pady=2)

        label = Label(cell, text=nums[i][j], bg="#ffffff", font=('Arial', 18))
        label.pack(padx=5, pady=5)
def display():
    name = acount.get()
    greet = "Hey " + name
    message = "\nCongratulations on your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
btn = Button(root, text="Create Account", command=display, bg="lime")
btn.grid(row=6, column=1, pady=15)

root.mainloop()
