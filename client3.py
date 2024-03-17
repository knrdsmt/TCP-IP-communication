import socket
import threading

HOST = 'localhost'
PORT = 12345

gniazdo_klienta = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gniazdo_klienta.connect((HOST, PORT))

def odbieranie_wiadomosci():
    while True:
        try:
            wiadomosc = gniazdo_klienta.recv(1024).decode()
            if wiadomosc:
                print("\nOtrzymana wiadomość: ", wiadomosc)
            else:
                break
        except:
            break

threading.Thread(target=odbieranie_wiadomosci).start()

try:
    while True:
        wiadomosc = input("Wprowadź wiadomość: ")
        gniazdo_klienta.send(wiadomosc.encode())
except KeyboardInterrupt:
    print("Zamykanie klienta...")
    gniazdo_klienta.close()
