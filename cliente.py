import socket
import argparse

parser = argparse.ArgumentParser(description="Cliente TCP")
parser.add_argument("port", type=int, help="Puerto al que conectar")

args = parser.parse_args()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', args.port))
client_socket.sendall(b"Hola desde el cliente")
respuesta = client_socket.recv(1024)
print("Respuesta del servidor:", respuesta.decode())
client_socket.close()


# cliente.py