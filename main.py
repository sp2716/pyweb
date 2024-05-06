from base64 import urlsafe_b64encode
from operator import methodcaller
from flask import Flask, jsonify, request, send_file, render_template
from pycomm3 import LogixDriver
import json


ip = '192.168.1.1'
tag = "Reactors[0]"


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():  
    
    if request.method == 'POST':
        ip = request.form.get('ip')
        tag = request.form.get('tag')
        return '/result'


@app.route('/result',methods=['GET'])
def result():
    if request.method == 'GET':
        with LogixDriver(ip) as plc:
            print("reading " + tag + " from " + ip)
            data = plc.read(tag)[0:2]
            pl = json.dumps(data)
            return '<!DOCTYPE html><html><body><h1>Controller Data</h1><p>' + pl + '</p></body></html>', 200


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    if request.method == 'GET':
        filename = 'favicon.ico'
        return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
