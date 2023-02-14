#blibiotecas
from flask import Flask
from flask_cors import CORS

import configuration


App = Flask(__name__)

cors = CORS(App)
 
configuration.init_app(App)
configuration.load_extensions(App)


App.run(port=5001) 