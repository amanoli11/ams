import tkinter as tk
from tkinter import StringVar, ttk
from amsentrybox import AMSEntryBox

class tkinterApp(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)

        self.geometry("1000x600")

#         self.demo_emtry_value = None

#         self.demo_emtry_value1 = None

#         label = ttk.Label(self, text="DEMO")
#         label.grid(row=0, column=0)

#         demo_entry = AMSEntryBox(self, placeholder="ENTER A VALUE", value = 'demo_emtry_value')
#         demo_entry.grid(row=0, column=1)

#         label1 = ttk.Label(self, text="DEMO1")
#         label1.grid(row=1, column=0)

#         demo_entry1 = AMSEntryBox(self, placeholder="ENTER A VALUE", value='demo_emtry_value1')
#         demo_entry1.grid(row=1, column=1)

#         def print_text():
#             print(self.demo_emtry_value)

#         button = ttk.Button(self, text='print_text', command=print_text)
#         button.grid(row=2, column=1)

        lst = ('value1', 'value2', 'value3')

        def check(self):
            if current_var.get() == "":
                combobox['values'] = lst
            else:
                data = []
                for item in lst:
                    if current_var.get().lower() in item.lower():
                        data.append(item)
                combobox['values'] = data

        def trace(*args):
            if current_var.get() == "":
                combobox.insert(tk.END, "ASD")

        def clear_place_holder(string):
            if "ASD" == string.get():
                combobox.delete(0, tk.END)

        current_var = tk.StringVar()
        combobox = ttk.Combobox(self, textvariable=current_var)
        combobox.set("ASD")
        combobox['values'] = lst
        combobox.bind("<KeyRelease>", check)
        combobox.bind("<FocusOut>", trace)
        # combobox.bind("<Button-1>", lambda event: clear_place_holder(current_var))
        combobox.grid(row=0, column=0)

        combobox = ttk.Combobox(self, textvariable=current_var)
        combobox.grid(row=1, column=0)

app = tkinterApp()
app.mainloop()