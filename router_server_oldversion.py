import flask
from flask import Flask
import router_db

db = router_db.load_data('db.json')

app = Flask(__name__)

def get_service_name():
    return "routerdienst"

# http://127.0.0.1/
@app.route('/')
def show_router_info():
    s_name = get_service_name()
    response = flask.render_template("service.html", service_name=s_name)
    return response

# http://127.0.0.1/interfaces/Loopback334
@app.route('/routers')
def show_routers():
    content = "Routers"
    #
    return content


# http://127.0.0.1/interfaces/Loopback334
@app.route('/interfaces')
def show_interfaces():
    return flask.request

# http://127.0.0.1/interfaces/Loopback334
@app.route('/interfaces/<device_name>')
def show_interface(device_name):
    return "Details van {device_name}"

