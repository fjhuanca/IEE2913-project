from flask_restful import Resource
from flask import request, Response


class Data(Resource):
  
    
    def post(self):
        global temp
        body = request.get_json(silent=True)
        if body:
            pot = body["pot"]
            with open("vars_log.txt", "w") as file:
                file.write(str(pot))
            return "set"
        return "not set"

    def get(self):
        with open("vars_log.txt") as file:
            return file.read()

       