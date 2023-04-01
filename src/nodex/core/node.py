import enum
from .messaging.connection import Connection
import json
import subprocess
from ..core.logger import Logger

class Node:
    name = ""
    language = ""
    command = ""
    ports: dict = {}
    args = []

    def __init__(self, node_name):
        node_file = f"{node_name}/{node_name}.node"
        with open(node_file) as f:
            nodeData = json.load(f)
            self.name = nodeData.get("name")
            self.language = nodeData.get("language")
            self.command = nodeData.get("command")
            initPort = nodeData.get("init_port")
            self.ports.update({"init": Connection(f"tcp://0.0.0.0:{initPort}")})
            self.args = nodeData.get("runtime_args")

    def spawn(self):
        s = [self.command] + self.args
        subprocess.Popen(s, shell=True)

    def initSend(self):
        self.ports["init"].send("Hello World!")
        self.ports["init"].send("Hello World!")
        self.ports["init"].send("10 chars!!")
    
    def __str__(self):
        initPort = self.ports["init"]
        return f"Node(name={self.name}, language={self.language}, command={self.command}, initPort={initPort}, args={self.args})"