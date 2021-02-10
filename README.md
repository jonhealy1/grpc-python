# grpc-python

### basic setup

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

### compile protobuf

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto`

### run server

`python server.py`

### run client with value to find square root of

`python client.py 6.1`