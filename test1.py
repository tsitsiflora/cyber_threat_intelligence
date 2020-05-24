from taxii2client.v20 import Collection
coll = Collection('http://127.0.0.1:5000/trustgroup1/collections/91a7b528-80eb-42ed-a74d-c6fbd5a26116',
                user='admin',
                password='Password0')
print(coll.title) 
print(coll.description)
obj = coll.get_objects()
print(obj)