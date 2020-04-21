from taxii2client.v20 import Server
server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
api_root = server.api_roots[0]
collection = api_root.collections[0]
objects = collection.get_objects()
print(collection.title)
print(objects)
