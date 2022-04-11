from tkinter import *
import backend


def view_command():
    list1.delete(0, END)  # to delete the previous enteries
    for row in backend.view():  # calling the view function from backend
        list1.insert(END, row)  # inserting in the list box we created below


def search_command():
    list1.delete(0, END)  # clearing the list box
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), price_text.get()):
        list1.insert(END, row)


def insert_command():
    backend.backendInsert(title_text.get(), author_text.get(),
                          year_text.get(), price_text.get())  # inserting in the database
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), price_text.get()))  # displaying only the inserted item in the listbox


def get_selected_row(event):  # to get the row from the listbox when we click on it
    global selected_tuple
    index = list1.curselection()[0]  # index is the id of the row
    # selected tuple as the data is in the form of tuple
    selected_tuple = list1.get(index)

    e1.delete(0, END)  # here we are adding the data in the entry boxes
    e1.insert(END, selected_tuple[1])

    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])

    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])

    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def update_command():
    # updating the data, click on the data to be updated, it will be displayed in the entry boxes
    # make the required changes, and then click update, click on viewall to see the updates
    backend.update(title_text.get(), author_text.get(),
                   year_text.get(), price_text.get(), selected_tuple[0])


def delete_command():
    # deleting the selected row
    backend.delete(selected_tuple[0])


window = Tk()  # making the window at frontend
window.title("Innogeeks Project")  # title of the window
# window.geometry("500x650")

# label for the text boxes
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)
l2 = Label(window, text='Author')
l2.grid(row=0, column=2)
l3 = Label(window, text='Year')
l3.grid(row=1, column=0)
l4 = Label(window, text='Price')
l4.grid(row=1, column=2)

# entry boxes
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

price_text = StringVar()
e4 = Entry(window, textvariable=price_text)
e4.grid(row=1, column=3)

# creating the display box (listbox)
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
# scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# attaching the scrollbar to listbox and vice versa
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# applying the selected row function
list1.bind("<<ListboxSelect>>", get_selected_row)

# buttons for the query
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

# to display the window
window.mainloop()
