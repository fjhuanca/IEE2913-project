from flask import Flask, render_template
from flask_restful import Api
from decouple import config
from api.extensions import custom_response
from api.resources import Data
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
api.add_resource(Data, '/data')

@app.route('/plot/')
@app.route('/plot/<nombre>')
def saluda(nombre=None):
	return render_template("chart1.html",nombre=nombre)
    # return app.send_static_file('chart1.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
