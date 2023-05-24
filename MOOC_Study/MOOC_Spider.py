def Tool_requests():
    import requests
    # r=requests.get('https://api.github.com/user',auth=('1808229384@qq.com','Hk1450385139'))
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def helloword(request):
    return Response("hello")
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello','/')
        config.add_view(helloword,route_name='hello')
        app=config.make_wsgi_app()
    sever=make_server('0.0.0.0',6543,app)
    sever.serve_forever()

    Tool_requests()


