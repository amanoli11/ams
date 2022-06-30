import tkinter as tk
from tkinter import END, FIRST, TOP, StringVar, ttk
import psycopg2
# from controller.create_menu_controller import CreateMenuController

from create_uom import CreateUom
from model.create_uom_model import CreateUomModel
from controller.create_uom_controller import CreateUomController

from libraries.amsentrybox import AMSEntryBox
from libraries.amscombobox import AMSComboBox
from libraries.amstreeview import AMSStripedRows, AMSTreeVIew
from libraries.amsgetindex import AMSGetIndex

from libraries.static_values import is_active

class CreateMenu(ttk.Frame):

    def __init__(self, container):

        super().__init__(container)
        # container.geometry("1000x600")
        container.title("Create Menu")
        container.geometry('1200x600')
        container.width = 1200
        container.height = 600
        container.resizable(False, False)
        self.container = container
        self.uom_values = {}
        self.uom_list = []
        # self.uom_id = {}
        self.item_name1 = ""
        # self.price = 0
        self.uom = -1
        self.item_id = 0
        self.show_menu_ddl()
        # self.create_menu_items()
        self.controller = None
        self.output = {}
        self.selected_value = {}



        #libraries ko variable haru
        self.item_name = None
        self.price = None

        self.uom_id = None
        self.uom_index = None

        self.uom_ddl = None

        self.is_active = is_active

        self.is_active_value = True
        self.is_deleted_value = False

    def set_controller(self, controller):
        self.controller = controller
        self.collect_initial_values()
        self.create_menu_items()
        self.show_menu_items()

    def create_menu_items(self):
        label = ttk.Label(self, text="Create Menu", font="Verdana, 15")
        label.grid(column=0, row=0, sticky=tk.W, padx=10)


        
        self.lf = ttk.LabelFrame(self, text='Create Menu')
        self.lf.grid(column=0, row=1, padx=10, pady=(10, 400), sticky=tk.NW)

        # style = ttk.Style()
        # style.theme_use('alt')
        # style.configure("TLabelframe", bordercolor="green")

        item_name_label = ttk.Label(self.lf, text="ITEM NAME")
        item_name_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)



        self.item_name_widget = AMSEntryBox(self, self.lf, 'item_name', placeholder="PLEASE INSERT AN ITEM NAME")
        # item_name.bind("<KeyRelease>", caps)
        self.item_name_widget.focus()
        self.item_name_widget.grid(row=1, column=1, pady=5, padx=15, ipadx=40)


        price_label = ttk.Label(self.lf, text="PRICE")
        price_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

        def price(price_string):
            self.price = int(price_string.get())

        price_string = StringVar()
        self.price_widget = ttk.Spinbox(self.lf, from_=0, to=9999999, wrap=False, textvariable=price_string)
        self.price_widget.bind("<KeyRelease>", lambda event: price(price_string))
        self.price_widget.set(0)
        self.price_widget.grid(row=2, column=1, pady=5, padx=15, ipadx=30)

        
        uom_label = ttk.Label(self.lf, text="UOM")
        uom_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)

        self.uom_widget = AMSComboBox(self.lf, self, self.uom_ddl, 'uom_id', 'uom_index', placeholder="PLEASE CHOOSE AN UOM", filter=True)
        self.uom_widget.grid(row=3, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


        is_active_label = ttk.Label(self.lf, text="IS ACTIVE")
        is_active_label.grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
        
        self.is_active_widget = AMSComboBox(self.lf, self, self.is_active, 'is_active_value', 'is_active_index', placeholder="IS ACTIVE")
        self.is_active_widget.current(0)
        self.is_active_widget.grid(row=4, column=1, pady=5, padx=15, sticky=tk.E+tk.W)

        is_deleted_label = ttk.Label(self.lf, text="IS DELETED")
        is_deleted_label.grid(row=5, column=0, sticky=tk.W, pady=5, padx=5)

        self.is_deleted_widget = AMSComboBox(self.lf, self, self.is_active, 'is_deleted_value', 'is_deleted_index', placeholder="IS DELETED")
        self.is_deleted_widget.current(1)
        self.is_deleted_widget.grid(row=5, column=1, pady=5, padx=15, sticky=tk.E+tk.W)

        clear_btn = ttk.Button(self.lf, text="CLEAR", command= lambda: self.clear_values(event = None))

        clear_btn.bind('<Return>', self.clear_values)

        clear_btn.grid(row=6, column=0, sticky=tk.E)


        
        self.submit_btn = ttk.Button(self.lf, text="SAVE MENU", command=lambda: self.submit_menu(event = None))
        self.submit_btn.bind('<Return>', self.submit_menu)

        self.submit_btn.grid(row=6, column=1, sticky=tk.E, pady=8, padx=13)

        # label1 = ttk.Label(self, text="ACTIONS", font="Verdana, 15")
        # label1.grid(column=0, row=1, sticky=tk.W, padx=10)

        action_label_frame = ttk.LabelFrame(self, text='Actions')
        action_label_frame.grid(column=0, row=1, padx=10, pady=10)

        create_uom_btn = ttk.Button(action_label_frame, text="CREATE UOM", command=lambda: self.container.show_frame(CreateUomController, CreateUomModel, CreateUom))
        create_uom_btn.grid(column=0, row=0, padx=13, pady=10)

        take_order_btn = ttk.Button(action_label_frame, text="TAKE ORDER")
        take_order_btn.grid(column=1, row=0, padx=13, pady=10)


        options = tk.Menu(self.lf, tearoff = False)
        options.add_command(label ="RESET", command=self.reset_field)

        def option_menu(event):
            options.tk_popup(event.x_root, event.y_root)


        self.lf.bind("<Button-3>", option_menu)


    def reset_field(self):


        self.update_btn.grid_remove()



        self.submit_btn = ttk.Button(self.lf, text="SAVE MENU", command=lambda: self.submit_menu(event = None))
        self.submit_btn.bind('<Return>', self.submit_menu)

        self.submit_btn.grid(row=6, column=1, sticky=tk.E, pady=8, padx=13)

        self.clear_values(event = None)

    
    def update_menu_item(self, item_name, price, uom, is_active, is_deleted, uom_id, menu_id):
        
        self.item_name_widget.delete(0, END)
        self.item_name_widget.insert(END, item_name)

        self.price_widget.set(price)

        self.uom_widget.current(AMSGetIndex(self.uom_ddl, uom_id))

        self.is_active_widget.current(AMSGetIndex(self.is_active, is_active))

        self.is_deleted_widget.current(AMSGetIndex(self.is_active, is_deleted))

        self.submit_btn.grid_remove()

        # selected = self.tree.focus()
        # values = self.tree.item(selected, values=(name,))
        



        def update(self, event):

            selected = self.tree.focus()
            print(selected)
            self.tree.item(selected, values=(self.item_name, self.price, self.uom_widget.get(), self.is_active_value, self.is_deleted_value, self.uom_id, menu_id))
            self.controller.update_menu_item(menu_id, self.item_name, self.price, self.uom_id, self.is_active_value, self.is_deleted_value)

            self.clear_values(event=None)
            
            self.controller.lister(self)

        self.update_btn = ttk.Button(self.lf, text="UPDATE MENU", command = lambda: update(self, event= None))
        self.update_btn.bind('<Return>', lambda event: update(self, event = None))

        self.update_btn.grid(row=6, column=1, sticky=tk.E, pady=8, padx=13)


    def show_menu_items(self):
        
        columns = ("MENU NAME", "PRICE", "UOM", "IS ACTIVE", "IS DELETED", "UOM ID", "MENU ID")
        frame, tree, option = AMSTreeVIew(self, columns, self.output, frame_name="MENU ITEMS", table_height=20)

        self.tree = tree
        self.tree["displaycolumns"]=("MENU NAME", "PRICE", "UOM", "IS ACTIVE", "IS DELETED")

        self.tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=320)
        self.tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=100)
        self.tree.column("# 3", anchor=tk.W, stretch=tk.NO, width=115)
        self.tree.column("# 4", anchor=tk.W, stretch=tk.NO, width=85)
        self.tree.column("# 5", anchor=tk.W, stretch=tk.NO, width=95)

        def item_selected(event):

            x = self.tree.selection()
            y = self.tree.item(x)['values']

            print(y)

            self.item_name = y[0]
            self.price = y[1]
            self.uom_id = y[5]
            self.is_active_value = y[3]
            self.is_deleted_value = y[4]

            self.update_menu_item(y[0], y[1], y[2], y[3], y[4], y[5], y[6])


        self.tree.bind('<<TreeviewSelect>>', item_selected)

        frame.grid(row=1, column=1, sticky=tk.NE, padx=(30, 0))


    def show_menu_ddl(self):
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("select id, uom from uom")
        result = c.fetchall()
        out = [row[1] for row in result]
        # out = [item for t in result for item in t]
        self.uom_values = out

        self.uom_list = result

        conn.commit()
        conn.close()

    def clear_values(self, event):
        
        self.item_name_widget.delete(0, END)
        
        self.price_widget.delete(0, END)
        self.price_widget.set(0)
        
        self.uom_widget.delete(0, END)
        self.uom_widget.set("PLEASE SELECT AN UOM")
        
        self.item_name_widget.focus()

        self.is_active_value = True
        self.is_deleted_value = False

        self.is_active_widget.current(0)
        self.is_deleted_widget.current(1)

    def submit_menu(self, event):

        # self.tree.insert("", index=0, values = (self.item_name_widget.get(), self.price_widget.get(), self.uom_widget.get(), self.is_active_value, self.is_deleted_value, self.uom_id))
        # self.controller.save(self.item_name_widget.get(), self.price_widget.get(), self.uom_widget.get(), self.uom_id, self.is_active_value, self.is_deleted_value)

        # self.controller.lister(self)
        # self.clear_values(event=None)

        self.controller.save(self.item_name_widget.get(), self.price_widget.get(), self.uom_widget.get(), self.uom_id, self.is_active_value, self.is_deleted_value)
        self.tree.delete(*self.tree.get_children())
        self.controller.lister(self)

        AMSStripedRows(self.tree, self.output)

        self.clear_values(event=None)

        # for i in self.output:
        #     self.tree.insert("", END, values=i)




        # selected = self.tree.focus()
        # print(selected)
        # self.tree.item(selected, values=(self.item_name, self.price, self.uom_widget.get(), self.is_active_value, self.is_deleted_value, uom_id, menu_id))
        # self.controller.update_menu_item(menu_id, self.item_name, self.price, self.uom_id, self.is_active_value, self.is_deleted_value)
        # self.clear_values(event=None)





        # self.controller.lister(self)
        # self.show_menu_items()

    def submit_updated_menu(self, item_id, item_name, price, uom, uom_id, item_del, price_del, uom_del):
        self.controller.update(item_id, item_name, price, uom, uom_id)
        self.clear_values(item_del, price_del, uom_del)
        self.show_menu_items()
        self.create_menu_items()


    # def submit_menu(self, item_name, price, uom, item_del, price_del, uom_del):
    #     CreateMenuController(self, item_name, price, uom)

    #     item_del, price_del, uom_del


    def collect_initial_values(self):
        self.controller.collect_initial_values(self)
        self.controller.lister(self)
