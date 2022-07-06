import tkinter as tk
from tkinter import BOTH, BOTTOM, END, FIRST, LEFT, NW, RIGHT, TOP, Button, Canvas, Frame, Label, PhotoImage, StringVar, ttk
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

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from take_order import TakeOrder
from controller.take_order_controller import TakeOrderController
from model.take_order_model import TakeOrderModel


class Dashboard(ttk.Frame):

    def __init__(self, container):

        super().__init__(container)

        container.title("POS Dashboard")
        container.geometry('1300x600')
        container.width = 1300
        container.height = 600
        container.resizable(False, False)
        self.container = container


        self.title = Label(self, text='POS Dashboard', font="Verdana, 15")
        self.title.grid(row=0, column=0, sticky=tk.NE+tk.NW, columnspan=2)

        self.table_details = {}
        self.table_numbers = []


    def demo_scrollbar(self):

        # s = ttk.Style()
        # s.configure('TFrame', background='white')

        table_frame = tk.Frame(self,width=850,height=300, bg='white')

        canvas = Canvas(table_frame, bg='white')

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas,width=850,height=300, bg='white')

        scrollable_frame.bind(
           "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)


        button_dict={}

        column_number = 0
        row_number = 0

        vacant_photo = PhotoImage(file='views/ss1.png')

        occupied_photo = PhotoImage(file='views/ss2.png')

        photoimage_vacant = vacant_photo.subsample(3, 4)

        photoimage_occupied = occupied_photo.subsample(3, 4)

        for i in self.table_details:

            def func(x=i[2]):
                # self.container.show_frame(TakeOrderController, TakeOrderModel, TakeOrder)

                model = TakeOrderModel
                view = TakeOrder(self.container, x)
                view.grid(row=0, column=0, sticky="nsew")
                a = TakeOrderController(model, view)
                view.set_controller(a)
                view.tkraise()

            if i[1] == "NOT OCCUPIED":
                button_dict=ttk.Button(scrollable_frame, image=photoimage_vacant, text=i[0], command=func, compound=TOP)
                button_dict.image = photoimage_vacant
            else:
                button_dict=ttk.Button(scrollable_frame, image=photoimage_occupied, text=i[0], command=func, compound=TOP)
                button_dict.image = photoimage_occupied
            button_dict.grid(row=row_number, column=column_number, padx=10, pady=10)

            
            column_number+=1
            if column_number == 7:
                column_number = 0
                row_number+=1

        table_frame.grid(row=1, column=0, padx=10, pady=(10, 0))
        # table_frame.grid_propagate(0)
        table_frame.propagate(0)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


    def table_status(self):

        table_frame = tk.Frame(self,bg="white",width=850,height=300)
        table_frame.grid(row=1, column=0, padx=10, pady=(10, 0))

        table_frame.grid_propagate(0)
        table_frame.propagate(0)

        v = ttk.Scrollbar(table_frame)
  
        # attach Scrollbar to root window on
        # the side
        v.pack(side = RIGHT, fill = tk.Y)


        button_dict={}
        option= ["Python", "Java", "Go", "C++", "Python", "Java", "Go", "C++", "Python", "Java", "Go", "C++", "Python", "Java", "Go", "C++"]


        column_number = 0
        row_number = 0

        for i in option:

            def func(x=i):
                print(x)

            button_dict=ttk.Button(table_frame, text=i, command=func)
            button_dict.grid(row=row_number, column=column_number, padx=10, pady=10)

            
            column_number+=1
            if column_number == 2:
                column_number = 0
                row_number+=1

        # v.config(command=button_dict.yview)

    def table_pie_chart(self):

        # frame2 = tk.Frame(self,bg="white",width=400,height=480)
        # frame2.grid(row=1, column=1, padx=10, pady=(10, 0))

        frameChartsLT = tk.Frame(self, bg='white')
        frameChartsLT.grid(row=1, column=1 ,padx=10, pady=(10, 0))


        stockListExp = ['NOT-OCCUPIED' , 'OCCUPIED']
        stockSplitExp = [self.table_numbers[1], self.table_numbers[0]-self.table_numbers[1]]

        myexplode = [0, 0.2]

        fig = Figure(figsize=(5, 3.75), dpi=80) # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
            return my_autopct

        ax.pie(stockSplitExp, radius=1, autopct=make_autopct(stockSplitExp), shadow=True, explode = myexplode)
        ax.legend(stockListExp)

        chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
        chart1.get_tk_widget().grid(row=0, column=0)


    def set_controller(self, controller):
        self.controller = controller
        self.controller.initial_values(self)
        self.table_pie_chart()

        # self.table_status()

        self.demo_scrollbar()        
