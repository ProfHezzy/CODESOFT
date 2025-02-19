import tkinter as tk

#Function to handle the functionality of the calculator
def onclick(buttonTxt):

    if buttonTxt == "Back":
        latest_text = screen_text.get().strip()
        if latest_text:
            screen_text.set(latest_text[:-1])
        return
    
    if buttonTxt == "C":
        screen_text.set("") #Clear the screen
        return

    if buttonTxt == "=":
        try:
            screen_text.set(str(eval(screen_text.get())))
        except:
            screen_text.set("Error")
        return
    
    if screen_text.get() == "Error":
        screen_text.set("")
        
    screen_text.set(screen_text.get() + buttonTxt)


#main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("380x550")
root.config(bg='blue')

#Screen for the calculator
screen_text = tk.StringVar()
screen = tk.Entry(root, textvariable = screen_text, font = ("Arial", 15), width=32, borderwidth=5, bg="light grey", justify="right", state="readonly");
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=20, ipady=20)

#Buttons
btn7 = tk.Button(root, text="7", command=lambda:onclick("7"), font=("Arial", 14), width=5, height=2)
btn7.grid(row=1, column=0, padx=5, pady=10)

btn8 = tk.Button(root, text="8", command=lambda:onclick("8"), font=("Arial", 14), width=5, height=2)
btn8.grid(row=1, column=1, padx=5, pady=10)

btn9 = tk.Button(root, text="9", command=lambda:onclick("9"), font=("Arial", 14), width=5, height=2)
btn9.grid(row=1, column=2, padx=5, pady=10)

btnDiv = tk.Button(root, text="/", command=lambda:onclick("/"), font=("Arial", 14), width=5, height=2)
btnDiv.grid(row=1, column=3, padx=5, pady=10)

btn4 = tk.Button(root, text="4", command=lambda:onclick("4"), font=("Arial", 14), width=5, height=2)
btn4.grid(row=2, column=0, padx=10, pady=10)

btn5 = tk.Button(root, text="5", command=lambda:onclick("5"), font=("Arial", 14), width=5, height=2)
btn5.grid(row=2, column=1, padx=10, pady=10)

btn6 = tk.Button(root, text="6", command=lambda:onclick("6"), font=("Arial", 14), width=5, height=2)
btn6.grid(row=2, column=2, padx=10, pady=10)

btnMul = tk.Button(root, text="*", command=lambda:onclick("*"), font=("Arial", 14), width=5, height=2)
btnMul.grid(row=2, column=3, padx=10, pady=10)

btn1 = tk.Button(root, text="1", command=lambda:onclick("1"), font=("Arial", 14), width=5, height=2)
btn1.grid(row=3, column=0, padx=10, pady=10)

btn2 = tk.Button(root, text="2", command=lambda:onclick("2"), font=("Arial", 14), width=5, height=2)
btn2.grid(row=3, column=1, padx=10, pady=10)

btn3 = tk.Button(root, text="3", command=lambda:onclick("3"), font=("Arial", 14), width=5, height=2)
btn3.grid(row=3, column=2, padx=10, pady=10)

btnSub = tk.Button(root, text="-", command=lambda:onclick("-"), font=("Arial", 14), width=5, height=2)
btnSub.grid(row=3, column=3, padx=10, pady=10)

btnC = tk.Button(root, text="C", command=lambda:onclick("C"), font=("Arial", 14), bg='red', width=5, height=2)
btnC.grid(row=4, column=0, padx=10, pady=10)

btn0 = tk.Button(root, text="0", command=lambda:onclick("0"), font=("Arial", 14), width=5, height=2)
btn0.grid(row=4, column=1, padx=10, pady=10)

btnDot = tk.Button(root, text=".", command=lambda:onclick("."), font=("Arial", 14), width=5, height=2)
btnDot.grid(row=4, column=2, padx=10, pady=10)

btnAdd = tk.Button(root, text="+", command=lambda:onclick("+"), font=("Arial", 14), width=5, height=2)
btnAdd.grid(row=4, column=3, padx=10, pady=10)

btnEqual = tk.Button(root, text="=", command=lambda:onclick("="), font=("Arial", 14), bg='green', width=23, height=2)
btnEqual.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

btnBack = tk.Button(root, text="Back", command=lambda:onclick("Back"), font=("Arial", 14), width=5, height=2)
btnBack.grid(row=5, column=3, padx=10, pady=10)

bylabel = tk.Label(root, text="Developed by: PROF. Hezzy", font=("Arial", 10))
bylabel.grid(row=6, column=0, columnspan=4, padx=10, pady=10)



#Run the main loop
root.mainloop()