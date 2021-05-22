# Base de datos, los datos
from flask_restful import Resource

names = {
    "balbino": {"name": "balbino", "age": 23, "salary": 1000.0},
    "paulina": {"name": "paulina", "age": 27, "salary": 1500.0},
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def put(self, name, age, salary):
        floatSalary = float(salary)
        value = {"name": name, "age": age, "salary": floatSalary}
        names[name] = value
        return names[name]
