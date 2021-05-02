from flask import Flask, render_template
from flask_restful import Api
from decouple import config
from api.extensions import custom_response
from api.resources import (
    Messages, Message, TextSearch, Users, User, DeleteMessage, test
)
import os

# template_dir = os.path.abspath('')
app = Flask(__name__)


app.config.update(
    DEBUG=config('DEBUG'),
    ENV=config('ENV')
)

# @app.errorhandler(Exception)
# def error_handler(error):
#     response = custom_response(success=False, error='Hubo un error')
#     return response

api = Api(app)

api.add_resource(test, '/test')
api.add_resource(Messages, '/messages')
api.add_resource(Message, '/messages/<int:id>')
api.add_resource(DeleteMessage, '/message/<int:id>')

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

api.add_resource(TextSearch, '/text-search')

@app.route('/hola/')
@app.route('/hola/<nombre>')
def saluda(nombre=None):
	return render_template("chart1.html",nombre=nombre)
    # return app.send_static_file('chart1.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
