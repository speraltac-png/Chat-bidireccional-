import socket
import threading

clientes = []

def manejar_cliente(client_socket, addr):
    print(f"Nueva conexión: {addr}")
    while True:
        try:
            # Recibir mensaje
            mensaje = client_socket.recv(1024)
            if not mensaje:
                eliminar_cliente(client_socket)
                break
            
            broadcast(mensaje, client_socket)
            
        except:
            eliminar_cliente(client_socket)
            break

def broadcast(mensaje, remitente_socket):
    for cliente in clientes:
        # Enviar a todos menos al que escribió el mensaje
        if cliente != remitente_socket:
            try:
                cliente.send(mensaje)
            except:
                eliminar_cliente(cliente)

def eliminar_cliente(client_socket):
    if client_socket in clientes:
        clientes.remove(client_socket)
        client_socket.close()

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        # Aceptar nueva conexión
        client_socket, addr = server_socket.accept()
        clientes.append(client_socket)
        
        # Iniciar un hilo separado para manejar a este cliente
        hilo = threading.Thread(target=manejar_cliente, args=(client_socket, addr))
        hilo.start()

if __name__ == "__main__":
    start_server()