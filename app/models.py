import pymysql
import os


def connect():
    rds_host = os.environ['DATABASE_HOST']
    db_user = os.environ['DATABASE_USER']
    password = os.environ['DATABASE_PASSWORD']
    db_name = os.environ['DATABASE_DB_NAME']
    port = 3306

    #server_address = (rds_host, port)
    conn = pymysql.connect(rds_host, user=db_user, passwd=password, db=db_name, connect_timeout=10000, port=port, charset='utf8mb4')
    return conn

class Product:
    def __init__(self, product_name=None, db=connect()):
        self.product_name = product_name
        self.cursor = db.cursor(pymysql.cursors.DictCursor)
        self.db = db
        print("cursor connection done!!!")
        
    
    def return_items(self):
        products = None
        cur = self.cursor
        cur.execute(f"SELECT * FROM {self.product_name}")
        products = cur.fetchall()
        self.db.commit()
        print("select specfic product done!!!!")
        return products

    def show_all_items(self):
        results = None
        cur = self.cursor
        sql = """
        SELECT id,name,price, description,img_url FROM apparels
        UNION
        SELECT id,name,price, description,img_url FROM fashion
        UNION
        SELECT id,name, price, description,img_url FROM bicycles
        UNION 
        SELECT id,name, price, description,img_url FROM jewelry
        ORDER BY name
        """
        cur.execute(sql)
        results = cur.fetchall()
        self.db.commit()
        print("select all done!!!!")
        return results

class User:
    def __init__(self, db=connect()):
        self.cursor = db.cursor()
        self.db = db

    def add(self, fname, lname, email, password):
        sql = f"INSERT INTO User(fname, lname, email, password) VALUES(?,?,?,?)"
        data=(fname, lname, email, password)
        cur = self.cursor
        cur.execute(sql, data)
        self.db.commit()
        

    def verify(self, email ,password):
        sql = f"SELECT email , password FROM User WHERE email='{email}' AND password='{password}'"
        cur = self.cursor
        cur.execute(sql)
        result = cur.fetchall()
        self.db.commit()
        row_count =  len(result)
        print(row_count)
        if row_count == 1 :
            return True
        else:
            return False

class Review:
    def __init__(self):
        pass

    def __repr__(self):
        pass
