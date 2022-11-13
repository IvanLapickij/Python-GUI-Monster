from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Welcome")

frame = Frame(window, width=400, height=400)
frame.place(x=10,y=180)
label1 = Label(window, text="Ball Image", fg="blue",bg="yellow", font=("arial", 14, "bold"))
label1.place(x=2, y=2)

canvas = Canvas(window, width = 350, height = 350)
canvas.place(x=10,y=40)
#img = PhotoImage(file="C:\\Users\\dbyrne\\PycharmProjects\\pythonProject\\Ball.jpg")
img = PhotoImage(file="Ball2.png")
canvas.create_image(130,130, anchor=CENTER, image=img)

mainloop()