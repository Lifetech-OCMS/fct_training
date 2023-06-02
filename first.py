import tkinter
window = tkinter.Tk()
window.title("home page")
frame = tkinter.Frame(window)
frame.pack()

#show the objects
user_info_frame = tkinter.LabelFrame(frame, text=" User Details Window:")
user_info_frame.grid(row=0, column=0, padx=110, pady=120)

user_name_label =tkinter.Label(user_info_frame, text ="Enter UserName")
user_name_label.grid(row=1, column=0,padx=20)
user_password_label =tkinter.Label(user_info_frame, text ="Enter Password")
user_password_label.grid(row=3, column=0)
user_name_entry=tkinter.Entry(user_info_frame)
user_name_entry.grid(row=1, column=1)
user_password_entry=tkinter.Entry(user_info_frame)
user_password_entry.grid(row=3, column=1)
#this is the function that will triger the window to launch
window.mainloop()