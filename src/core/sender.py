import os
import zmq

from node import Node, Language

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.connect("tcp://0.0.0.0:4501")

endpoint = socket.getsockopt(zmq.LAST_ENDPOINT).decode()

node = Node("test", Language.PYTHON, "python3 main.py", endpoint, [])
node.ports["init"].send("Hello World!")
