import tkinter as tk
from tkinter import ttk
from create_menu import CreateMenu
from model.create_menu_model import CreateMenuModel
# from take_order import TakeOrder
from controller.create_menu_controller import CreateMenuController

from create_uom import CreateUom
from model.create_uom_model import CreateUomModel
from controller.create_uom_controller import CreateUomController

from take_order import TakeOrder
from model.take_order_model import TakeOrderModel
from controller.take_order_controller import TakeOrderController

class Homepage(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self):
        # __init__ function for class Tk
        tk.Tk.__init__(self)
        self.width = 1000
        self.height = 600

        self.title("AMS")
        # self.geometry("1000x600")

        # initializing frames to an empty array
        # self.frames = {}

        # classes_list = [TakeOrder,
        #                 CreateMenu]

        # iterating through a tuple consisting
        # of the different page layouts
        # for F in (classes_list):

        #     frame = F(self)

        #     # initializing frame of that object from
        #     # startpage, page1, page2 respectively with
        #     # for loop
        #     self.frames[F] = frame

        #     frame.grid(row=0, column=0, sticky="nsew")
        self.bind('<Control-n>', self.open_new_window)
        self.bind('<Control-q>', self.quit_app)
        # self.show_frame(TakeOrderController, TakeOrderModel, TakeOrder)
        # self.show_frame(CreateUomController, CreateUomModel, CreateUom)
        self.show_frame(CreateMenuController, CreateMenuModel, CreateMenu)

    # to display the current frame passed as
    # parameter

    def quit_app(self,event):
       self.quit()

    def show_frame(self, cont, model, view):
        # frame = self.frames[cont]
        model = model #CreateMenuModel
        view = view(self) #CreateMenu(self)
        view.grid(row=0, column=0, sticky="nsew")
        a = cont(model, view)
        view.set_controller(a)
        # self.display = a
        view.tkraise()

    def window_placement(self):
        width_of_window = self.width
        height_of_window = self.height

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = (screen_width/2) - (width_of_window/2)
        y_coordinate = (screen_height/3) - (height_of_window/3)

        self.geometry("%dx%d+%d+%d" % (width_of_window,
                      height_of_window, x_coordinate, y_coordinate))

    def open_new_window(self, event):
        app = Homepage()
        app.menu()
        app.mainloop()

    def menu(self):
        ams_menu = tk.Menu(self)
        self.config(menu=ams_menu)

        file_menu = tk.Menu(ams_menu, tearoff="off")
        ams_menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New File", command=lambda: self.open_new_window(event=None))
        file_menu.bind('<Control-n>', self.open_new_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=lambda: self.quit_app(event=None))

        menu = tk.Menu(ams_menu, tearoff="off")
        ams_menu.add_cascade(label="Menu", menu=menu)

        menu.add_command(label="Create Menu",
                         command=lambda: self.show_frame(CreateMenuController, CreateMenuModel, CreateMenu))
        menu.add_separator()
        menu.add_command(label="Create UOM", command=lambda: self.show_frame(CreateUomController, CreateUomModel, CreateUom))
        menu.add_separator()
        menu.add_command(label="Take Order", command=lambda: self.show_frame(TakeOrderController, TakeOrderModel, TakeOrder))


app = Homepage()
app.menu()
app.window_placement()
app.mainloop()
