import os
from nodex.core.node import Node
from nodex.core.logger import Logger

class MyNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)

def main():
    node_name = os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1]
    node = MyNode(node_name)
    # Logger.log(f"Node: {node}")
    node.initSend()


if __name__ == "__main__":
    main()
