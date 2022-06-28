import psycopg2
from datetime import datetime

class CreateUomModel():
    
    def save(uom_name, is_active, is_deleted):
        print("SAVE")
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("insert into uom (uom, is_active, is_deleted, created_date) values(%s, %s, %s, %s)",
                  (uom_name, is_active, is_deleted, datetime.now()))

        conn.commit()
        conn.close()

    def update(uom_name, is_active, is_deleted, uom_id):
        print("UPDATE")
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("update uom set uom = %s, is_active = %s, is_deleted = %s where id = %s",
                  (uom_name, is_active, is_deleted, uom_id))

        conn.commit()
        conn.close()

    def uom_list(parent):
        conn = psycopg2.connect(
            database="Demo", user="postgres", password="12345", host="localhost")
        c = conn.cursor()

        c.execute("select uom, is_active, is_deleted, id from uom order by id desc")
        result = c.fetchall()
        # output = [item for t in result for item in t]

        parent.uom_list = result

        conn.commit()
        conn.close()