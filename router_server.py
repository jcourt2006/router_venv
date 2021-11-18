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

# http://127.0.0.1/routers
@app.route('/routers')
def show_routers():
    response = flask.render_template("routers.html", routers=db)
    return response


# http://127.0.0.1/interfaces/Loopback334
@app.route('/interfaces')
def show_interfaces():
    return flask.render_template("service.html", service_name="the home page of Julio")

# http://127.0.0.1/interfaces/Loopback334
@app.route('/interfaces/<device_name>')
def show_interface(device_name):
    return f"Details van {device_name}"

@app.route('/julio')
def show_text():
    my_html = '''

    <body style="background-color: #b1db34;">


        <h1 style="color:  #002aff;">"Hallo <b>Julio</b>"</h1>

    </body>

    '''
    return my_html



