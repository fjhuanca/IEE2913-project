from flask_restful import Resource
from flask import request, Response
import json

class Data(Resource):
  
    
    def post(self):
        global temp
        body = request.get_json(silent=True)
        if body:
            with open('vars.json', 'w') as outfile:
                json.dump(body, outfile)
            return "set"
        return "not set"

    def get(self):
        try:
            with open("vars.json") as file:
                data = json.load(file)
            if data: return data
            else: return dict()
        except:
            return 0

       