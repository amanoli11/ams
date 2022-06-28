import tkinter as tk
from tkinter import END, StringVar, ttk
import psycopg2
# from controller.create_menu_controller import CreateMenuController

from create_uom import CreateUom
from model.create_uom_model import CreateUomModel
from controller.create_uom_controller import CreateUomController

from libraries.amsentrybox import AMSEntryBox
from libraries.amscombobox import AMSComboBox
from libraries.amstreeview import AMSTreeVIew
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

        self.is_active_value = None
        self.is_deleted_value = None

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


        global item_name
        item_name = AMSEntryBox(self, self.lf, 'item_name', placeholder="PLEASE INSERT AN ITEM NAME")
        # item_name.bind("<KeyRelease>", caps)
        item_name.focus()
        item_name.grid(row=1, column=1, pady=5, padx=15, ipadx=40)


        price_label = ttk.Label(self.lf, text="PRICE")
        price_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)


        global price
        price = ttk.Spinbox(self.lf, from_=0, to=9999999, wrap=False)
        price.set(0)
        price.grid(row=2, column=1, pady=5, padx=15, ipadx=30)

        global uom
        uom_label = ttk.Label(self.lf, text="UOM")
        uom_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)

        uom = AMSComboBox(self.lf, self, self.uom_ddl, 'uom_id', 'uom_index', placeholder="PLEASE CHOOSE AN UOM", filter=True)
        uom.grid(row=3, column=1, pady=5, padx=15, sticky=tk.E+tk.W)


        is_active_label = ttk.Label(self.lf, text="IS ACTIVE")
        is_active_label.grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
        
        is_active = AMSComboBox(self.lf, self, self.is_active, 'is_active', 'is_active_index', placeholder="IS ACTIVE")
        is_active.current(0)
        is_active.grid(row=4, column=1, pady=5, padx=15, sticky=tk.E+tk.W)

        is_deleted_label = ttk.Label(self.lf, text="IS DELETED")
        is_deleted_label.grid(row=5, column=0, sticky=tk.W, pady=5, padx=5)

        is_deleted = AMSComboBox(self.lf, self, self.is_active, 'is_deleted', 'is_deleted_index', placeholder="IS DELETED")
        is_deleted.current(1)
        is_deleted.grid(row=5, column=1, pady=5, padx=15, sticky=tk.E+tk.W)

        clear_btn = ttk.Button(self.lf, text="CLEAR", command=lambda: self.clear_values(
            item_name,
            price,
            uom))

        clear_btn.bind('<Return>', lambda event: self.clear_values(item_name,
                                                                price,
                                                                uom))

        clear_btn.grid(row=6, column=0, sticky=tk.E)


        global submit_btn
        submit_btn = ttk.Button(self.lf, text="SAVE MENU", command=lambda: self.submit_menu(item_name.get(),
                                                                                       price.get(),
                                                                                       uom.get(),
                                                                                       self.uom_id,
                                                                                       item_name,
                                                                                       price,
                                                                                       uom))
        submit_btn.bind('<Return>', lambda event: self.submit_menu(item_name.get(),
                                                                   price.get(),
                                                                   uom.get(),
                                                                   self.uom_id,
                                                                   item_name,
                                                                   price,
                                                                   uom))

        submit_btn.grid(row=6, column=1, sticky=tk.E, pady=8, padx=13)

        # label1 = ttk.Label(self, text="ACTIONS", font="Verdana, 15")
        # label1.grid(column=0, row=1, sticky=tk.W, padx=10)

        action_label_frame = ttk.LabelFrame(self, text='Actions')
        action_label_frame.grid(column=0, row=1, padx=10, pady=10)

        create_uom_btn = ttk.Button(action_label_frame, text="CREATE UOM", command=lambda: self.container.show_frame(CreateUomController, CreateUomModel, CreateUom))
        create_uom_btn.grid(column=0, row=0, padx=13, pady=10)

        take_order_btn = ttk.Button(action_label_frame, text="TAKE ORDER")
        take_order_btn.grid(column=1, row=0, padx=13, pady=10)

    # def update_menu_items(self):
    #     label = ttk.Label(self, text="Create Menu", font="Verdana, 15")
    #     label.grid(column=0, row=0, sticky=tk.W, padx=10)

    #     self.lf = ttk.LabelFrame(self, text='Create Menu')
    #     self.lf.grid(column=0, row=1, padx=10, pady=10, sticky=tk.NW)

    #     # style = ttk.Style()
    #     # style.theme_use('clam')
    #     # style.configure("TLabelframe", bordercolor="green")

    #     item_name_label = ttk.Label(self.lf, text="ITEM NAME")
    #     item_name_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)

    #     def caps(event):
    #         v.set(v.get().upper())

    #     v = StringVar()

    #     item_name = ttk.Entry(self.lf, width=30, textvariable=v)
    #     item_name.insert(END, self.item_name1)
    #     item_name.bind("<KeyRelease>", caps)
    #     item_name.grid(row=1, column=1, pady=5, padx=15)

    #     price_label = ttk.Label(self.lf, text="PRICE")
    #     price_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

    #     price = ttk.Entry(self.lf, width=30)
    #     price.insert(END, self.price)
    #     price.grid(row=2, column=1, pady=5, padx=15)

    #     uom_label = ttk.Label(self.lf, text="UOM")
    #     uom_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)

    #     def callback(*args):
    #         numberr = [row[0] for row in self.uom_list
    #                    if row[1] == variable.get()
    #                    ]

    #         if len(numberr) > 0:
    #             s = [str(integer) for integer in numberr]
    #             a_string = "".join(s)

    #             res = int(a_string)

    #             self.uom = res

    #     variable = StringVar()
    #     uom = ttk.Combobox(self.lf, value=self.uom_values, textvariable=variable)
    #     uom.bind('<<ComboboxSelected>>', callback)
    #     uom.set('PLEASE SELECT A UOM')
    #     if(self.uom > 0):
    #         uom.current(self.uom - 1)
            
    #     uom.grid(row=3, column=1, pady=5, padx=15, sticky=tk.E+tk.W)

    #     # clear_btn = ttk.Button(self.lf, text="CLEAR", command=lambda: self.clear_values(
    #     #                                                                         item_name.delete(0, END),
    #     #                                                                         price.delete(0, END),
    #     #                                                                         uom.delete(0, END)))

    #     clear_btn = ttk.Button(self.lf, text="CLEAR", command=lambda: self.clear_values(item_name,
    #                                                                             price,
    #                                                                             uom))

    #     clear_btn.bind('<Return>', lambda event: self.clear_values(item_name,
    #                                                             price,
    #                                                             uom))

    #     clear_btn.grid(row=4, column=0, sticky=tk.E)

    #     submit_btn = ttk.Button(self.lf, text="UPDATE MENU", command=lambda: self.submit_updated_menu(self.item_id,
    #                                                                                              item_name.get(),
    #                                                                                              price.get(),
    #                                                                                              uom.get(),
    #                                                                                              self.uom,
    #                                                                                              item_name,
    #                                                                                              price,
    #                                                                                              uom))

    #     submit_btn.bind('<Return>', lambda event: self.submit_updated_menu(self.item_id,
    #                                                                 item_name.get(),
    #                                                                 price.get(),
    #                                                                 uom.get(),
    #                                                                 self.uom,
    #                                                                 item_name,
    #                                                                 price,
    #                                                                 uom))

    #     submit_btn.grid(row=4, column=1, sticky=tk.E, pady=8, padx=13)


    def update_menu_items(self, menu_name, item_price, item_uom, item_is_active, item_is_deleted, item_uom_id):

        item_name.delete(0, END)
        item_name.insert(0, menu_name)

        price.set(item_price)

        uom.current(AMSGetIndex(self.uom_ddl, item_uom_id))

        submit_btn.grid_forget()

        update_btn = ttk.Button(self.lf, text="UPDATE MENU", command=lambda: self.submit_updated_menu(self.item_id,
                                                                                                 item_name.get(),
                                                                                                 price.get(),
                                                                                                 uom.get(),
                                                                                                 self.uom,
                                                                                                 item_name,
                                                                                                 price,
                                                                                                 uom))

        update_btn.bind('<Return>', lambda event: self.submit_updated_menu(self.item_id,
                                                                    item_name.get(),
                                                                    price.get(),
                                                                    uom.get(),
                                                                    self.uom,
                                                                    item_name,
                                                                    price,
                                                                    uom))

        update_btn.grid(row=6, column=1, sticky=tk.E, pady=8, padx=13)



    def show_menu_items(self):
        
        columns = ("MENU NAME", "PRICE", "UOM", "IS ACTIVE", "IS DELETED")
        frame, tree, option = AMSTreeVIew(self, columns, self.output, frame_name="MENU ITEMS", table_height=20)
        
        # tree = ttk.Treeview(self, columns=columns, show='headings', height=25)
        # tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=320)
        # tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=100)
        # tree.column("# 3", anchor=tk.W, stretch=tk.NO, width=115)
        # tree.column("# 4", anchor=tk.W, stretch=tk.NO, width=80)
        # tree.heading('MENU NAME', text='MENU NAME')
        # tree.heading('PRICE', text='PRICE')
        # tree.heading('UOM', text='UOM')
        # tree.heading('IS ACTIVE', text='IS ACTIVE')

        
        # for i in self.output:
        #     tree.insert('', tk.END, values=i)


        tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=320)
        tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=100)
        tree.column("# 3", anchor=tk.W, stretch=tk.NO, width=115)
        tree.column("# 4", anchor=tk.W, stretch=tk.NO, width=85)
        tree.column("# 5", anchor=tk.W, stretch=tk.NO, width=95)

        def item_selected(event):

            x = tree.selection()
            y = tree.item(x)['values']
            # self.item_id = y[5]
            # self.item_name1 = y[0]
            # self.price = y[1]
            # self.uom = y[2]
            self.update_menu_items(y[0], y[1], y[2], y[3], y[4], y[5])


            # for selected_item in tree.selection():
            #     item = tree.item(selected_item)
            #     record = item['values']

            #     self.item_name = record[0]

        tree.bind('<<TreeviewSelect>>', item_selected)

        frame.grid(row=1, column=1, sticky=tk.NE, padx=(30, 0))

        scrollbar = ttk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar.set)
        scrollbar.grid(row=3, column=1, sticky='ew')

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

    def clear_values(self, item_name, price, uom):
        item_name.delete(0, END)
        price.delete(0, END)
        uom.delete(0, END)
        uom.set("PLEASE SELECT A UOM")
        item_name.focus()

    def submit_menu(self, item_name, price, uom, uom_id, item_del, price_del, uom_del):
        self.controller.save(item_name, price, uom, uom_id)
        self.clear_values(item_del, price_del, uom_del)

        self.controller.lister(self)
        self.show_menu_items()

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
