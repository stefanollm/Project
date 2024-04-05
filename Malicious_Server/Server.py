"""
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Definizione di una sottoclasse MyHandler che estende FTPHandler
class MyHandler(FTPHandler):
    # Metodo chiamato quando un file viene ricevuto
    def on_file_received(self, file):
        filename = os.path.basename(file)  # Ottiene il nome del file ricevuto
        destination = os.path.join("Malicious_Server", filename)  # Definisce il percorso di destinazione
        os.rename(file, destination)  # Sposta il file nella directory di destinazione
        print(f"FILE '{filename}' RICEVUTO E SALVATO IN '{destination}'\n")  # Stampa un messaggio di conferma

# Creazione di un autorizzatore Dummy
authorizer = DummyAuthorizer()
# Aggiunta di un utente con nome utente 'user', password 'pass' e permessi nella directory corrente
authorizer.add_user("user", "pass", ".", perm="elradfmwMT")

# Creazione di un'istanza del gestore MyHandler
handler = MyHandler
# Collegamento dell'autorizzatore al gestore
handler.authorizer = authorizer

# Creazione di un'istanza del server FTP che ascolta sull'indirizzo 127.0.0.1 e sulla porta 1337
server = FTPServer(("127.0.0.1", 1337), handler)
# Avvio del server FTP in un loop infinito
server.serve_forever()
"""


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define a custom FTP handler class inheriting from FTPHandler
class MyFTPHandler(FTPHandler):
    def on_file_received(self, file):
        print(f"FILE '{file}' RICEVUTO'\n")

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()

# Add a new user with write permissions on all directories and subdirectories
authorizer.add_user("user", "pass", script_directory, perm="elradfmwMT")

# Instantiate an instance of your custom FTP handler
handler = MyFTPHandler
handler.authorizer = authorizer

# Specify the address and port for the FTP server to listen on
server_address = ("127.0.0.1", 1337)

# Instantiate the FTP server with your custom handler
server = FTPServer(server_address, handler)

# Start the FTP server
server.serve_forever()


