import argparse
import os

def is_int(value):
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"\"{value}\" is not a valid integer")
    
def is_file_path(value):
    path = os.path.dirname(os.path.realpath(__file__)) + "/" + value
    if (not os.path.isfile(path) and (not os.path.exists(path))):
        raise argparse.ArgumentTypeError(f"\"{value}\" is not a valid file path")
    return value

def new_node(args):
    print(f"Creating a new node project with name \"{args.project_name}\"")

def remove_node(args):
    print(f"Removing node project with name \"{args.project_name}\"")

def new_project(args):
    print(f"Creating a new project with name \"{args.project_name}\"")

def new_connect(args):
    print(f"Connecting to project with name \"{args.project_name}\"")

def run_nodes(args):
    print(f"Running nodes: {args.nodes}")

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

    try:
        args.func
        args.func(args)
    except AttributeError:
        parser.print_help()
        parser.error("too few arguments")

if __name__ == '__main__':
    main()
