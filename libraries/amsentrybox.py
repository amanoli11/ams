import tkinter as tk
from tkinter import END, StringVar, ttk

def AMSEntryBox(parent, container, value, placeholder = None):

    def clear_place_holder(string):
            setattr(parent, value, string.get())

    def to_uppercase(*args):
        string.set(string.get().upper())

    def trace(*args):
        if string.get() == "":
            entry_box.insert(END, placeholder)

        if string.get() == placeholder:
            setattr(parent, value, '')
        else:
            setattr(parent, value, string.get())

    def remove_place_holder(string):
        if placeholder == string.get():
            entry_box.delete(0, END)


    string = StringVar()
    string.trace_add('write', to_uppercase)
    entry_box = ttk.Entry(container, textvariable=string)
    if placeholder is not None:
        entry_box.insert(END, placeholder)
    # entry_box.bind("<Button-1>", lambda event: clear_place_holder(string))
    # entry_box.bind("<KeyRelease>", lambda event: clear_place_holder(string))
    entry_box.bind("<KeyPress>", lambda event: remove_place_holder(string))
    entry_box.bind("<FocusOut>", trace)

    return entry_box