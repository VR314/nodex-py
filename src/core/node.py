import enum
from messaging.connection import Connection

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

    def __init__(self, name:str, language:Language, command:str, initPort:int, args:list):
        self.name = name
        self.language = language
        self.command = command
        self.args = args
        self.ports.update({"init": Connection(initPort)})

    def initializePorts():
        pass
    
    def __str__(self):
        return f"Node(name={self.name}, language={self.language}, command={self.command}, initPort={self.initPort}, args={self.args})"