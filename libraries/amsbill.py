import tkinter as tk
from tkinter import Frame, StringVar, Toplevel, ttk
from datetime import datetime
from tkinter import messagebox
import pandas as pd
import webbrowser
from threading import Thread
import time

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys

class AMSBill():
    def __init__(self, item_details, tree_list, user_name, company_name, table_number, total_price, tno=None, controller=None, parent=None, save_order=None):
        # __init__ function for class Tk
        # tk.Tk.__init__(self)

        # self.withdraw()
        top = Toplevel()
        top.geometry('670x635')
        top.title("BILL")
        self.top = top

        self.items = [['BUFF MOMO', 130.0, '1', 130], ['ICE CREAM', 60.0, '1', 60], ['ICE CREAM', 60.0, '1', 60], ['PORK SEKWA', 800.0, '1', 800]]
        self.data = {'Name':['Tom', 'nick', 'krish', 'jack'],'Age':[20, 21, 19, 18]}

        self.width = 670
        self.height = 635

        self.item_details = item_details
        self.list_items = tree_list
        self.user_name = user_name
        self.table_number = table_number

        self.tno = tno
        self.controller = controller
        self.parent = parent
        self.save_orders = save_order

        self.company_name = company_name
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.pan_number = 123456789
        self.discount_amount = 0
        self.total_amount = total_price
        self.payable_amount = total_price
        self.discount_percentage = 0

        # self.header = Frame(self)
        self.left_frame = Frame(self.top, bg='red', width=self.width/2)
        self.right_frame = Frame(self.top, bg='blue', width=self.width/2)

        self.checkout_btn = ttk.Button(self.top, text="CHECKOUT", underline=5, command=lambda: self.print_file_thread(event=None))
        self.top.bind('<Alt-o>', self.print_file_thread)

        self.base_layout()

    def base_layout(self):

        restraunt_name = ttk.Label(self.top, text="***AMS Restro, Sukedhara***", font="Verdana, 15")
        restraunt_name.grid(row=0, column=0, columnspan=2, pady=20)

        date_now = ttk.Label(self.top, text=f"Date: {self.datetime}", font="Verdana, 10")
        date_now.grid(row=1, column=1, sticky=tk.NE, padx=15)

        table = ttk.Label(self.top, text=f"Table Number: {self.table_number}", font="Verdana, 10")
        table.grid(row=2, column=0, sticky=tk.NW, padx=(15, 0))

        company_name = ttk.Label(self.top, text=f"Company Name: {self.company_name}", font="Verdana, 10", width=40)
        company_name.grid(row=1, column=0, sticky=tk.NW, padx=(15, 0))

        user = ttk.Label(self.top, text=f"User: {self.user_name}", font="Verdana, 10")
        user.grid(row=2, column=1, sticky=tk.NE, padx=15)

        # pan = ttk.Label(self.right_frame, text="Date: ", font="Verdana")
        # pan.grid(row=1, column=1)

        restraunt_name = ttk.Label(self.top, text="******************************************************************************************")
        restraunt_name.grid(row=3, column=0, columnspan=2, pady=(15,5))

        columns = ("ITEM NAME", "PRICE", "QTY", "UOM", "TOTAL PRICE")
        tree = ttk.Treeview(self.top, columns=columns, show='headings', height=19)
        tree.grid(row=4, column=0, columnspan=2)

        tree.heading('ITEM NAME', text='ITEM NAME')
        tree.heading('PRICE', text='PRICE')
        tree.heading('QTY', text='QTY')
        tree.heading('UOM', text='UOM')
        tree.heading('TOTAL PRICE', text='TOTAL PRICE')

        tree.column("# 1", anchor=tk.W, stretch=tk.NO, width=280)
        tree.column("# 2", anchor=tk.E, stretch=tk.NO, width=80)
        tree.column("# 3", anchor=tk.E, stretch=tk.NO, width=50)
        tree.column("# 4", anchor=tk.E, stretch=tk.NO, width=100)
        tree.column("# 5", anchor=tk.E, stretch=tk.NO, width=120)

        # self.total_price = 0
        for i in self.list_items:
            tree.insert('', tk.END, values=i)
            # self.total_price = self.total_price + i[4]

        total_amount = ttk.Label(self.top, text=f"TOTAL AMOUNT: {self.total_amount}")
        total_amount.grid(row=5, column=0, sticky=tk.NW, pady=(20,0), padx=(20, 0))


        discount_label = ttk.Label(self.top, text="DISCOUNT PERCENTAGE: ")
        discount_label.grid(row=6, column=0, sticky=tk.NW, pady=(5,0), padx=(20, 0))

        def asd(e):
            discount_value = var_1.get()

            if discount_value == '':
                self.discount_percentage = 0
            else:
                self.discount_percentage = float(discount_value)

                self.payable_amount = self.total_amount - self.discount_percentage*self.total_amount/100

                self.discount_amount = self.total_amount - self.payable_amount

                payable_amount.config(text=f"PAYABLE AMOUNT: {self.payable_amount}")

        var_1 = StringVar()
        discount_percentage = ttk.Entry(self.top, width=10, textvariable=var_1)
        discount_percentage.bind('<KeyRelease>', asd)
        discount_percentage.focus()
        discount_percentage.grid(row=6, column=0, sticky=tk.NE, pady=(5,0), padx=(0, 60))

        # def caps(event):
        #     v.set(v.get().upper())
        #     print(v.get())

        # v = StringVar()

        # discount_percentage = ttk.Entry(self.top, width=30, textvariable=v)
        # discount_percentage.bind("<KeyRelease>", caps)
        # discount_percentage.focus()
        # discount_percentage.grid(row=6, column=0, sticky=tk.NE, pady=(5,0), padx=(0, 60))

        payable_amount = ttk.Label(self.top, text=f"PAYABLE AMOUNT: {self.payable_amount}")
        payable_amount.grid(row=5, column=1, sticky=tk.NE, pady=(20,0), padx=(0, 20))

        
        
        self.checkout_btn.grid(row=6, column=1, sticky=tk.NE, pady=(5,0), padx=(0, 20))

        # self.top.bind('<Alt-o>', self.print_file_thread)


        # heading = tk.Label(self,text='SN\tITEM NAME\tPRICE\tUOM\tQTY\tTOTAL PRICE')
        # heading.grid(row=5, column=0, columnspan=2, pady=(15,5))

        # item1 = tk.Label(self,text=f'{1}\t{"BUFF MOMO"}\t{130}\t{"PLATE"}\t{2}\t{260}')
        # item1.grid(row=6, column=0, columnspan=2, pady=(15,5))

        self.left_frame.grid(row=0, column=0)
        self.right_frame.grid(row=0, column=1)



    def print_file(self):

        df = pd.DataFrame(self.item_details)
        
        restro = "***AMS Restro, Sukedhara***\n\n\n"

        company = f"Company Name: {self.company_name}\n"

        datetime_now = f"Date&Time: {self.datetime}\n"

        pan = f"Pan Number: {self.pan_number}\n"

        table = f"Table Number: {self.table_number}\n"

        dotted_line = "-------------------------------------------------\n\n"

        total_amount = self.total_amount
        total = f"Total Amount: {total_amount}\n"

        discount = f"Discounted Amount: {self.discount_amount}\n"

        payable = f"Payable Amount: {self.payable_amount}\n"

        # webbrowser.get('C:\Program Files\Google\Chrome\Application\chrome.exe')
        # webbrowser.get('google-chrome')
        chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        
        txtfile = open('Bill', 'w')
        txtfile.write(restro+datetime_now+company+pan+table+dotted_line+str(df)+'\n\n'+dotted_line+total+discount+payable)
        txtfile.close()
        webbrowser.get('chrome').open_new_tab('E:/Development/ams/Bill')
        # webbrowser.open_new_tab('Bill')
        messagebox.showinfo("Txt Export", "Export Completed")
        self.top.destroy()

    def update_payable(self, discount_value):
        print(discount_value)
        # if discount_value == '':
        #     self.discount_percentage = 0
        # else:
        #     self.discount_percentage = float(discount_value)

        # self.payable_amount = self.total_amount - self.discount_percentage*self.total_amount/100

        # payable.config(text=f"PAYABLE AMOUNT: {self.payable_amount}")

        # print(self.total_amount)

        # print(self.discount_percentage)


    def print_file_thread(self, event):

        self.checkout_btn.config(text = "LOADING", state='disabled', underline=False)
        self.checkout_btn.update_idletasks()

        self.print_file()

        self.parent.reset_page()

        self.controller.delete_occupied_table(self.tno)

        print(self.item_details)

        print(self.list_items)

        self.controller.save_orders_list(self.save_orders)

        # new_thread = Thread(target=self.print_file())
        # new_thread.start()
        # self.monitor(new_thread, btn)

    def monitor(self, thread, btn):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread, btn))
        else:
            thread.join()
            # btn.config(text = "CHECKOUT", state='normal')
            # btn.update_idletasks()

# app = AMSBill()
# app.mainloop()