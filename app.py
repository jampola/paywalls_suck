#!/usr/bin/env python2
from flask import Flask, flash, request, url_for, render_template, abort, Response
from flask_restful import Resource, Api, reqparse
from lib import screenshot
from functools import wraps
import datetime, logging, traceback, os

# App and Imports setup
app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False
app.secret_key = 'Turn off the lights, I\'m watching Back to the Future'
logger = logging.getLogger(__name__)
parser = reqparse.RequestParser()

# Logging Setup

# Check to see if logs is created, if not, create it
if not os.path.exists('logs/'):
    os.makedirs('logs/')

logger.setLevel(logging.INFO)
handler = logging.FileHandler('./logs/{}.log'.format(datetime.datetime.now().strftime("%Y-%m-%d")))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# API keys (Maybe if enough people want to use this, I might make use of SQLachemy)
keys = [
    'e4b2ce6cc31eca46fc64257f3cadb4fa' # md5sum as an example
]


''' Start Basic API key Mechanism '''
def check_auth(key):
    return key in keys

def authenticate():
    return Response('Sorry. A valid API key is required in the request header.', 401)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers
        # Allow our local service to use the API
        if request.remote_addr == '127.0.0.1':
            return f(*args, **kwargs)
            logger.info('API Auth Success')
        # Only allow specified non-local keys to use the API    
        if not auth or not check_auth(auth['api_key']):
            logged.error("Could not auth API for {}".format(request.remote_addr))
            return authenticate()

        return f(*args, **kwargs)

    return decorated
''' End Basic API key Mechanism '''

'''Start API End Point '''
class GrabScreenGrab(Resource):
    def get(self):
        return "{'data':'Nothing to see here, run along now...'}"

    @requires_auth
    def post(self):
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('width')
        parser.add_argument('height')
        args = parser.parse_args()
        
        # default values
        width, height = 0, 0
        if args['width']: width = args['width']
        if args['height']: height = args['height']

        try:
            image_url = screenshot.get_screenshot(args['url'], width, height)
            logger.info("Image URL Returned {}".format(image_url))
            return {"url": image_url} 
        except:
            logger.error(traceback.format_exc())
            abort(401)
            

api.add_resource(GrabScreenGrab, '/api/grab')
''' End API End Point '''

''' Start Views '''

# Year in footer
year = datetime.datetime.now().strftime("%Y")

# root
@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html',year=year)

# about
@app.route("/about")
def about():
    print request.remote_addr
    return render_template('about.html',year=year)
''' End Views '''

if __name__ == '__main__':
    app.run(debug=True)