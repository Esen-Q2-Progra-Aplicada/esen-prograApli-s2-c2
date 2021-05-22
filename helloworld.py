# Base de datos, los datos
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self, name):
        return {"data": f"hello world! {name}"}

    def post(self):
        return {"data": "posted"}
