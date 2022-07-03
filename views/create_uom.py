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


        
        self.lf = ttk.LabelFrame(self, text='Create UOM')
        self.lf.grid(column=0, row=1, padx=10, pady=10, sticky=tk.NW)

        uom_name_label = ttk.Label(self.lf, text="UOM NAME")
        uom_name_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)


        self.uom_name_widget = AMSEntryBox(self, self.lf, value='uom_name', placeholder="ENTER A UOM")
        self.uom_name_widget.focus()
        self.uom_name_widget.grid(row=1, column=1, pady=5, padx=15, ipadx=6.5)

        is_active_label = ttk.Label(self.lf, text="IS ACTIVE")
        is_active_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

        
        self.is_active_widget = AMSComboBox(self.lf, self, values = self.is_active, id='is_active_value', index="is_active_index", placeholder="IS ACTIVE")
        self.is_active_widget.current(0)
        self.is_active_widget.grid(row=2, column=1)

        is_deleted_label = ttk.Label(self.lf, text="IS DELETED")
        is_deleted_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)

        
        self.is_deleted_widget = AMSComboBox(self.lf, self, values = self.is_active, id='is_deleted_value', index="is_deleted_index", placeholder="IS DELETED")
        self.is_deleted_widget.current(1)
        self.is_deleted_widget.grid(row=3, column=1)

        
        self.submit_btn_widget = ttk.Button(self.lf, text="SAVE UOM", command=self.save)
        self.submit_btn_widget.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

        
        self.update_btn_widget = ttk.Button(self.lf, text="UPDATE UOM", command=self.update)

        clear_btn = ttk.Button(self.lf, text="CLEAR", command=self.clear_field)
        clear_btn.grid(row=4, column=0, sticky=tk.W, pady=8, padx=13)

        options = tk.Menu(self.lf, tearoff = False)
        options.add_command(label ="RESET", command=self.reset_field)

        def option_menu(event):
            options.tk_popup(event.x_root, event.y_root)


        self.lf.bind("<Button-3>", option_menu)


        return self.lf

    def reset_field(self):
        self.update_btn_widget.grid_remove()
        self.submit_btn_widget.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

        self.clear_field()



    def clear_field(self):
        self.uom_name_widget.delete(0, END)
        self.uom_name_widget.focus()

        self.is_active_widget.current(0)
        self.is_deleted_widget.current(1)
        

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

        self.update_btn_widget.grid_remove()
        self.submit_btn_widget.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)
        self.clear_field()
        self.uom_name_widget.focus()
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

            self.submit_btn_widget.grid_remove()

            self.uom_name_widget.delete(0, END)
            self.uom_name_widget.insert(0, y[0])

            self.update_btn_widget.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)

            self.is_active_widget.current(AMSGetIndex(self.is_active, y[1]))

            self.is_deleted_widget.current(AMSGetIndex(self.is_active, y[2]))

        tree.bind('<<TreeviewSelect>>', item_selected)

        frame.grid(row=1, column=1, sticky=tk.NE)