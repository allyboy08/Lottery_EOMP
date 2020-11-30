from tkinter import messagebox
from tkinter import *
import random
from datetime import *

window = Tk()
window.title("Lottery")
window.geometry("500x150")
window.configure(background="skyblue")

# generates random numbers
gen_num = []
lottery = random.sample(range(1, 50), 6)
print(list(sorted(lottery)))

# date
date = datetime.now()
dlb = Label(window)
dlb.place(x=300, y=1)
dlb.config(background="skyblue", text="Date and Time: " + date.strftime("%d/%m/%y %H:%M"))

#entires and labels
lb=Label(window,text="Ithuba National Lottery of South Africa",background="skyblue")
lab = Label(window, text="Enter lotto numbers:", background="skyblue")
res = Label(window, background="skyblue")
num1 = Entry(window, width=6, background="blue")
num2 = Entry(window, width=6, background="yellow")
num3 = Entry(window, width=6, background="white")
num4 = Entry(window, width=6, background="green")
num5 = Entry(window, width=6, background="pink")
num6 = Entry(window, width=6, background="orange")

#positions of the labels and entries
lb.place(x=1, y=1)
lab.place(x=1, y=30)
res.place(x=1, y=100)
num1.place(x=1, y=50)
num2.place(x=45, y=50)
num3.place(x=90, y=50)
num4.place(x=135, y=50)
num5.place(x=180, y=50)
num6.place(x=225, y=50)

#comparing the winning numbers and displaying the result function
def winnings():
    gen_num.append(int(num1.get()))
    gen_num.append(int(num2.get()))
    gen_num.append(int(num3.get()))
    gen_num.append(int(num4.get()))
    gen_num.append(int(num5.get()))
    gen_num.append(int(num6.get()))

    right = 0
    for a in gen_num:
        if a in lottery:
            right +=1
    #right = set(gen_num).intersection(lottery)
    try:
        #result if you get all of the winning numbers rightbackground="yellow",
        if right == 6:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: R10 000 000.00")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt','a+')
            file.write(res.cget("text")+ "\n" + "You won: R10 000 000.00" + "\n")
            file.close()

        # result if you get none of the winning numbers right
        elif right == 0:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: Nothing")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: Nothing" + "\n")
            file.close()

        # result if you get 1 of the winning numbers right
        elif right == 1:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: Nothing")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: Nothing" + "\n")
            file.close()

        # result if you get 2 of the winning numbers right
        elif right == 2:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: R20.00")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: R20.00" + "\n")
            file.close()

        # result if you get 3 of the winning numbers right
        elif right == 3:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: R100.00")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: R100.00" + "\n")
            file.close()

        # result if you get 4 of the winning numbers right
        elif right == 4:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: R2,384.00")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: R2,384.00" + "\n")
            file.close()

        # result if you get 5 of the winning numbers right
        elif right == 5:
            res.config(text="Results:" + str(lottery))
            messagebox.showinfo("Message", "You won: R8,584.00")
            file = open('/home/user/PycharmProjects/EOMP/lottery.txt', 'a+')
            file.write(res.cget("text")+ "\n"  + "You won: R8,584.00" + "\n")
            file.close()

    except ValueError:
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num4.delete(0, END)
        num5.delete(0, END)
        num6.delete(0, END)


#generator button
numberGen = Button(window, width=20, text="Generate Numbers", command=winnings)
numberGen.place(x=280, y=50)

#exit button function
def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None

#exit button
exitbtn = Button(window, command=close, text="exit")
exitbtn.place(x=280, y=100)

#reset button
def reset():
    res.config(text="")
    num1.delete(0,END)
    num2.delete(0,END)
    num3.delete(0,END)
    num4.delete(0,END)
    num5.delete(0,END)
    num6.delete(0,END)

clearbtn= Button(window, command=reset, text="clear")
clearbtn.place(x=409, y=100)


window.mainloop()
