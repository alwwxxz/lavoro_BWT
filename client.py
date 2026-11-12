import socket as sck

messaggio=input("Inserisci il messaggio da inviare al server: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 5000))
    print("Connessione al server stabilita")
    client.sendall(messaggio.encode()) #da stringa a bytes
    print("Messaggio inviato al server")
    risposta=client.recv(1024)
    print("Risposta dal server: ", risposta.decode()) #da bytes a stringa

print("Client terminato")