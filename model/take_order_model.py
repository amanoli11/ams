import json
import psycopg2
from datetime import datetime
from libraries.amsdbconnector import AMSDbConnector

class TakeOrderModel():

    def get_table_number(parent):

        table_number = "select id, table_number from table_management where is_active = true"
        parent.table_number_ddl = AMSDbConnector(table_number)


    def get_attendant(parent):

        attendant = "select id, attendant_name from attendant where is_active = true"
        parent.attendant_ddl = AMSDbConnector(attendant)


    def get_company(parent):

        company = "select id, company_name from company where is_active = true"

        parent.company_ddl = AMSDbConnector(company)


    def get_menu(parent):
        
        menu = "select id, item_name from menu where is_active = true"
        
        parent.menu = AMSDbConnector(menu)

        
        menu_price = "select menu.id, item_name, price, uom.uom from menu left join uom on uom.id = menu.uom_id where menu.is_active = true"
        
        parent.menu_price = AMSDbConnector(menu_price)


    def save_orders(parent, occupied_table):
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("insert into occupied_table (table_id, attendant_id, company_id, ordered_list, created_date) values(%s, %s, %s, %s, %s)",
                    (occupied_table["table_id"], occupied_table["attendant_id"], occupied_table["company_id"], occupied_table["ordered_list"], datetime.now()))

        print('save')

        conn.commit()
        conn.close()

        parent.occupied_tables = {}

    
    def update_orders(json_value, table_id):
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        # c.execute("update occupied_table set ordered_list = %s, created_date = %s where table_id = %s)",(json_value, datetime.now(), table_id))
        sql = """ UPDATE occupied_table
                SET ordered_list = %s,
                created_date = %s
                WHERE table_id = %s"""

        c.execute(sql, (json_value, datetime.now(), table_id))

        conn.commit()
        conn.close()

    def delete_occupied_table(table_number):
        
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()
        
        c.execute("DELETE FROM OCCUPIED_TABLE WHERE TABLE_ID = %s",(table_number,))

        conn.commit()
        conn.close()

    def check_occupied_table(parent, table_number):

        check_occupied_table = "select * from occupied_table where table_id = '{0}'".format(table_number)

        parent.occupied_tables = AMSDbConnector(check_occupied_table)



    def save_orders_list(orders_list):
        for i in orders_list:
            conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
            c = conn.cursor()
        
            c.execute("insert into orders (item_id, qty, table_id, attendant_id, company_id, is_active, is_deleted, created_date) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                    (i[3], i[4], i[0], i[1], i[2] ,True, False, datetime.now()))

            conn.commit()
            conn.close()