import tkinter as tk
from tkinter import DISABLED, END, StringVar, ttk
import json
from tkinter import messagebox
from libraries.amstreeview import AMSTreeVIew
from libraries.library import AMSComboBox
from libraries.amsgetindex import AMSGetIndex
from libraries.amsbill import AMSBill

class TakeOrder(tk.Frame):
    
    def __init__(self, container):
        super().__init__(container)

        container.geometry('850x600')
        container.width = 850
        container.height = 600
        container.resizable(False, False)
        container.title("Take Order")
        container.bind('<Alt-t>', self.save_orders)
        container.bind('<Alt-u>', self.update_orders)

        container.bind('<Alt-b>', self.create_bill)

        self.table_number_ddl = {}
        self.attendant_ddl = {}
        self.company_ddl = {}
        self.menu_price = {}
        self.occupied_tables = {}

        #for table ddl
        self.table_number_value = None
        self.table_number_index = None


        #for attendant ddl
        self.attendant_value = None
        self.attendant_index = None


        #for table ddl
        self.company_value = None
        self.company_index = None


        #for menu ddl
        self.menu_value = None
        self.menu_index = None


        #for listing ordered items
        self.ordered_items = {}
        self.list_items = []


        #default values
        self.default_table_number = None
        self.uom = None
        self.price = None

        self.is_occupied = False


        self.save_orders_list = []


        #For action buttons
        self.save_order_btn = ttk.Button(self, text="TAKE ORDER", underline=0, command = lambda: self.save_orders(event=None))
        
        self.update_order_btn = ttk.Button(self, text="UPDATE ORDER", underline=0, command = lambda: self.update_orders(event=None))


    def set_controller(self, controller):
        self.controller = controller
        self.get_table_number()
        self.get_attendant()
        self.get_company()
        self.get_menu()
        self.base_layout()
        self.items()
        self.show_uom_items()
        # self.action()

    def base_layout(self):
        label = ttk.Label(self, text="Take Order", font="Verdana, 15")
        label.grid(column=0, row=0, sticky=tk.W, padx=10)

        lf = ttk.LabelFrame(self, text='Table Details')
        lf.grid(column=0, row=1, padx=10, pady=10, sticky=tk.NW)

        table_number_label = ttk.Label(lf, text="TABLE NUMBER")
        table_number_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)

        table_number = AMSComboBox(container=lf, parent_class=self, values=self.table_number_ddl, id='table_number_value', index='table_number_index', placeholder='PLEASE SELECT A TABLE')
        table_number1 = table_number()
        table_number1.current(self.default_table_number)
        table_number1.bind('<<ComboboxSelected>>', lambda event: self.check_occupied_table(self.table_number_value, attendant1, company1), add=True)
        table_number1.focus()
        table_number1.grid(row=0, column=1, pady=5, padx=15, sticky=tk.E+tk.W, ipadx=50)


        attendant_label = ttk.Label(lf, text="ATTENDANT")
        attendant_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)

        attendant = AMSComboBox(container = lf, parent_class = self, values=self.attendant_ddl, id='attendant_value', index='attendant_index', placeholder='PLEASE SELECT AN ATTENDANT')
        attendant1 = attendant()
        # attendant1.current(self.attendant)
        attendant1.grid(row=1, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


        company_label = ttk.Label(lf, text="COMPANY")
        company_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

        company = AMSComboBox(container=lf, parent_class=self, values=self.company_ddl, id='company_value', index='company_index', placeholder='PLEASE SELECT A COMPANY')
        company1 = company()
        # company1.current(self.company)
        company1.grid(row=2, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


    def items(self):
        item_lf = ttk.LabelFrame(self, text='Item Details')
        item_lf.grid(column=1, row=1, padx=10, pady=10, sticky=tk.NW)


        menu_label = ttk.Label(item_lf, text="MENU")
        menu_label.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        def get_uom(uom):
            for i in self.menu_price:
                if i[0] == self.menu_value:
                    self.uom = i[3]

            uom.config(state="normal")
            uom.delete(0, END)
            uom.insert(0, self.uom)
            uom.configure(foreground='green')
            uom.configure(state='disabled')
            

        # menu = ttk.Combobox(item_lf, value=self.menu, textvariable = menu_variable)
        # menu.set('PLEASE SELECT A MENU')
        # menu.bind('<<ComboboxSelected>>', lambda event: get_uom(uom))
        # menu.grid(row=1, column=2, sticky=tk.NE, padx=5, pady=5)

        menu = AMSComboBox(container=item_lf, parent_class=self, values=self.menu, id='menu_value', index='menu_index', placeholder='PLEASE SELECT A MENU')
        menu1 = menu()
        menu1.bind('<<ComboboxSelected>>', lambda event: get_uom(uom), add=True)
        menu1.grid(row=1, column=2, sticky=tk.NE, padx=5, pady=5)


        qty_label = ttk.Label(item_lf, text="QUANTITY")
        qty_label.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)

        qty = ttk.Entry(item_lf, width=21)
        # qty.insert(END, self.uom_name)
        qty.grid(row=2, column=2, pady=5, padx=5)

        uom_label = ttk.Label(item_lf, text="UOM")
        uom_label.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)
        
        uom = ttk.Entry(item_lf, width=21)
        uom.grid(row=3, column=2, pady=5, padx=5)
        uom.configure(state='disabled')

        add_btn = ttk.Button(item_lf, text="ADD", command=lambda: self.add_items(qty.get(), menu1, qty, uom))
        add_btn.grid(row=1, column=3, sticky=tk.W, padx=13)

        add_btn.bind('<Return>', lambda event: self.add_items(qty.get(), menu1, qty, uom))


        clear_btn = ttk.Button(item_lf, text="CLEAR", command = lambda: self.clear_values(menu1, qty, uom))
        clear_btn.grid(row=2, column=3, sticky=tk.W, padx=13)

        clear_btn.bind('<Return>', lambda event: self.clear_values(menu1,
                                                                qty, uom))

        # return item_lf

    
    def show_uom_items(self):

        # self.items()

        style = ttk.Style()


        columns = ("ITEM NAME", "PRICE", "QTY", "TOTAL PRICE")
        frame, tree, options = AMSTreeVIew(self, columns, self.list_items, frame_name = "ORDERS LIST", table_height=10)
        tree.column("# 2", anchor=tk.E, stretch=tk.NO)
        tree.column("# 3", anchor=tk.E, stretch=tk.NO)
        tree.column("# 4", anchor=tk.E, stretch=tk.NO)
        # tree = ttk.Treeview(self, columns=columns, show='headings', height=19)
        # tree.heading('ITEM NAME', text='ITEM NAME')
        # tree.heading('PRICE', text='PRICE')
        # tree.heading('QTY', text='QTY')
        # tree.heading('TOTAL PRICE', text='TOTAL PRICE')

        # tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=280)
        # tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=80)
        # tree.column("# 3", anchor=tk.E, stretch=tk.NO, width=50)
        # tree.column("# 4", anchor=tk.E, stretch=tk.NO, width=120)

        
        # self.total_price = 0
        # tree.tag_configure('oddcolumn', background='white')
        # tree.tag_configure('evencolumn', background='#88bdb6')
        # count = 0

        # for i in self.list_items:
        #     if count % 2 == 0:
        #         tree.insert('', tk.END, values=i, tags='oddcolumn')
        #     else:
        #         tree.insert('', tk.END, values=i, tags='evencolumn')
        #     count += 1
        #     self.total_price = self.total_price + i[3]

        self.total_price = 0
        for i in self.list_items:
            self.total_price = self.total_price + i[3]

        self.total_ordered_price(frame)

        frame.grid(row=2, column=0, sticky=tk.NE, padx=10, pady=(20,10), columnspan=2)


    def action(self):

        if self.is_occupied == False:
            self.update_order_btn.grid_remove()
            self.save_order_btn.grid(row=3, column=1, sticky=tk.NE, padx=(0, 110))
        else:
            self.save_order_btn.grid_remove()
            self.update_order_btn.grid(row=3, column=1, sticky=tk.NE, padx=(0, 110))

        create_bill_btn = ttk.Button(self, text="CREATE BILL", underline=7, command=lambda: self.create_bill(event=None))
        create_bill_btn.grid(row=3, column=1, sticky=tk.NE, padx=10)

    def create_bill(self, event):
        print(self.list_items)
        
        item_name = []
        price = []
        quantity = []
        total_amount = []
        uom_name = []

        bill_dict = {}

        for i in self.list_items:
            item_name.append(i[0])
            price.append(i[1])
            quantity.append(i[2])
            total_amount.append(i[3])
            uom_name.append(i[4])

        bill_dict["ITEM NAME"] = item_name
        bill_dict["PRICE"] = price
        bill_dict["QTY"] = quantity
        bill_dict["UOM"] = uom_name
        bill_dict["TOTAL"] = total_amount

        converted_list = []
        converted_tuple = ()

        for i in self.list_items:
            converted_tuple = (i[0], i[1], i[2], i[4], i[3])
            converted_list.append(converted_tuple)

        attendant_name = None
        for i in self.attendant_ddl:
            if self.attendant_value == i[0]:
                attendant_name = i[1]

        company_name = None
        for i in self.company_ddl:
            if self.company_value == i[0]:
                company_name = i[1]

        table_number = None
        for i in self.table_number_ddl:
            if self.table_number_value == i[0]:
                table_number = i[1]

        if len(self.list_items) > 0:
            AMSBill(bill_dict, converted_list, attendant_name, company_name, table_number, float(self.total_price), self.table_number_value, controller=self.controller, parent = self, save_order=self.save_orders_list)
            # self.reset_page()
        else:
            messagebox.showwarning("WARNING", "This Item List is Empty.")

        # try:
        #     # self.occupied_tables["table_id"] = self.table_number_value
        #     # self.occupied_tables["attendant_id"] = self.attendant_value
        #     # self.occupied_tables["company_id"] = self.company_value
        #     # self.occupied_tables["ordered_list"] = json.dumps(self.list_items)
            
        #     # self.controller.save_orders(self, self.occupied_tables)
        #     self.save_orders(event=None)
        # except:
        #     # self.controller.update_orders(json.dumps(self.list_items), self.table_number_value)
        #     self.update_orders()

            

    def total_ordered_price(self, frame):
        total_price = ttk.Label(frame, text="TOTAL PRICE: "+ str(self.total_price))
        total_price.grid(row=2, column=0, sticky=tk.NE, padx=(0, 10))

    def save_orders(self, event):
        self.occupied_tables["table_id"] = self.table_number_value
        self.occupied_tables["attendant_id"] = self.attendant_value
        self.occupied_tables["company_id"] = self.company_value
        self.occupied_tables["ordered_list"] = json.dumps(self.list_items)
        

        # self.controller.save_orders(self.list_items, self.table_number, self.attendant, self.company_name, self.occupied_tables)
        self.controller.save_orders(self, self.occupied_tables)

        self.reset_page()

    def update_orders(self, event):
        # self.occupied_tables["ordered_list"] = json.dumps(self.list_items)

        # self.controller.save_orders(self.list_items, self.table_number, self.attendant, self.company_name, self.occupied_tables)
        self.controller.update_orders(json.dumps(self.list_items), self.table_number_value)

        self.reset_page()


    def add_items(self, qty, menu_focus, qty_focus, uom):

        menu_name = ''
        uom_name = ''

        for i in self.menu_price:
            if i[0] == self.menu_value:
                self.price = int(i[2])
                menu_name = i[1]
                uom_name = i[3]

        
        self.ordered_items["MENU"] = menu_name
        self.ordered_items["price"] = float(self.price)
        self.ordered_items["qty"] = qty
        self.ordered_items["total_price"] = self.price * int(qty)
        self.ordered_items["uom"] = uom_name

        # self.list_items.append(self.ordered_items)


        self.list_items.append(tuple(self.ordered_items.values()))

        # val = [self.table_number_value, self.attendant_value, self.company_value]
        
        self.save_orders_list.append([self.table_number_value, self.attendant_value, self.company_value, self.menu_value, qty])

        
        self.show_uom_items()
        # menu_focus.focus()
        self.clear_values(menu_focus, qty_focus, uom)


    def clear_values(self, menu, qty, uom):
        menu.delete(0, END)
        menu.set("PLEASE SELECT A MENU")
        menu.focus()
        qty.delete(0, END)
        uom.config(state="normal")
        uom.delete(0, END)
        uom.config(state="disabled")
        self.uom = None
        
    def get_table_number(self):
        self.controller.get_table_number(self)

    def get_attendant(self):
        self.controller.get_attendant(self)

    def get_company(self):
        self.controller.get_company(self)

    def get_menu(self):
        self.controller.get_menu(self)

    def check_occupied_table(self, table_id, attendant1, company1):
        self.controller.check_occupied_table(self, table_id)
        
        if len(self.occupied_tables) > 0:
            self.is_occupied = True
            for i in self.occupied_tables:
                self.list_items = i[4]
                self.attendant_value = i[2]
                self.company_value = i[3]

            attendant1.current(AMSGetIndex(self.attendant_ddl, self.attendant_value))
            attendant1.configure(state='disabled', foreground = 'blue')

            company1.current(AMSGetIndex(self.company_ddl, self.company_value))
            
            company1.configure(state='disabled', foreground = 'blue')

            self.action()
        else:
            self.is_occupied = False
            self.action()
            self.list_items = []

            attendant1.set('PLEASE SELECT AN ATTENDANT')
            attendant1.current(None)
            attendant1.configure(state='normal', foreground = 'black')

            company1.set('PLEASE SELECT A COMPANY')
            company1.current(None)
            company1.configure(state='normal', foreground = 'black')

        self.show_uom_items()
        self.occupied_tables = {}

    
    def reset_page(self):
        self.list_items = []
        self.is_occupied = False
        
        self.base_layout()
        self.show_uom_items()
        self.action()