# Importiamo le classi
from server import ServerTCP
import sys


def main():
    """
    Funzione principale.
    Permette di scegliere se avviare il server o il client.
    """
    # Se l'argomento è 'server' avviamo il server
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        server = ServerTCP()
        server.start_server()

    else:
        print("Argomento non valido. Usa 'server'")


# Punto di ingresso del programma
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
        import traceback
        traceback.print_exc()