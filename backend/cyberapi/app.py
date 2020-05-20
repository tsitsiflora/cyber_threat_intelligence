#!flask/bin/python
#!flask/bin/python
from flask import Flask, jsonify
from taxii2client.v20 import Server

app = Flask(__name__)


@app.route('/api/mitre-pre', methods=['GET'])
def get_preattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root[1]
    
    objects = collection.get_objects()
    return jsonify({'data': objects["objects"]})

@app.route('/api/data/phishtank', methods=['GET'])
def get_objects():
    server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
    api_root = server.api_roots[0]
    collection = api_root.collections[0]

    objects = collection.get_objects()
    return jsonify({'data': objects["objects"]})

@app.route('/api/mitre-enterprise', methods=['GET'])
def get_entepriseattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root[0]
    
    objects = collection.get_objects()
    return jsonify({'data': objects["objects"]})

@app.route('/api/mitre-mobile', methods=['GET'])
def get_mobileattack_objects():
    server = Server('https://cti-taxii.mitre.org/taxii')
    api_root = server.api_roots[0]
    collection = api_root[2]
    
    objects = collection.get_objects()
    return jsonify({'data': objects["objects"]})

if __name__ == '__main__':
    app.run(debug=True)