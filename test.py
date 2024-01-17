import socket
import json
import time
import random

def send_random_data():
    host, port = '127.0.0.1', 8888
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    sensors = ['MQ136', 'MQ2', 'DHT11', 'A extra1', 'A extra2', 'MQ137', 'MQ7']

    while True:
        sensor_data = {sensor: random.uniform(0, 100) for sensor in sensors}
        json_data = json.dumps(sensor_data).encode('utf-8')
        client_socket.sendall(json_data)
        time.sleep(0.02)

    client_socket.close()

send_random_data()
