import socket
from uuid import uuid4
from datetime import datetime

HOST = '127.0.0.1'
PORT = 33000
BUFFER = 1024
now = datetime.now()

transactions = []

def generate_transactions():
    for _ in range(1,11):
        t = uuid4()
        transactions.append(str(t))

def main():

    generate_transactions()

    # connecting to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST,PORT))

    # client informs server about connection try
    client_socket.send(str(now.strftime("%Y-%m-%d %H:%M:%S")).encode('utf8'))

    # server inform client about successful connection
    msg_from_server = client_socket.recv(BUFFER).decode('utf8')
    print(msg_from_server)

    # client sents data to server
    transaction_str = ','.join(transactions)
    client_socket.send(transaction_str.encode('utf8'))
    print('Data sent to server')


if __name__ == '__main__':
    main()
