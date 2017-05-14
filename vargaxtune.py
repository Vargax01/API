# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect
import requests
from sys import argv
import json
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
        redirect("/error")

@route('/album/<para1>')
def album(para1):
    payload={"term":para1,"media":"music","country":"ES","entity":"album"}
    r=requests.get('https://itunes.apple.com/search',params=payload)
    js=json.loads(r.text)
    listacodigo=[]
    listalbum=[]
    for album in js["results"]:
        if album["collectionType"] == "Album" and album["collectionId"] not in listacodigo:
            diccio={"album":album["collectionName"],"imagen":album["artworkUrl100"],"codigo":album["collectionId"],"artista":album["artistName"]}
            listalbum.append(diccio)
    return template('html/albumes.tpl',listalbum=listalbum,album1=para1)

@route('/canciones/<codigo>')
def canciones(codigo):
    payload={"id":codigo,"entity":"song","country":"ES"}
    req=requests.get('https://itunes.apple.com/lookup',params=payload)
    js2=json.loads(req.text)
    nomalbum=js2["results"][0]["collectionName"]
    img=js2["results"][0]["artworkUrl100"]
    listacanc=[]
    for cancion in js2["results"]:
        if cancion.has_key("kind"):
            candiccio={"codigo":cancion["trackId"],"nombre":cancion["trackName"],"artista":cancion["artistName"],"media":cancion["previewUrl"]}
            listacanc.append(candiccio)
    return template('html/canciones.tpl',nomalbum=nomalbum,img=img,listacanc=listacanc)

@route('/correo/<codigocan>',method="get")
def correo(codigocan):
    return template('html/correo.tpl',codigocan=codigocan)

@route('/correo/<codigocan>',method="post")
def correo2(codigocan):
    correo=str(request.forms.get('correo'))
    return """<h1>%s para %s</h1>"""%(codigocan,correo)

@route('/artista/<para1>')
def artista(para1):
    return """<h1>Has elegido categoria artista con artista: %s</h1>"""%(para1)

@route('/music/<para1>')
def music(para1):
    return """<h1>Has elegido categoria musica con musica: %s</h1>"""%(para1)

@route('/error')
def error():
    return """<h1>Categoría no Válida</h1>"""

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath,root='html/style')

#run(host='0.0.0.0', port=argv[1])
run(host='0.0.0.0', port=8081, debug=True)
