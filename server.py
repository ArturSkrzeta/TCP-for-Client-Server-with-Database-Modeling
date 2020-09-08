import socket

HOST = '57.20.206.19'
PORT = 33000
BUFFER = 1024
msg = 'Welcome on server!'
transactions = []

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
    transaction_list = transactions_str.split(',')

    for transaction in transaction_list:
        print(transaction)

    # for _ in range(1, int(message_count) + 1):
    #     transactions.append(client_socket.recv(BUFFER).decode('utf8'))
    #
