from tkinter import *
import tkinter.messagebox

beClick = True
flag = 0


def checkForWin():
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
       button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
       button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
       button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
       button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
       button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
       button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
       button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        dissableButtons()


def buttonClick(b):
    global beClick, player1_name, player2_name, playerA, playerB, flag
    if(beClick == True and b["text"] == ""):
        b["text"] = "X"
        beClick = False
        flag = flag+1
        checkForWin()
    elif(beClick == False and b["text"] == ""):
        b["text"] = "O"
        beClick = True
        flag = flag+1
        checkForWin()


def dissableButtons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


root = Tk()
root.title("Tik Tak Toe Game")
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
player1_name = Entry(root, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)

player2_name = Entry(root, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
label = Label(root, text="Player 1 :", font="Times 20 bold",
              bg="white", fg="black", height=1, width=8)
label.grid(row=1, column=0)

label = Label(root, text="Player 2 :", font="Times 20 bold",
              bg="white", fg="black", height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button1))
button1.grid(row=3, column=0)

button2 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button2))
button2.grid(row=3, column=1)

button3 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button3))
button3.grid(row=3, column=2)

button4 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button4))
button4.grid(row=4, column=0)

button5 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button5))
button5.grid(row=4, column=1)

button6 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button6))
button6.grid(row=4, column=2)

button7 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button7))
button7.grid(row=5, column=0)

button8 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button8))
button8.grid(row=5, column=1)

button9 = Button(root, text="", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: buttonClick(button9))
button9.grid(row=5, column=2)
root.mainloop()
