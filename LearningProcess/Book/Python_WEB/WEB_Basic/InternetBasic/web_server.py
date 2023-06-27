from wsgiref.simple_server import make_server

from application import app
httpd=make_server('',8000,app)
print('serving HTTP om port 8000')
httpd.serve_forever()