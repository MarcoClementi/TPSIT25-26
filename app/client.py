# Importiamo il modulo socket
import socket


# Definizione della classe ClientTCP
class ClientTCP:
    def __init__(self, host='localhost', port=5000):
        """
        Costruttore della classe ClientTCP.
        :param host: indirizzo del server
        :param port: porta del server
        """
        self.host = host
        self.port = port

        # Creiamo il socket TCP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        """
        Metodo per connettersi al server e inviare un messaggio.
        """
        # Connessione al server
        self.client_socket.connect((self.host, self.port))

        # Otteniamo il nome dell'host locale
        host_name = socket.gethostname()

        # Creiamo un messaggio da inviare
        message = f"Ciao server! Sono il client su host: {host_name}"

        # Inviamo il messaggio al server
        self.client_socket.send(message.encode())

        # Riceviamo la risposta dal server
        response = self.client_socket.recv(1024).decode()

        print(f"Risposta dal server: {response}")

        # Chiudiamo la connessione
        self.client_socket.close()