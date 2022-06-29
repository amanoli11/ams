import tkinter as tk
from tkinter import END, StringVar, ttk


# # importing sys
# import sys
  
# # adding Folder_2 to the system path
# sys.path.insert(0, '/home/amanoli/ams')

from libraries.amscombobox import AMSComboBox
from libraries.amsentrybox import AMSEntryBox
from libraries.amstreeview import AMSTreeVIew
from libraries.amsdbconnector import AMSDbConnector
from libraries.amsgetindex import AMSGetIndex

class CreateUom(ttk.Frame):
    
    def __init__(self, container):
        super().__init__(container)

        container.title("Create UOM")
        container.geometry('820x500')
        container.width = 820
        container.height = 500
        container.resizable(False, False)

        self.uom_id = 0
        self.uom_name = ''
        self.uom_list = {}

        self.is_active_value = True
        self.is_deleted_value = False

        self.is_active = [(True, 'YES'), (False, 'NO')]


    def set_controller(self, controller):
        self.controller = controller
        self.base_layout()
        self.show_uom_items()

    def base_layout(self):
        label = ttk.Label(self, text="Create UOM", font="Verdana, 15")
        label.grid(column=0, row=0, sticky=tk.W, padx=10)


        global lf
        lf = ttk.LabelFrame(self, text='Create UOM')
        lf.grid(column=0, row=1, padx=10, pady=10, sticky=tk.NW)

        uom_name_label = ttk.Label(lf, text="UOM NAME")
        uom_name_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)


        global uom_name
        uom_name = AMSEntryBox(self, lf, value='uom_name', placeholder="ENTER A UOM")
        uom_name.focus()
        uom_name.grid(row=1, column=1, pady=5, padx=15, ipadx=6.5)

        is_active_label = ttk.Label(lf, text="IS ACTIVE")
        is_active_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

        global is_active
        is_active = AMSComboBox(lf, self, values = self.is_active, id='is_active_value', index="is_active_index", placeholder="IS ACTIVE")
        is_active.current(0)
        is_active.grid(row=2, column=1)

        is_deleted_label = ttk.Label(lf, text="IS DELETED")
        is_deleted_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)

        global is_deleted
        is_deleted = AMSComboBox(lf, self, values = self.is_active, id='is_deleted_value', index="is_deleted_index", placeholder="IS DELETED")
        is_deleted.current(1)
        is_deleted.grid(row=3, column=1)

        global submit_btn
        submit_btn = ttk.Button(lf, text="SAVE UOM", command=self.save)
        submit_btn.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

        global update_btn
        update_btn = ttk.Button(lf, text="UPDATE UOM", command=self.update)

        clear_btn = ttk.Button(lf, text="CLEAR", command=self.clear_field)
        clear_btn.grid(row=4, column=0, sticky=tk.W, pady=8, padx=13)

        options = tk.Menu(lf, tearoff = False)
        options.add_command(label ="RESET", command=self.reset_field)

        def option_menu(event):
            options.tk_popup(event.x_root, event.y_root)


        lf.bind("<Button-3>", option_menu)


        return lf

    def reset_field(self):
        update_btn.grid_remove()
        submit_btn.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

        self.clear_field()



    def clear_field(self):
        uom_name.delete(0, END)
        uom_name.focus()

        is_active.current(0)
        is_deleted.current(1)
        

    def save(self):
        self.controller.save(self.uom_name, self.is_active_value, self.is_deleted_value)
        print(self.is_active_value)
        print(self.is_deleted_value)
        self.show_uom_items()

    def update(self):
        self.controller.update(self.uom_name, self.is_active_value, self.is_deleted_value, self.uom_id)
        # self.show_uom_items()
        # self.save_uom()
        self.uom_id = 0

        update_btn.grid_remove()
        submit_btn.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)
        self.clear_field()
        uom_name.focus()
        self.show_uom_items()


    def show_uom_items(self):
        
        self.controller.uom_list(self)

        columns = ("UOM NAME", "IS ACTIVE", "IS DELETED")
        frame, tree, menu_bar  = AMSTreeVIew(self, columns, self.uom_list, frame_name="UOM LIST", table_height=15)

        tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=250)
        tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=100)
        tree.column("# 3", anchor=tk.E, stretch=tk.NO, width=100)


        def item_selected(event):

            x = tree.selection()
            y = tree.item(x)['values']

            self.uom_name = y[0]
            self.uom_id = y[3]

            submit_btn.grid_remove()

            uom_name.delete(0, END)
            uom_name.insert(0, y[0])

            update_btn.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

            is_active.current(AMSGetIndex(self.is_active, y[1]))

            is_deleted.current(AMSGetIndex(self.is_active, y[2]))

        tree.bind('<<TreeviewSelect>>', item_selected)

        frame.grid(row=1, column=1, sticky=tk.NE)