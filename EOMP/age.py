# Alex Sassman, class 1
from datetime import *
from tkinter import *
from tkinter import messagebox



window=Tk()
window.title("Lottery")
window.geometry("450x150")
window.configure(background="yellow")

#date and time
date = datetime.now()
dlb = Label(window)
dlb.grid(row=0, column=0)
dlb.config(background="yellow", text="Date and Time: " + date.strftime("%d/%m/%y %H:%M"))

lb=Label(window,text="Ithuba National Lottery of South Africa", background="yellow")
lb.grid(row=1, column=2)

#age entry
Label(window, text="please enter your age:", background="lime").grid(row=12, column=0)
age_entry = Entry(window, textvariable="age")
age_entry.grid(row=12, column=2)


#name entry
Label(window, text="Name and Surname:", background="lime").grid(row=2, column=0)
name_= Entry(window, textvariable="name")
name_.grid(row=2, column=2)

#verify age
def verify():
    age = int(age_entry.get())
    name =name_.get()

    #error handling
    try:
        #closes if you are under 18
        if age < 18:
            (messagebox.showinfo("ERROR", "Must be 18 years or older to play!"))
            file = open("lottery.txt", "a+")
            file.write("Name: " + name + "\n")
            file.write("Age: " + str(age) + "\n")
            file.close()
            window.withdraw()

        #you are allowed to play if you are of age
        else:
            messagebox.showinfo("message","You are of age to play, good luck!")
            age_entry.delete(0, END)
            file=open("lottery.txt","a+")
            file.write("Name: "+ name + "\n")
            file.write("Age: "+ str(age) + "\n")
            file.close()
            window.withdraw()
            import lottery
            lottery.lottery()

    except ValueError as v:
        print(v)
        age_entry.delete(0, END)


Button(window, text="Verify", width=10, height=2, command=verify).grid(row=15, column=2)


window.mainloop()