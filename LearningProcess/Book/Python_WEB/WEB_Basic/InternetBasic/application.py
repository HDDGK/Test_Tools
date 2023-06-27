def app(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    file_name=environ['PATH_INFO'][1:]or 'index.html'
    HTML_ROOT_DIR='./Views/'
    try:
        file=open(HTML_ROOT_DIR+file_name,'rb')
    except IOError:
        response_body="The file is not Found!"
    else:
        file_data=file.read()
        file.close()
        response=file_data.decode('utf-8')
    return [response.encode('utf-8')]