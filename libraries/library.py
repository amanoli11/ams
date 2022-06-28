import tkinter as tk
from tkinter import END, StringVar, ttk

class AMSComboBox():

    def __init__(self, container, parent_class, values, id, index, placeholder = "PLEASE INSERT A PLACEHOLDER"):

        # self.geometry("1000x600")

        # self.values = {102 : 'Item 1', 103 : 'Item 2', 104 : 'Item 3', 105: 'Item 4'}

        self.container = container

        self.parent_class = parent_class

        self.values = dict(values)

        self.update_index = None

        self.ddl_value_index = None

        self.ddl_name = None

        self.id = id

        self.index = index

        self.values_values = list(self.values.values())

        self.placeholder = placeholder

        # self.base_layout()

    def check(self, string, combobox):
        if string.get() == "" or string.get() == self.placeholder:
            combobox['values'] = self.values_values
        else:
            data = []
            for item in self.values_values:
                if string.get().lower() in item.lower():
                    data.append(item)
            combobox['values'] = data

    def remove_placeholder_while_typing(self, string, combobox):
        if string.get() == self.placeholder:
            combobox.set("")
    
    def insert_placeholder_on_focus_out(self, string, combobox):
        if string.get() == "":
            combobox.set(self.placeholder)


    def __call__(self):
        string = StringVar()
        combobox = ttk.Combobox(self.container, values=self.values_values, textvariable=string)
        combobox.bind('<<ComboboxSelected>>', lambda event: self.get_key(string.get()))
        combobox.bind("<KeyRelease>", lambda event: self.check(string, combobox))
        combobox.bind("<KeyPress>", lambda event: self.remove_placeholder_while_typing(string, combobox))
        combobox.bind("<FocusOut>", lambda event: self.insert_placeholder_on_focus_out(string, combobox))
        combobox.set(self.placeholder)
        # combobox.current(self.ddl_value_index)
        # combobox.grid(row=2, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


        return combobox

    def base_layout(self):
        string = StringVar()
        combobox = ttk.Combobox(self.container, values=self.values_values, textvariable=string)
        combobox.bind('<<ComboboxSelected>>', lambda event: self.get_key(string.get()))
        combobox.bind("<KeyRelease>", lambda event: self.check(string, combobox))
        combobox.set(self.placeholder)
        # combobox.current(self.ddl_value_index)
        # combobox.grid(row=2, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


        return combobox

    def current_id(self, value):
        for i in self.values.keys():
            if i == value:
                self.ddl_value_index = list(self.values.keys()).index(value)

        setattr(self.parent_class, self.index, self.ddl_value_index)
        # return self.ddl_value_index

    # def get_index(self):
    #     self.ddl_value_index = list(self.values.keys()).index(self.update_index)

    def get_key(self, string):
        for key, val in self.values.items():
            if val == string:
                self.update_index = key

        setattr(self.parent_class, self.id, self.update_index)

        self.current_id(self.update_index)

    def get_index(self):
        return self.update_index
        
        # self.get_index()

# app = Library()
# app.mainloop()
