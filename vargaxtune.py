# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file

@route('/inicio',method="get")
@route('/')
def inicio():
    return template('html/inicio.tpl')

@route('/inicio',method="post")
def inicio2():
    para1=str(request.forms.get('nombre'))
    para2=str(request.forms.get('tipo'))
    return """<h1>%s %s</h1>"""%(para1,para2)

@route('/file /<filepath:path>')
def server_static(filepath):
    return static_file(filepath,root='html/style')

run(host='0.0.0.0', port=8081, debug=True)
