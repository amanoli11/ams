import psycopg2
from datetime import datetime
from views.create_menu import CreateMenu


class CreateMenuController():

    # def __init__(self, container, item_name, price, uom):
    #     conn = psycopg2.connect(database="Demo", user="postgres", password="12345", host="localhost")
    #     c = conn.cursor()

    #     c.execute("insert into menu (item_name, price, uom, is_active, is_deleted, created_date) values(%s, %s, %s, %s, %s, %s)", (item_name, price, uom, True, False, datetime.now()))

    #     conn.commit()
    #     conn.close()

    def __init__(self, model, view):
        # self.a = CreateMenu(root)
        # self.a.grid(row=0, column=0, sticky="nsew")
        # self.a.tkraise()
        self.model = model
        self.view = view

    def save(self, item_name, price, uom, uom_id, is_active, is_deleted):
        self.model.save(item_name, price, uom, uom_id, is_active, is_deleted)

    def update_menu_item(self, menu_id, item_name, price, uom_id, is_active, is_deleted):
        self.model.update_menu_item(menu_id, item_name, price, uom_id, is_active, is_deleted)

    def lister(self, parent):
        self.model.lister(parent)

    def collect_initial_values(self, parent):
        self.model.collect_initial_values(parent)