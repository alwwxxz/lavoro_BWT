from bwt import bwt_transform
import socket as sck

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    IP="127.0.0.1" #maggiore di 1023 
    PORTA=5000
    server.bind((IP, PORTA)) #tupla
    server.listen(5) #coda di attesa può contenere al massimo 5 elementi 
    #(facoltativo, sennò lo da OS)   
    print("Server in ascolto su IP: ", IP, " e porta: ", PORTA)

    connessione, indirizzo_client = server.accept() #metodo bloccante, attende
    #la connessione di un client
    with connessione:
        print("Socket di connesione: ", connessione.getsockname())

        dati=connessione.recv(1024) #num massimo di byte da ricevere, in attesa di
        #dati (bloccante)
        bwt_result = bwt_transform(dati.decode()) #da byte a stringa 
        connessione.sendall(bwt_result.encode())
print("Server terminato")