from taxii2client.v20 import Collection
from stix2 import *



coll = Collection('http://127.0.0.1:5000/trustgroup1/collections/365fed99-08fa-fdcd-a1b3-fb247eb41d01',
                user='admin',
                password='Password0')

indicator = Indicator(name="File hash for malware variant",
                      labels=["malicious-activity"],
                      pattern="[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']")
#print(indicator)

bundle = Bundle([indicator]).serialize()
coll.add_objects(bundle)

obj = coll.get_objects()
print(obj)
