from tkinter import StringVar, ttk
import tkinter as tk

class CustomComboBox():


    def __init__(self, parent, list, index_value):

        ddl = []
        self.ddl = ddl

        self.ddl_value = None

        id = 0
        self.id = id

        self.index_value = index_value

        self.index_number = None

        self.parent = parent

        self.list = list

        for i in self.list:
            self.ddl.append(i[1])

        self.base_layout()


    def get_value(self, variable):
        self.ddl_value = variable.get()

        for i in self.list:
            if(i[1]) == variable.get():
                self.id = i[0]

        self.index_number = self.retrieve_index()
        print(self.index_number)


    def retrieve_index(self):
        index = self.ddl.index(self.index_value)
        return index

    def base_layout(self):
        variable = StringVar()

        combobox = ttk.Combobox(self.parent, value=self.ddl, textvariable = variable)
        combobox.bind('<<ComboboxSelected>>', self.get_value(variable))
        combobox.set('PLEASE SELECT A COMPANY')
        combobox.grid(row=2, column=1, pady=5, padx=15, sticky=tk.E+tk.W)