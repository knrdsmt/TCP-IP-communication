import socket
import threading
import os

HOST = 'localhost'
PORT = 12345

klienci = []

mutex = threading.Lock()

def obsluga_klienta(gniazdo_klienta):
    with mutex:
        klienci.append(gniazdo_klienta)
    while True:
        try:
            dane = gniazdo_klienta.recv(1024)
            if not dane:
                break
            if dane.decode() == "SEND_FILE":
                nazwa_pliku = gniazdo_klienta.recv(1024).decode()
                rozmiar_pliku = int(gniazdo_klienta.recv(1024).decode())
                with open(nazwa_pliku, 'wb') as plik:
                    odebrane_dane = 0
                    while odebrane_dane < rozmiar_pliku:
                        fragment = gniazdo_klienta.recv(1024)
                        plik.write(fragment)
                        odebrane_dane += len(fragment)
                print(f"Odebrano plik: {nazwa_pliku}")
            else:
                with mutex:
                    for inny_klient in klienci:
                        if inny_klient != gniazdo_klienta:
                            inny_klient.send(dane)
        except Exception as e:
            print(f"Błąd: {e}")
            break
    with mutex:
        klienci.remove(gniazdo_klienta)
    gniazdo_klienta.close()

gniazdo_serwera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gniazdo_serwera.bind((HOST, PORT))
gniazdo_serwera.listen(5)
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

try:
    while True:
        gniazdo_klienta, adres = gniazdo_serwera.accept()
        print(f"Nowe połączenie od {adres}")
        watek_klienta = threading.Thread(target=obsluga_klienta, args=(gniazdo_klienta,))
        watek_klienta.start()
except KeyboardInterrupt:
    print("Zamykanie serwera...")
    gniazdo_serwera.close()
    for klient in klienci:
        klient.close()
