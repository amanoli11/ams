from cProfile import label
import tkinter as tk
from tkinter import ttk
from custom_combo_box import CustomComboBox
import psycopg2

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self):

        # __init__ function for class Tk
        tk.Tk.__init__(self)


        self.geometry("1000x600")

        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("select uom_id, uom from uom where is_active = true")

        self.ddl = c.fetchall()

        conn.commit()
        conn.close()

        CustomComboBox(self, self.ddl, 'KG')

        # combobox = ttk.Combobox(self)
        # combobox.set('PLEASE SELECT A COMPANY')
        # combobox.grid(row=2, column=1, pady=5, padx=15, sticky=tk.E+tk.W)




#         # initializing frames to an empty array
#         self.frames = {}
#         print(self.frames)

#         # iterating through a tuple consisting
#         # of the different page layouts
#         for F in (StartPage, Page1, Page2):

#             frame = F(self)

#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame

#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(StartPage)

#     # to display the current frame passed as
#     # parameter

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

    
#     def menu(self):
#         ams_menu = tk.Menu(self)
#         self.config(menu=ams_menu)

#         file_menu = tk.Menu(ams_menu)
#         ams_menu.add_cascade(label="File", menu=file_menu)

#         file_menu.add_command(label="New File", command=lambda: self.show_frame(Page2))
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.quit)


#         menu = tk.Menu(ams_menu)
#         ams_menu.add_cascade(label="Menu", menu=menu)

#         menu.add_command(label="Create Menu")
#         menu.add_separator()
#         menu.add_command(label="Take Order")
# # first window frame startpage


# class StartPage(tk.Frame):
#     def __init__(self, container):
#         super().__init__(container)

#         # label of frame Layout 2
#         label = ttk.Label(self, text="Startpage", font=LARGEFONT)

#         # putting the grid in its place by using
#         # grid
#         label.grid(row=0, column=4, padx=10, pady=10)

#         button1 = ttk.Button(self, text="Page 1",
#                              command=lambda: container.show_frame(Page1))

#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 2 with text layout2
#         button2 = ttk.Button(self, text="Page 2",
#                              command=lambda: container.show_frame(Page2))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# # second window frame page1
# class Page1(tk.Frame):

#     def __init__(self, container):

#         super().__init__(container)
#         label = ttk.Label(self, text="Page 1", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="StartPage",
#                              command=lambda: container.show_frame(StartPage))

#         # putting the button in its place
#         # by using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text="Page 2",
#                              command=lambda: container.show_frame(Page2))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# # third window frame page2
# class Page2(tk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         label = ttk.Label(self, text="Page 2", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="Page 1",
#                              command=lambda: container.show_frame(Page1))

#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 3 with text
#         # layout3
#         button2 = ttk.Button(self, text="Startpage",
#                              command=lambda: container.show_frame(StartPage))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
# app.menu()
app.mainloop()
