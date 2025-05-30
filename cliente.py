import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.sendall(b"Hola desde el cliente")
respuesta = client_socket.recv(1024)
print("Respuesta del servidor:", respuesta.decode())
client_socket.close()
# cliente.py