# -*- coding: utf-8 -*-
from bottle import route, run, request, redirect, template, static_file
import json
import requests

@route('/inicio')
@route('/')
def inicio():
    return """<h1>Hola