import psycopg2

# class AMSDbConnector():
#     def __init__(self, query):

#         # self.parent = parent

#         self.query = query

#         # self.return_value = return_value


#         def run_query(self):
#             conn = psycopg2.connect(
#                 database="Demo", user="postgres", password="12345", host="localhost")
#             c = conn.cursor()

#             c.execute(self.query)

            
#             output = c.fetchall()


#             # setattr(self.parent, self.return_value, output)

#             conn.commit()
#             conn.close()

#             return run_query

def AMSDbConnector(query):
    conn = psycopg2.connect(
        database="Demo", user="postgres", password="12345", host="localhost")
    c = conn.cursor()

    c.execute(query)

    
    output = c.fetchall()


    # setattr(self.parent, self.return_value, output)

    conn.commit()
    conn.close()

    return output