import socket
import tkinter as tk
import threading

def start_client():
    ventana = tk.Tk()
    ventana.title("Chat Cliente")
    ventana.geometry("500x500")

    label = tk.Label(ventana, text="CHAT CON SOCKETS", height=1, font=("Arial", 20, "bold"))
    label.pack(pady=10) 

  
    salida = tk.Text(ventana, height=15, width=55)
    salida.pack(padx=10, pady=5)
    salida.config(state='disabled') 

    label2 = tk.Label(ventana, text="Escribe tus mensajes:")
    label2.pack()

    
    entrada = tk.Text(ventana, height=4, width=55)
    entrada.pack(padx=10, pady=10)

  
    host = 'localhost'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        salida.config(state='normal')
        salida.insert(tk.END, "No se pudo conectar al servidor.\n")
        salida.config(state='disabled')
        return 
    

    def enviar():
        
        mensaje = entrada.get("1.0", "end-1c")
        
        if mensaje.strip() != "":
            try:
                client_socket.send(mensaje.encode('utf-8'))
                
                # Mostrar el mensaje en la pantalla
                mostrar_mensaje(f"Tú: {mensaje}")
                
                # Limpiar la caja de entrada
                entrada.delete("1.0", tk.END)
            except:
                mostrar_mensaje("Error al enviar mensaje.")

    def recibir_mensajes():
        "Escucha mensajes del servidor en segundo plano"
        while True:
            try:
                mensaje = client_socket.recv(1024).decode('utf-8')
                if mensaje:
                    mostrar_mensaje(f"Amigo: {mensaje}")
            except:
                mostrar_mensaje("Desconectado del servidor.")
                client_socket.close()
                break

    def mostrar_mensaje(texto):
        "Agrega texto a la caja de salida de forma segura"
        salida.config(state='normal') # Habilitar edición
        salida.insert(tk.END, texto + "\n")
        salida.see(tk.END) # Scroll al final
        salida.config(state='disabled') # Bloquear edición

    boton = tk.Button(ventana, text="Enviar", command=enviar)
    boton.pack()

    # Iniciar el hilo que escucha mensajes entrantes
    hilo_escucha = threading.Thread(target=recibir_mensajes, daemon=True)
    hilo_escucha.start()

    ventana.mainloop()

if __name__ == "__main__":
    start_client()