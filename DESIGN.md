# DX Design Document

How should developers interface with Nodex? The experience should be intuitive and frictionless. Overhead to start a new project should be as little as possible.


Creating a new nodex project should have a friendly dialog to get set up, similar to cookiecutters. There should also be an option to pass in an already-created config file to bypass the prompts.

```
> nodex project new <directory> <name> -c <config file>
Enter your project's name:
Enter your first node's name:
...
Created project in <directory>!

```

```
> nodex node new <project-root> <name> -c <config file>
Enter your node's name:
Enter the language you want this node to be written in:
...

Created node in <project-root>/<name>!
```

```
> nodex connect new <project-root> <name>
Enter the connection type: 
Enter the source node:
Enter the origin node:
...
Created connection file in connects/<name>.connect!
```

```
> nodex node autocode <project-root> <name>
Generating autocoded stub files in <language (defined in node setup)>
Generated <name>/<name>.py.gen
```

```
> nodex run <node_name> <node_name_2>
```