from flask import Flask, jsonify, request, send_file, render_template, redirect
from pycomm3 import LogixDriver
import json

PLC_IP = "127.0.0.1"
PLCTAG = "Reactors[0].Calcs"
LATEST = "Never ran yet..."

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():  
    global PLC_IP, PLCTAG
    if request.method == 'GET':
        context={'ip': PLC_IP, 'tag': PLCTAG}
        return render_template("index.html", **context)
    

@app.route('/config', methods=['GET', 'POST'])
def config():
    global PLC_IP, PLCTAG
    if request.method == 'POST':
        PLC_IP = request.form.get('ip')
        PLCTAG = request.form.get('tag')
        return redirect('/')
    
    if request.method == 'GET':
        context={'ip': PLC_IP, 'tag': PLCTAG}
        return render_template('config.html', **context), 200


@app.route('/start', methods=['GET'])
def start():
    if request.method == 'GET':
        global LATEST
        try:
            with LogixDriver(PLC_IP,) as plc:
                    print("reading " + PLCTAG + " from " + PLC_IP)
                    data = plc.read(PLCTAG)[0:2]
                    LATEST = json.dumps(data)
                    context={'ip': PLC_IP, 'tag': PLCTAG, 'payload': LATEST}
        except:
                context={'ip': PLC_IP, 'tag': PLCTAG, 'payload': 'comms error'}
        return render_template("index.html", **context)


@app.route('/result',methods=['GET'])
def result():
    if request.method == 'GET':
        global LATEST, PLCTAG, PLC_IP
        try:
            with LogixDriver(PLC_IP,) as plc:
                    print("reading " + PLCTAG + " from " + PLC_IP)
                    data = plc.read(PLCTAG)[0:2]
                    LATEST = json.dumps(data)
                    context = {'payload' : LATEST }
        except:
                context = {'payload': 'comms error'}
            
        return render_template('result.html',**context), 200


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    if request.method == 'GET':
        filename = 'favicon.ico'
        return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
