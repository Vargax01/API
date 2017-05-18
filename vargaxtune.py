# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect, get, response
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from sys import argv
import json
import sendgrid
import os
from sendgrid.helpers.mail import *

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "5lWOSvU6M66CrZTkOGTZJ0W8B"
CONSUMER_SECRET = "jHgZn8qW6QFJXYCjFZcX2fIsVkdkjl1NExRfKGX3mtrHNHqKE5"

TOKENS = {}

def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]

def get_access_token(TOKENS):
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
  r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
  credentials = parse_qs(r.content)
  TOKENS["access_token"] = credentials.get('oauth_token')[0]
  TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]


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
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('html/correo.tpl',codigocan=codigocan,authorize_url=authorize_url)

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
    sg = sendgrid.SendGridAPIClient(apikey=os.environ('SENDGRID_API_KEY'))
    from_email = Email("miguelchico14@gmail.com")
    subject = "Cancion que me ha gustado desde VargaxTune"
    to_email = Email(correo)
    content = Content("text/html","""<html><body><img src='http://apivargax.herokuapp.com/style/images/vargaxtunepeque.png' /><br><h1>Me ha gustado la cancion %s</h1><br><h2>Album: %s</h2><br><h2>Artista: %s</h2><br><img src=%s /></body></html>"""%(cancion,album,artista,imagen))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return template('html/correoenviado.tpl')

@get('/callback')
def get_verifier():
  TOKENS["request_token"]=request.get_cookie("request_token", secret='some-secret-key')
  TOKENS["request_token_secret"]=request.get_cookie("request_token_secret", secret='some-secret-key')
  TOKENS["verifier"] = request.query.oauth_verifier
  get_access_token(TOKENS)
  response.set_cookie("access_token", TOKENS["access_token"],secret='some-secret-key')
  response.set_cookie("access_token_secret", TOKENS["access_token_secret"],secret='some-secret-key')
  redirect('/twittear')

@get('/twittear')
def twittear():
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      print CONSUMER_KEY
      print CONSUMER_SECRET
      print TOKENS["access_token"]
      print TOKENS["access_token_secret"]
      oauth = OAuth1(CONSUMER_KEY,
                       client_secret=CONSUMER_SECRET,
                       resource_owner_key=TOKENS["access_token"],
                       resource_owner_secret=TOKENS["access_token_secret"])
      url = 'https://api.twitter.com/1.1/statuses/update.json'
      r = requests.post(url=url,
                          data={"status":"prueba de oauth1"},
                          auth=oauth)
      if r.status_code == 200:
        return "<p>Tweet properly sent</p>"
      else:
        return "<p>Unable to send tweet</p>"

@get('/twitter_logout')
def twitter_logout():
  response.set_cookie("access_token", '',max_age=0)
  response.set_cookie("access_token_secret", '',max_age=0)
  redirect('/inicio')

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
#run(host='0.0.0.0', port=8081, debug=True)
