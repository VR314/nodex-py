# Nodex

### Problem Statement: ROS and FPrime… suck. 
	- ROS: heavy/bloated
	- FPrime: old, undocumented, XML/CMake building and debugging hell

### Solution: 
- Make a new framework for modular, component-based codebases. 
- Priority should be ease of unit testing and running with input spoofing. 
- Should work with multiple languages and generate *USEFUL* errors. 
  - Since multiple languages within one project are supported, each node can leverage the libraries written for each language.

General important steps to a functioning proof of concept:
1. Determine a messaging protocol (defining a schema for the payload of a message on a connection) [timestamp, connection, sending and receiving components, etc.]
2. Determine a multi-process communication middleware (ZeroMQ or gRPC)
3. Determine component and connection instantiation schema (DSL w/ parser)
4. Implement error handling/propogation
5. Implement codegen for different languages based on component and connection instantiation
6. Component lifecycle manager (start/stop/monitor components)
7. Runtime config on a component and system level that affects runtime but does NOT require a re-compile of compiled components
8. Robust tests of the framework internal code + create a method for testing components

## Development
1. requirements: Python 3.10
2. `cd src` and `source setup_venv.sh`
3. `pip install -r requirements.txt`
4. `cd nodex` and `pip install -e .`
5. `pip list` to verify nodex is installed
6. run `nodex run ...node_names` to run nodes from the root directory of an example project
