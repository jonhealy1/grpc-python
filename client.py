import grpc
import typer
# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

app = typer.Typer()

@app.command()
def square_root(val: float):

    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # create a stub (client)
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # create a valid request message
    number = calculator_pb2.Number(value=val)

    # make the call
    response = stub.SquareRoot(number)

    # et voilà
    print(response.value)

if __name__ == "__main__":
    app()