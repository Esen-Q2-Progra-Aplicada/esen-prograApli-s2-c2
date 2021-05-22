# api
from flask import Flask
from flask_restful import Api
from helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)  # wrapper

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>/<string:salary>")


if __name__ == "__main__":
    app.run(debug=True)
