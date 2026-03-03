# Importiamo il modulo socket che permette la comunicazione di rete
import socket


# Definizione della classe ServerTCP
class ServerTCP:
    def __init__(self, host='localhost', port=5000):
        """
        Costruttore della classe ServerTCP.
        :param host: indirizzo IP o nome host su cui il server ascolta
        :param port: porta su cui il server resta in ascolto
        """
        self.host = host
        self.port = port
        
        # Creiamo il socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        """
        Metodo per avviare il server.
        """
        # Colleghiamo il socket all'indirizzo e alla porta
        self.server_socket.bind((self.host, self.port))

        # Mettiamo il server in ascolto (max 5 connessioni in coda)
        self.server_socket.listen(5)

        print(f"Server avviato su {self.host}:{self.port}")
        print("In attesa di connessioni...")

        # Ciclo infinito per accettare connessioni
        while True:
            # Accettiamo una connessione
            client_socket, client_address = self.server_socket.accept()

            print(f"Connessione ricevuta da {client_address}")

            # Riceviamo i dati dal client (max 1024 byte)           
            data = client_socket.recv(1024).decode()
            while len(data) > 0:
                print(f"Messaggio ricevuto: {data}")
                data = client_socket.recv(1024).decode()
                
            # Inviamo una risposta al client
            response = "Messaggio ricevuto correttamente!"
            client_socket.send(response.encode())

            # Chiudiamo la connessione con il client
            client_socket.close()