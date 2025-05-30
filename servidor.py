#servidor web
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Servidor ejecutándose...")
conn, addr = server_socket.accept()
print("Esperando conexiones en puerto {addr}")

data = conn.recv(1024)
print("Datos recibidos:", data.decode())

conn.sendall(b"Hola desde el servidor mundo!")
conn.close()
