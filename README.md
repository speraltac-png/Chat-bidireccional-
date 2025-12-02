# Chat bidireccional con Python Sockets, Tkinter y Thread
Este proyecto implementa una sala de chat en tiempo real utilizando la arquitectura Cliente-Servidor. Permite que múltiples usuarios se conecten simultáneamente y se envíen mensajes entre sí mediante una interfaz gráfica amigable.

## Características
Arquitectura Cliente-Servidor: Un servidor central gestiona las conexiones y distribuye los mensajes.

Comunicación TCP: Uso de sockets AF_INET y SOCK_STREAM para una transmisión de datos fiable.

Interfaz Gráfica (GUI): Construida con Tkinter, incluye área de visualización con scroll y campo de entrada.

Multihilo (Threading):

Servidor: Maneja múltiples clientes simultáneamente sin bloquearse.

Cliente: Escucha mensajes entrantes en un hilo secundario para no congelar la interfaz visual.

Broadcast: El servidor reenvía los mensajes a todos los usuarios conectados excepto al remitente.

## Requisitos
Python 3.x

Librerías estándar de Python (no requiere instalación externa):



socket

threading

tkinter

## Estructura del Proyecto
Asegúrate de guardar tus scripts con los siguientes nombres para seguir las instrucciones:

servidor.py: El script que inicia el servidor y gestiona las conexiones.

cliente.py: El script que inicia la interfaz gráfica del usuario.

## Cómo Ejecutar
Para probar el chat, necesitas abrir múltiples terminales (o consolas de comando).

Paso 1: Iniciar el Servidor
Abre la primera terminal y ejecuta:

Bash

python servidor.py
Verás el mensaje: Servidor escuchando en localhost:12345

Paso 2: Iniciar el primer Cliente
Abre una segunda terminal y ejecuta:

Bash

python cliente.py
Se abrirá la ventana del chat. Puedes escribir, pero necesitas a alguien más para hablar.

Paso 3: Iniciar el segundo Cliente
Abre una tercera terminal y ejecuta el mismo comando:

Bash

python cliente.py
Ahora tienes dos ventanas abiertas. Lo que escribas en una aparecerá en la otra.

## Conceptos Técnicos Utilizados
Sockets: El punto final de la comunicación. Usamos el puerto 12345 en localhost.

Buffer (1024): El tamaño de paquete (recv(1024)) define cuántos bytes se reciben por "viaje" de datos.

String Methods: Uso de .strip() para limpiar espacios en blanco innecesarios antes de enviar mensajes.

Tkinter Text vs Entry: Uso de widgets Text configurados con state='disabled' para crear un historial de chat de solo lectura.

## Notas
Si cierras la ventana del cliente, el servidor detectará la desconexión y cerrará el socket correspondiente.

Asegúrate de ejecutar siempre el servidor antes que los clientes.
