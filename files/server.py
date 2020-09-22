import socket
import sqlite3

HOST = '127.0.0.1'
PORT = 33000
BUFFER = 1024
msg = 'Welcome on server!'

def establish_db():
    global conn
    conn = sqlite3.connect('xxxx.db')
    global c
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE tblTransactions(id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)')
    except:
        pass

def insert_into_db(data):
    for row in data:
        c.execute("INSERT INTO tblTransactions VALUES(NULL, '" + row + "')")
    conn.commit()

def terminate_db_connection():
    c.close()
    conn.close()

def render_transactions(transactions_str):
    transactions = []
    transactions = transactions_str.split(',')
    transaction_count = 1
    for transaction in transactions:
        print('Transaction ' + str(transaction_count) + ': ' + transaction + ' received.')
        transaction_count += 1
    return transactions

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # allowing clients to connect the server socket
    server_socket.bind((HOST,PORT))
    # setting queue of at most 2 client sockets
    server_socket.listen(2)

    while True:

        client_socket, address = server_socket.accept()

        date = client_socket.recv(BUFFER).decode('utf8')
        print(f'The connection from {address} has been established on {date}.')

        msg_to_client =  msg.encode('utf8')
        client_socket.send(msg_to_client)

        transactions_str = client_socket.recv(BUFFER).decode('utf8')
        transactions = render_transactions(transactions_str)

        # DB
        establish_db()
        insert_into_db(transactions)
        terminate_db_connection()

if __name__ == '__main__':
    main()
