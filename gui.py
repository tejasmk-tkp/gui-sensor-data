from nicegui import ui
import sys
import socket
import json
import asyncio

ui.label('Sensor Data')

columns = [{'name': 'Sensor', 'label': 'Sensor', 'field': 'Sensor', 'required': True, 'align': 'left'},
        {'name': 'Value', 'label': 'Value', 'field': 'Value', 'sortable': False},
        ]

rows = [{'Sensor': 'MQ136', 'Value': ' '},
        {'Sensor': 'MQ2', 'Value': ' '},
        {'Sensor': 'DHT11', 'Value': ' '},
        {'Sensor': 'A extra1', 'Value': ' '},
        {'Sensor': 'A extra2', 'Value': ' '},
        {'Sensor': 'MQ137', 'Value': ' '},
        {'Sensor': 'MQ7', 'Value': ' '},
        ]

table = ui.table(columns=columns, rows=rows, row_key='name')

def update_table(data):
    for row in rows:
        sensor_name = row['Sensor']
        if sensor_name in data:
            row['Value'] = data[sensor_name]

    table.refresh()

async def socket_server():
    host, port = '127.0.0.1', 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = await loop.sock_accept(server_socket)
        loop.create_task(handle_connection(conn, addr))

async def handle_connection(conn, addr):
    print(f"Connected by {addr}")

    data = await loop.sock_recv(conn, 1024)
    if not data:
        conn.close()
        return

    sensor_data = json.loads(data.decode('utf-8'))

    await update_table(sensor_data)

    conn.close()

loop = asyncio.get_event_loop()

loop.create_task(socket_server())

ui.run()
