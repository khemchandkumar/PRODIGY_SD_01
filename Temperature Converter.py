import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("900x510")
root.resizable(False, False)


def getFont(size=9, bold=False):
    return("TkDefaultFont",size,"bold" if bold else "normal")

def validate(P):
    if P == "" or P == "-":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False



calcFunc = {
    "cf":lambda x: x*9/5+32,
    "ck":lambda x: x+273.15,
    "fc":lambda x: (x-32)*5/9,
    "kc":lambda x: x-273.15
}

calcFunc["fk"] = lambda x: calcFunc["ck"](calcFunc["fc"](x))
calcFunc["kf"] = lambda x: calcFunc["cf"](calcFunc["kc"](x))

def convert(fromInpt, fromUnitVar, toUnitVar, resultVar):
    fromU = fromUnitVar.get().lower()
    toU = toUnitVar.get()[0].lower()

    try:
        val = float(fromInpt.get())
    except ValueError:
        resultVar.set("Error!")
        return

    if fromU == toU:
        res = val
    else:
        key = fromU + toU
        if key not in calcFunc:
            resultVar.set("Unsupported")
            return
        res = calcFunc[key](val)

    resultVar.set(f"{res:.2f} °{toU.upper()}")

reg = root.register(validate)

borderFrame = tk.Frame(root, bg="#EA5D11", width=450, height=510)
borderFrame.place(x=0,y=0)

leftFrame = tk.Frame(borderFrame, bg="#212121", width=440, height=500)
leftFrame.place(x=5,y=5)

enterLabel = tk.Label(leftFrame, text="Enter Temperature", bg="#212121", fg="#EA5D11", font=("Helvetica", 25, "bold","underline"))
enterLabel.place(x=30,y=10)

degLabel = tk.Label(leftFrame, text="Degree", bg="#212121", fg="#EA5D11", font=("Helvetica", 15, "bold"))
degLabel.place(x=30,y=120)

inptEntry = tk.Entry(leftFrame, bg="#303030", fg="#d72121", insertbackground="#d72121", borderwidth=5,
                     relief="flat", validatecommand=(reg, "%P"), validate="key",font="bold")
inptEntry.place(x=30,y=160, width=265, height=42)

unitVar = tk.StringVar(root)
unitVar.set("C")

convertVar = tk.StringVar(root)
convertVar.set("Fahrenheit")

s = ttk.Style()
s.configure("unit.TMenubutton", background="#EA5D11", relief="flat")
s.configure("convertTo.TMenubutton", relief="flat", background="#EA5D11",foreground="#212121", font="bold")

unitMenu = ttk.OptionMenu(leftFrame, unitVar, "C", "C", "F", "K", style="unit.TMenubutton")
unitMenu.place(x=300,y=160, width=50, height=42)

convertLabel = tk.Label(leftFrame, text="Convert To", bg="#212121", fg="#EA5D11", font=("Helvetica", 15, "bold"))
convertLabel.place(x=30, y=280)

convertMenu = ttk.OptionMenu(leftFrame, convertVar, "Fahrenheit", "Celsius", "Fahrenheit", "Kelvin", style="convertTo.TMenubutton")
convertMenu.place(x=30,y=320, width=320, height=42)

convertButton = tk.Button(leftFrame, text="Convert", bg="#EA5D11", fg="#212121", font=("Helvetica", 12, "bold"),
                          relief="flat", activebackground="#EA5D11", bd=0)
convertButton.place(x=150, y=420, width=140, height=40)


rightFrame = tk.Frame(root, bg="#EA5D11", width=450, height=510)
rightFrame.place(x=450,y=0)

resultVar = tk.StringVar(root)
resultVar.set("")

resultLabel = tk.Label(rightFrame, textvariable=resultVar, bg="#EA5D11", fg="#212121", font=("Helvetica",64, "bold"))
resultLabel.place(relx=0.5,rely=0.4901, anchor=tk.CENTER)

convertButton.configure(command=lambda: convert(inptEntry,unitVar,convertVar,resultVar))

root.mainloop()