# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect
from sys import argv
import requests
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
    payload={"term":para1,"media":"music","country":"ES","enity":"album"}
    r=requests.get('https://itunes.apple.com/search',params=payload)
    js=json.loads(r.text)
    listacodigo=[]
    for i in js["results"]:
        if i["kind"] == "song" and i["collectionId"] not in listacodigo:
            listacodigo.append(i["collectionId"])
    listalbum=[]
    for album in listacodigo:
        payload2={"id":album,"country":"ES"}
        r1=requests.get('https://itunes.apple.com/lookup',params=payload2)
        js1=json.loads(r1.text)
        diccio={"album":js1["results"][0]["collectionName"],"imagen":js1["results"][0]["artworkUrl100"]}
        listalbum.append(diccio)
    return template('html/albumes.tpl',listalbum=listalbum)

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


run(host='0.0.0.0', port=argv[1])
