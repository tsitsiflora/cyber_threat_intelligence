from taxii2client.v20 import Server
server = Server('http://127.0.0.1:5000/api1',
                user='admin',
                password='Password0')
print(server.title)