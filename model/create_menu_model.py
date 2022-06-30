import psycopg2
from datetime import datetime

from libraries.amsdbconnector import AMSDbConnector

class CreateMenuModel():
    # conn = psycopg2.connect(database="Demo", user="postgres",
    #                         password="12345", host="localhost")
    # c = conn.cursor()

    # # Create table
    # c.execute("""
    # DROP TABLE IF EXISTS MENU;

    # CREATE TABLE MENU(
    #     MENU_ID serial PRIMARY KEY,
    #     ITEM_NAME text,
    #     PRICE decimal,
    #     UOM text,
    #     IS_ACTIVE boolean,
    #     IS_DELETED boolean,
    #     CREATED_DATE timestamp
    # )
    # """)

    # # Commit changes
    # conn.commit()

    # # Close connection
    # conn.close()

    def __init__(self):
        self.list = {}
        print("model.py")
    
    def save(item_name, price, uom, uom_id, is_active, is_deleted):
        print("SAVE")
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("insert into menu (item_name, price, uom_id, is_active, is_deleted, created_date) values(%s, %s, %s, %s, %s, %s)",
                  (item_name, price, uom_id, is_active, is_deleted, datetime.now()))

        conn.commit()
        conn.close()

    def update_menu_item(menu_id, item_name, price, uom_id, is_active, is_deleted):
        print("UPDATE")
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("update menu set item_name = %s, price = %s, uom_id = %s, is_active = %s, is_deleted = %s, created_date = %s where id = %s",
        (item_name, price, uom_id, is_active, is_deleted, datetime.now(), menu_id))

        conn.commit()
        conn.close()

    def lister(parent):
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("""select item_name, price, uom, menu.is_active, menu.is_deleted, uom_id, menu.id
                    from menu left join uom on menu.uom_id = uom.id
                    order by menu.id desc""")
        result = c.fetchall()
        # output = [item for t in result for item in t]

        parent.output = result

        conn.commit()
        conn.close()

    
    def collect_initial_values(parent):
        query = "SELECT ID, UOM FROM UOM"
        initial_values = AMSDbConnector(query)

        parent.uom_ddl = initial_values