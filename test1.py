from taxii2client.v20 import Server
server = Server("https://cti-taxii.mitre.org/taxii/")
print(server.title)
print(server.description)
api_root = server.api_roots[0]
print(api_root.title)

coll1 = api_root.collections[1]
print(coll1.title)
print(coll1.description)

obj = coll1.get_objects()
print(obj)