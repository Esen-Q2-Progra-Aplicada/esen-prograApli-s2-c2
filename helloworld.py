# Base de datos, los datos
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {"data": "hello world!"}

    def post(self):
        return {"data": "posted"}
