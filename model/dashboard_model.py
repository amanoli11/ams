import psycopg2
from datetime import datetime

from libraries.amsdbconnector import AMSDbConnector

class DashboardModel():
    
    def initial_values(parent):
        
        query_for_table_status = "select tm.table_number, coalesce(ot.id::varchar, 'NOT OCCUPIED') as table_status, tm.id from table_management tm  left join occupied_table ot on tm.id = ot.table_id order by tm.id asc"

        query_for_vacant_table = '''select count (*) from (select coalesce(ot.id::varchar, 'NOT OCCUPIED') as table_status from table_management tm
        left join occupied_table ot on tm.id = ot.table_id)x
        where x.table_status = 'NOT OCCUPIED' '''

        query_for_total_table = "select count(*) from table_management"


        values_for_table_status = AMSDbConnector(query_for_table_status)

        values_for_vacant_table = AMSDbConnector(query_for_vacant_table)

        values_for_total_table = AMSDbConnector(query_for_total_table)


        parent.table_numbers = [sum(values_for_total_table[0]), sum(values_for_vacant_table[0])]

        parent.table_details = values_for_table_status