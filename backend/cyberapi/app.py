#!flask/bin/python
#!flask/bin/python
from flask import Flask, jsonify
from taxii2client.v20 import Server

app = Flask(__name__)

def prepare_response(res_object, status_code = 200):
    response = jsonify(res_object)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response, status_code

@app.route('/api/mitre-pre', methods=['GET'])
def get_preattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root.collections[1]
    
    objects = collection.get_objects()
    return prepare_response({'data': objects["objects"]})


@app.route('/api/phishtank', methods=['GET'])
def get_objects():
    server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
    api_root = server.api_roots[0]
    collection = api_root.collections[0]

    objects = collection.get_objects()
    return prepare_response({'data': objects["objects"]})


@app.route('/api/mitre-enterprise', methods=['GET'])
def get_entepriseattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root.collections[1]
    
    objects = collection.get_objects()
    return prepare_response({'data': objects["objects"]})

@app.route('/api/mitre-mobile', methods=['GET'])
def get_mobileattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root.collections[2]
    
    objects = collection.get_objects()
    return prepare_response({'data': objects["objects"]})

if __name__ == '__main__':
    app.run(debug=True, port=8050)