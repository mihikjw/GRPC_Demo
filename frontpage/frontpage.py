from flask import Flask, render_template
import grpc_functions
import os

app = Flask(__name__)

cpp_address = os.getenv("CPP_ENDPOINT", "")
py_address = os.getenv("PY_ENDPOINT", "")


@app.route("/")
def get_frontpage():
    output = {}

    # contact c++ service
    if len(cpp_address):
        name, location, error = grpc_functions.make_request(cpp_address)
        if not len(error):
            output[location] = name
        else:
            print("Error Contacting C++ Endpoint: " + error)
    else:
        print("C++ Endpoint Not Configured")

    # contact python service
    if len(py_address):
        name, location, error = grpc_functions.make_request(py_address)
        if not len(error):
            output[location] = name
        else:
            print("Error Contacting Python Endpoint: " + error)
    else:
        print("Python Endpoint Not Configured")

    return render_template('index.html', response_data=output)


if __name__ == "__main__":
    app.run("0.0.0.0", port=1234)
