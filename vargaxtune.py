# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect

@route('/inicio',method="get")
@route('/')
def inicio():
    return template('html/inicio.tpl')

@route('/inicio',method="post")
def inicio2():
    para1=str(request.forms.get('nombre'))
    para2=str(request.forms.get('tipo'))
    if para2 == "cancion":
        redirect("/music/%s"%(para1))
    elif para2 == "artista":
        redirect("/artista/%s"%(para1))
    elif para2 == "album":
        redirect("/album/%s"%(para1))
    else:
        redirect("/error/%s"%(para1))

@route('/album/<para1>')
def album(para1):
    return """<h1>Has elegido categoria album con album: %s</h1>"""%(para1)

@route('/artista/<para1>')
def artista(para1):
    return """<h1>Has elegido categoria artista con artista: %s</h1>"""%(para1)

@route('/music/<para1>')
def music(para1):
    return """<h1>Has elegido categoria musica con musica: %s</h1>"""%(para1)

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath,root='html/style')


run(host='0.0.0.0', port=8081, debug=True)
