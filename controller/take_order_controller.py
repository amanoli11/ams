class TakeOrderController():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_table_number(self, parent):
        self.model.get_table_number(parent)

    def get_attendant(self, parent):
        self.model.get_attendant(parent)

    def get_company(self, parent):
        self.model.get_company(parent)

    def get_menu(self, parent):
        self.model.get_menu(parent)

    # def save_orders(self, values, table, attendant, company):
    #     self.model.save_orders(values, table, attendant, company)

    def save_orders(self, parent, occupied_tables):
        self.model.save_orders(parent, occupied_tables)

    def update_orders(self, json_value, table_id):
        self.model.update_orders(json_value, table_id)

    def check_occupied_table(self, parent, table_id):
        self.model.check_occupied_table(parent, table_id)

    def delete_occupied_table(self, table_number):
        self.model.delete_occupied_table(table_number)

    def save_orders_list(self, orders_list):
        self.model.save_orders_list(orders_list)
