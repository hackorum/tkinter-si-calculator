from tkinter import *

window = Tk()

# add widgets here


window.title("Simple Interest Calculator")
window.geometry("380x400")
window.configure(bg="lightcyan")


app_label = Label(
    window,
    text="Simple Interest Calculator",
    fg="black",
    bg="lightcyan",
    font=("Calibri", 20),
    bd=5,
)
app_label.place(x=50, y=20)

principle_label = Label(
    window,
    text="Enter principle",
    fg="black",
    bg="lightcyan",
    font=("Calibri", 12),
    bd=1,
)
principle_label.place(x=20, y=90)

principle = Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)


result_frame = LabelFrame(
    window, text="Result", bg="lightcyan", fg="black", font=("Calibri", 12)
)
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label = Label(
    result_frame, text=" ", bg="lightcyan", font=("Calibri", 12), width=33
)
result_label.place(x=20, y=20)
result_label.pack()

rate_label = Label(
    window, text="Enter rate", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1
)
rate_label.place(x=20, y=140)
rate = Entry(window, text="", bd=2, width=22)
rate.place(x=150, y=142)

time_label = Label(
    window, text="Enter time", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1
)
time_label.place(x=20, y=185)
time = Entry(window, text="", bd=2, width=22)
time.place(x=150, y=187)


def calculateSI():
    timeval = int(time.get())
    rateval = int(rate.get())
    principleval = int(principle.get())
    si = (timeval * rateval * principleval) / 100
    print(si)
    output_msg = Label(
        result_frame,
        text="SI is Rs. " + str(si),
        bg="lightcyan",
        font=("Calibri", 12),
        width=42,
        fg="black",
    )
    output_msg.place(x=20, y=40)
    output_msg.pack()


calc = Button(
    window,
    text="Calculate",
    bg="cyan",
    bd=0,
    font=("Calibri", 12),
    command=calculateSI,
)
calc.place(x=20, y=250)

window.mainloop()
