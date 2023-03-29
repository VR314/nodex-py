# Nodex

Problem Statement: ROS and FPrime… suck. 
	- ROS: heavy/bloated
	- FPrime: old, undocumented, XML/CMake building and debugging hell

Solution: Make a new framework for modular, component-based codebases. Priority should be ease of unit testing and running with input spoofing. Should work with multiple languages and generate *USEFUL* errors.



General important steps to a functioning proof of concept:
	1. Determine a messaging protocol (defining a schema for the payload of a message on a connection)
		a. timestamp, connection, sending and receiving components, etc.
	2. Determine a multi-process communication middleware (ZeroMQ or gRPC)
	3. Determine component and connection instantiation schema (DSL)
	4. Implement codegen for different languages based on component and connection instantiation
	5. Component lifecycle manager (start/stop/monitor components)
	6. Runtime config on a component and system level that affects runtime but does NOT require a re-compile of the C/C++/Java code
Robust tests of the code I've written + create a method for testing components
