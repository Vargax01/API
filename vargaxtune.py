# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect
import requests
from sys import argv
import json
import sendgrid
import os
from sendgrid.helpers.mail import *
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
    payload={"id":codigocan,"country":"ES"}
    req=requests.get('https://itunes.apple.com/lookup',params=payload)
    js=json.loads(req.text)
    cancion=js["results"][0]["trackName"]
    album=js["results"][0]["collectionName"]
    artista=js["results"][0]["artistName"]
    imagen=js["results"][0]["artworkUrl100"]
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("miguelchico14@gmail.com")
    subject = "Cancion que me ha gustado desde VargaxTune"
    to_email = Email(correo)
    content = Content("text/html","""<html><body><img src='http://apivargax.herokuapp.com/style/images/vargaxtunepeque.png' /><br><h1>Me ha gustado la cancion %s</h1><br><h2>Album: %s</h2><br><h2>Artista: %s</h2><br><img src=%s /></body></html>"""%(cancion,album,artista,imagen))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return template('html/correoenviado.tpl')

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
