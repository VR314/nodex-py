import argparse
import zmq
from ..core.node import Node
from .util import is_file_path
from ..core.logger import Logger

def new_node(args):
    print(f"Creating a new node project with name \"{args.project_name}\"")

def remove_node(args):
    print(f"Removing node project with name \"{args.project_name}\"")

def new_project(args):
    print(f"Creating a new project with name \"{args.project_name}\"")

def new_connect(args):
    print(f"Connecting to project with name \"{args.project_name}\"")

def parseNodes(node_names: list):
    nodes = [Node(node_name) for node_name in node_names]
    return nodes

# TODO: move this to a publish/subscribe model, try using a Poller object to remove blocking behavior
def run_nodes(args):
    Logger.log(f"Running nodes: {args.nodes}")    
    nodes = parseNodes(args.nodes)
    Logger.log(" " + ''.join(str([str(node) for node in nodes])) + " ")

    context = zmq.Context()
    sockets = []

    for node in nodes:
        socket = context.socket(zmq.PAIR)
        socket.bind(node.ports["init"].endpoint)  # Bind to a random available port

        endpoint = socket.getsockopt(zmq.LAST_ENDPOINT).decode()
        Logger.log("Bound to endpoint from run:" + endpoint)

        socket.setsockopt(zmq.RCVTIMEO, 1000)
        sockets.append(socket)
        node.spawn()

    message = ""
    while len(message) != 10:
        try:
            for socket in sockets:
                message = socket.recv_string()
                Logger.log("Received message: " + message + " on socket: " + str(socket))
        except zmq.error.Again as e:
            Logger.log("No message received within timeout period" + " on socket: " + str(socket))

def main():
    parser = argparse.ArgumentParser(description='Nodex CLI')
    subparsers = parser.add_subparsers(title='subcommands', dest='command')

    # Subparser for "project"
    project_parser = subparsers.add_parser('project', help='Project commands')

    # Subparser for "project new"
    project_new_subparser = project_parser.add_subparsers(title='project new', dest='project')
    project_new_parser = project_new_subparser.add_parser('new', help='Create a new project')
    project_new_parser.add_argument('project_name', help='Name of the new project')
    project_new_parser.add_argument('--dest', '-d', type=is_file_path, help='Destination of the new project')
    project_new_parser.set_defaults(func=new_node)

    # Subparser for "node"
    node_parser = subparsers.add_parser('node', help='Node commands')

    # Subparser for "node new"
    node_new_subparser = node_parser.add_subparsers(title='node new', dest='node')
    node_new_parser = node_new_subparser.add_parser('new', help='Create a new project')
    node_new_parser.add_argument('node_name', help='Name of the new node')
    node_new_parser.add_argument('--config', '-c', type=is_file_path, help='Location of the config file to use')
    node_new_parser.set_defaults(func=new_node)

    # Subparser for "connect"
    parser_connect = subparsers.add_parser('connect', help='Connection commands')

    # Subparser for "connect new"
    parser_connect_new = parser_connect.add_subparsers(title='connect new', dest='connect')
    project_new_subparser = parser_connect_new.add_parser('new', help='Create a new connection')
    project_new_subparser.add_argument('project_name', help='Name of the project to connect to')
    project_new_subparser.set_defaults(func=new_connect)

    # Parser for "run"
    parser_run = subparsers.add_parser('run', help='Run a command')
    parser_run.add_argument('nodes', nargs=argparse.REMAINDER, help='Node names to run')
    parser_run.set_defaults(func=run_nodes)

    args = parser.parse_args()

    args.func
    args.func(args)

if __name__ == '__main__':
    main()