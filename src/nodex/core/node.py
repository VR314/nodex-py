import enum
from .messaging.connection import Connection
import json

class Language(enum.Enum):
    PYTHON = 0
    CPP = 1
    JS = 2

class Node:
    name = ""
    language: Language = None
    command = ""
    ports: dict = {}
    args = []

    def __init__(self, node_name):
        node_file = f"{node_name}/{node_name}.node"
        with open(node_file) as f:
            nodeData = json.load(f)
            print(nodeData.get("name"), nodeData.get("language"), nodeData.get("command"), nodeData.get("init_port"), nodeData.get("runtime_args"))
            self.name = nodeData.get("name")
            self.language = nodeData.get("language")
            self.command = nodeData.get("command")
            initPort = nodeData.get("init_port")
            self.ports.update({"init": Connection(f"tcp://0.0.0.0:{initPort}")})
            self.args = nodeData.get("runtime_args")

    def initializePorts():
        pass

    def initSend(self):
        self.ports["init"].send("Hello World!")
        self.ports["init"].send("Hello World!")
        self.ports["init"].send("10 chars!!")
    
    def __str__(self):
        return f"Node(name={self.name}, language={self.language}, command={self.command}, initPort={self.initPort}, args={self.args})"