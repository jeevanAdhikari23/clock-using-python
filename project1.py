from tkinter import *
# tkinter helps to create GUI and it is the only framework built into the standarad library

from tkinter.ttk import *
# It provides access to the TK themed Widget set

from time import strftime
# It helps us to convert time into string

root=Tk()
# It is an instance of tkinter frame.It helps to display the root window and manages all the components of the tkinter application
root.title("World clock")
def time():
    string=strftime('%H:%M:%S')
    Label.config(text=string)
    # This method is used to perform overwriting over label widget
    Label.after(1000,time)
    # This after()method calls the time function once after a delay of milliseconds within the tkinter mainloop()

Label=Label(root,font=("calibir",50,'bold'),background="black",foreground="aqua")
# The label is used to specify the container box where we can place the text or images

Label.pack(anchor='center')


time()
mainloop()
# This tells python to run the tkinter event loop 







