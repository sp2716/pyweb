
from base64 import urlsafe_b64encode
from operator import methodcaller
from flask import Flask, jsonify, request, send_file, render_template
from pycomm3 import LogixDriver
import json

PLC_IP = "192.168.1.1"
PLCTAG = "Reactors[0]"



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():  
    global PLC_IP, PLCTAG
    if request.method == 'GET':
        str = "IP Address:" + PLC_IP + " Tagname:" + PLCTAG
        return str, 200
    
    if request.method == 'POST':
        PLC_IP = request.form.get('ip')
        PLCTAG = request.form.get('tag')
        str = "IP Address:" + PLC_IP + " Tagname: " + PLCTAG
        print("IP and tag changed to: " + PLC_IP + PLCTAG)
        return str, 200


@app.route('/result',methods=['GET'])
def result():
    if request.method == 'GET':
        with LogixDriver(PLC_IP) as plc:
            print("reading " + PLCTAG + " from " + PLC_IP)
            data = plc.read(PLCTAG)[0:2]
            pl = json.dumps(data)
            return '<!DOCTYPE html><html><body><h1>Controller Data</h1><p>' + pl + '</p></body></html>', 200


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    if request.method == 'GET':
        filename = 'favicon.ico'
        return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
