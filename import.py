import psycopg2
import psycopg2.extras
import index
import math
class Import:
    def __init__(self, hostName,userName,passwd,db,dbPort=5439):
        self.con = psycopg2.connect(
            dbname= db, 
            host= hostName, 
            port= dbPort, 
            user= userName, 
            password= passwd
        )
        self.cur = self.con.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    def select(self, query):    
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def closeConn(self):
        self.cur.close()
        self.con.close()
    
    def importRecords(self,table,columns,limit=10000):
        query = "select " +  str(columns) +" from "+table

        self.cur.execute("select count(*) as total from "+table)
        result = self.cur.fetchone()
        if int(result['total'])>limit:
            total = round(result['total'] / limit)
        else:
            total = 1
            limit = result['total']

        # self.cur.close()
        for x in range(total):
            if x == 0:
                query+= " limit "+str(limit)
            else:
                query+= " limit "+str(x*limit)
            print(query)
            result = self.select(query)
            print(result)
        self.con.close()
