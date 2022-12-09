import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("My pizza")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame =tkinter.LabelFrame(frame, text="Customer Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="last Name")
last_name_label.grid(row=0, column=1)
tel_name_label = tkinter.Label(user_info_frame, text="Phone Number")
tel_name_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame, text="First Name")
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame, text="last Name")
last_name_entry.grid(row=1, column=1)
tel_name_entry = tkinter.Entry(user_info_frame, text="Phone Number")
tel_name_entry.grid(row=1, column=2)

pizza_info_frame = tkinter.LabelFrame(frame, text="Choose your Information")
pizza_info_frame.grid(row= 2, column=2, padx=20, pady=20)

pizza_label = tkinter.Label(pizza_info_frame, text="Pizza Name")
pizza_combobox = ttk.Combobox(pizza_info_frame, values=["Hot pizza", "Beef pizza", "Chiken pizza", "Chiken pizza"])
pizza_label.grid(row=0, column=0)
pizza_combobox.grid(row=1, column=0)

sauce_label = tkinter.Label(pizza_info_frame, text="Select sauce")
sauce_combobox = ttk.Combobox(pizza_info_frame, values=["BBQ", "red pizza sauce", "american sauce"])
sauce_label.grid(row=1, column=1)
sauce_combobox.grid(row=2, column=1)



print("Hello world")
window.mainloop()
