import zmq
from ...core.logger import Logger

class Connection:
    def __init__(self, endpoint:str):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)        
        if endpoint is None:   
          self.endpoint = self.socket.getsockopt(zmq.LAST_ENDPOINT).decode()
        else: 
          self.endpoint = endpoint
        self.socket.connect(self.endpoint)
        Logger.log("Connected to endpoint from connection:" + self.endpoint)

    def send(self, message:str):
        self.socket.send_string(message)
        Logger.log("Sent message: " +  message)

    def __str__(self):
        return f"Connection(endpoint={self.endpoint})"