#!/usr/bin/env python
#!flask/bin/python
from flask import Flask, jsonify, request
from taxii2client.v20 import Server
from taxii2client.v20 import Collection
from stix2 import *

app = Flask(__name__)

def prepare_response(res_object, status_code = 200):
    response = jsonify(res_object)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response, status_code
    
@app.route('/api/ioc/create', methods=['POST'])    
def create_ioc():
    
    
    collection = Collection('http://127.0.0.1:5000/trustgroup1/collections/365fed99-08fa-fdcd-a1b3-fb247eb41d01',
                            user='admin',
                            password='Password0')

    name = request.form.get('name')
    rtype = request.form.get('type')
    pattern = request.form.get('pattern')
    labels = request.form.get('labels')

    # return prepare_response({'status': 'error', 'message': 'Something went wrong while trying to save IoC'})
    if rtype == "Indicator":
        indicator = Indicator(name=name, pattern=pattern, labels=labels)
        bundle = Bundle([indicator]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Malware":
        malware = Malware(name=name, labels=labels)
        bundle = Bundle([malware]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Attack Pattern":
        attack_pattern = AttackPattern(name=name, pattern=pattern, labels=labels)
        bundle = Bundle([attack_pattern]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Identity":
        identity = Identity(name=name, labels=labels)
        bundle = Bundle([identity]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Threat Actor":
        threat_actor = ThreatActor(name=name, pattern=pattern, labels=labels)
        bundle = Bundle([threat_actor]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Tool":
        tool = Tool(name=name, pattern=pattern, labels=labels)
        bundle = Bundle([tool]).serialize()
        collection.add_objects(bundle)
    elif rtype == "Vulnerability":
        vuln = Vulnerability(name=name, pattern=pattern, labels=labels)
        bundle = Bundle([vuln]).serialize()
        collection.add_objects(bundle)
    
    return prepare_response({'status': 'success', 'message': 'IoC was saved successfully'})


@app.route('/api/ioc/view_new', methods=['GET'])    
def view_new_ioc():
    
    collection = Collection('http://127.0.0.1:5000/trustgroup1/collections/365fed99-08fa-fdcd-a1b3-fb247eb41d01',
                            user='admin',
                            password='Password0')

    new_objects = collection.get_objects()
    print(new_objects)
    return prepare_response({'data':new_objects})


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
