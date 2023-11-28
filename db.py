import pyodbc

# Define the connection string
connection_string = 'Driver={SQL Server};Server=PRATHAM;Database=Stock;Trusted_Connection=yes;'

# Establish a connection
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

def verify(n,m,e):
    cursor.execute('select * from users where email=? and name=? and mob=?',(e,n,m))
    d=cursor.fetchall()
    if d:
        return True
    else:
        return False


def createaccount(r,p,m,e):
    global cursor
    cursor.execute('insert into users(name,pass,mob,email) values(?,?,?,?)',(r,p,m,e))
    cursor.execute('select userid from users where email=?',(e,))
    d = cursor.fetchall()
    t= f't{d[0][0]}'

    cursor.execute(f"create table {t}(stockid int identity(1,1) primary key,stock_name varchar(255), amt int, quantity int, d_ate date)")
    cursor.commit()
    return t

def changepass(e,n,p):
    cursor.execute('update users set pass=? where email=? and name=?',(p,e,n))
    cursor.commit()
def add(num,s,qu,p):
    cursor.execute(f'insert into t{num} values(?,?,?,getdate())',(s,p,qu))
    cursor.commit()

def isUser(n,p):
    cursor.execute("select * from users where email=? and pass=?",(n,p))
    r = cursor.fetchall()
    if r:
        return r[0][0]
    else:
        return False

def up(num, s, qu, p):
    cursor.execute(f"update t{num} set quantity=?,amt=? where stock_name=?",(qu,p,s))
    cursor.commit()

def get(num):
    query = f'select * from t{num}'
    cursor.execute(query)
    r=cursor.fetchall()
    return list(r[0])


def gets(num):
    query = f'select stock_name,stockid,amt,quantity from t{num}'
    cursor.execute(query)
    r=cursor.fetchall()
    return r

def dele(num,s):
    cursor.execute(f"delete from t{num} where stock_name=?",(s,))
    cursor.commit()
