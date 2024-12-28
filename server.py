import threading
import hashlib  # For encoding and decoding of the message
import socket  # Establishes connection between server and client
import sqlite3

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S] Server socket created")
except socket.error as err:
    print("Socket error:", err)
    exit()

server_binding = ('localhost', 9998)
ss.bind(server_binding)
ss.listen()

def check(username, password):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def start_connection(client):
    data = client.recv(1024).decode()
    username, password = data.split(",")

    # Build login server that verifies the username and password as a valid user
    if check(username, password):
        client.sendall("You exist and are a good person :)".encode())
    else:
        client.sendall("What is wrong with you? Stranger danger".encode())

    client.close()

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

ss.close()
exit()
