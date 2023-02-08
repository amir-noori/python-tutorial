
import psycopg2

class User:
    def __init__(self, username = None, account = None):
        self.username = username
        self.account = account


class Account:

    def __init__(self, account_id = None, account_name = None):
        self.account_id = account_id
        self.account_name = account_name

    def __str__(self):
        return f"{self.account_id} - {self.account_name}"


def get_connection():
    # Connect to your postgres DB
    conn = psycopg2.connect(database="testdb", user = "postgres", password = "123456", host = "127.0.0.1", port = "5432")
    return conn

def query(conn, sql):   
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute(sql)
    # Retrieve query results
    records = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    return records, colnames

def insert(conn, sql, data):   
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute(sql, data)
    conn.commit()



def process_accounts(accounts):
    pass




# insert_sql = "insert into tbl_account (account_id, account_name) values (%s, %s)"
# insert(get_connection(), insert_sql, (2, "test2"))

records, colnames = query(get_connection(), "SELECT account_id, account_name FROM tbl_account")

acounts = []
for record in records:
    account = Account()
    i = 0
    for colname in colnames:
        if i == 0:
            account.account_id = record[i]
        else:
            account.account_name = record[i]
        # print(f" {colname} -> {record[i]}")
        i += 1
    acounts.append(account)

for a in acounts:
    print(a)






