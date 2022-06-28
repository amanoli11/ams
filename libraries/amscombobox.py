import tkinter as tk
from tkinter import END, StringVar, ttk


def AMSComboBox(container, parent_class, values, id, index, placeholder = "PLEASE INSERT A PLACEHOLDER", filter = False):

    def get_key(e):
        for key, val in dict_values.items():
            if val == string.get():
                update_index = key

        setattr(parent_class, id, update_index)

        current_id(update_index)

        combobox['values'] = list(dict_values.values())

    def check(e):
        if string.get() == "" or string.get() == placeholder:
            combobox['values'] = list(dict_values.values())
        else:
            data = []
            for item in list(dict_values.values()):
                if string.get().lower() in item.lower():
                    data.append(item)
            combobox['values'] = data


    def current_id(update_index):
        for i in dict_values.keys():
            if i == update_index:
                ddl_value_index = list(dict_values.keys()).index(update_index)

        setattr(parent_class, index, ddl_value_index)

    def remove_placeholder_while_typing(e):
        if string.get() == placeholder:
            combobox.set("")
    
    def insert_placeholder_on_focus_out(e):
        if string.get() == "":
            combobox.set(placeholder)

    def clear_placeholder(e):
        combobox.set("")

    def asd(e):
        combobox['values'] = list(dict_values.values())
        print('activated')



    dict_values = dict(values)

    string = StringVar()
    combobox = ttk.Combobox(container, values=list(dict_values.values()), textvariable=string)
    
    if filter == False:
        combobox.bind('<<ComboboxSelected>>', get_key)
        combobox.config(state='readonly')
    
    if filter:
        combobox.bind("<KeyPress>", remove_placeholder_while_typing)
        combobox.bind("<KeyRelease>", check)
        combobox.bind('<<ComboboxSelected>>', get_key)
        combobox.bind("<FocusOut>", insert_placeholder_on_focus_out)
        combobox.bind("<Tab>", asd)
        # container.bind("<Leave>", asd)
        # parent_class.bind("<Leave>", asd)
        combobox.bind("<Alt-c>", clear_placeholder)
    
    
    combobox.set(placeholder)


    return combobox
