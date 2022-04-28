from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("400x300+30+15")

btn = Button(window, text="Click to Change Color", fg="black", activebackground="yellow")
btn.place(x=140, y= 130)

window.mainloop()