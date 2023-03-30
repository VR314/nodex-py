import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:0")  # Bind to a random available port

endpoint = socket.getsockopt(zmq.LAST_ENDPOINT).decode()
print("Bound to endpoint:", endpoint)