import json
import subprocess

from nodex.core.topic import Topic
from nodex.core.lifeline import Lifeline
from nodex.core.logger import Logger

'''
First, create the lifeline to the CORE, which is used for updates on lifecycle, errors, etc.
Then, connect to all topics (PUB/SUB) to receive messages from other nodes. Dynamically open ports as the publishers of the topics come online.
'''

class Node:
    name = ""
    language = ""
    command = ""
    topics: list[Topic] = []
    args = []
    lifeline: Lifeline = None

    def __init__(self, node_name):
        node_file = f"nodes/{node_name}/{node_name}.node"
        with open(node_file) as f:
            node_data = json.load(f)
            self.name = node_data.get("name")
            self.language = node_data.get("language")
            self.command = node_data.get("command")
            init_port = node_data.get("init_port")
            self.lifeline = Lifeline(f"tcp://0.0.0.0:{init_port}")
            self.args = node_data.get("runtime_args")
            topic_dict = node_data.get("topics")
            for topic in topic_dict:
                self.topics.append(Topic(topic["name"]))

        Logger.log(self.topics)

    def spawn(self):
        string = [self.command] + self.args
        subprocess.Popen(string, shell=True)

    def initSend(self):
        self.lifeline.send("Hello World!")
        self.lifeline.send("Hello World!")
        self.lifeline.send("10 chars!!")
    
    def __str__(self):
        return f"Node(name={self.name}, language={self.language}, command={self.command}, initPort={self.lifeline}, args={self.args})"