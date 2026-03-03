# Importiamo le classi
from server import ServerTCP
from client import ClientTCP
import sys


def main():
    """
    Funzione principale.
    Permette di scegliere se avviare il server o il client.
    """
    
    # Controlliamo che l'utente abbia inserito un argomento
    if len(sys.argv) < 2:
        print("Uso: python main.py server | client")
        return

    # Se l'argomento è 'server' avviamo il server
    if sys.argv[1] == "server":
        server = ServerTCP()
        server.start_server()

    # Se l'argomento è 'client' avviamo il client
    elif sys.argv[1] == "client":
        client = ClientTCP()
        client.connect_to_server()

    else:
        print("Argomento non valido. Usa 'server' o 'client'")


# Punto di ingresso del programma
if __name__ == "__main__":
    main()