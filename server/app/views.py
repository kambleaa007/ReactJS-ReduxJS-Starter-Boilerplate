# -*- coding: utf-8 -*-
import json
import time
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseServerError
from django.conf import settings
from django.template import loader
from django.contrib.auth import logout
import requests
from six.moves.urllib.parse import urlparse

def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render({"dev": True}, request))


def healthCheck(request):
    return HttpResponse('success')


def todos(request):
    todos = [
        {"id": 1, "name": 'Find the meaning of life', "completed": True},
        {"id": 2, "name": 'Learn more about 6sense', "completed": False},
        {"id": 3, "name": 'Meditate', "completed": False},
        {"id": 4, "name": 'Take a barista class', "completed": False},
        {"id": 5, "name": 'Take a bartender class', "completed": True},
        {"id": 6, "name": 'Give to someone in need', "completed": True},
        {"id": 7, "name": 'laugh as much as possible', "completed": True},
        {"id": 8, "name": 'Tell Scott to follow pep8', "completed": True},
        {"id": 9, "name": 'Improve product', "completed": False},
        {"id": 10, "name": 'Zen', "completed": False},
        {"id": 11, "name": 'Finish food', "completed": False},
        {"id": 12, "name": 'Clean room', "completed": False},
        {"id": 13, "name": 'Dance', "completed": False},
        {"id": 14, "name": 'Find Dance Partner', "completed": False},
        {"id": 15, "name": 'Call Doctor', "completed": False},
        {"id": 16, "name": 'Call Dentist', "completed": False},
        {"id": 17, "name": 'Call Mom', "completed": False},
        {"id": 18, "name": 'Call Sister for birthday', "completed": False},
        {"id": 19, "name": 'Organize secure docs', "completed": False},
        {"id": 20, "name": 'Apply for jobs', "completed": False},
    ]
    return HttpResponse(json.dumps(todos))


def badrequest(request):
    return HttpResponseBadRequest(json.dumps({'error': 'not working'}))



def weather(request):
    weather = [
        {"coord":
        {"lon":-0.13,"lat":51.51},
        "weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],
        "base":"stations","main":
                {"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},
                "visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":
                        {"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},
                        "id":2643743,"name":"London","cod":200}
    ]
    return HttpResponse(json.dumps(weather))    


def mocks(request):
    mocks = [
        {"id": 1, "name": 'Find the meaning of life', "completed": True},
        {"id": 2, "name": 'Learn more about 6sense', "completed": False},
        {"id": 3, "name": 'Meditate', "completed": False},
        {"id": 4, "name": 'Take a barista class', "completed": False},
        {"id": 5, "name": 'Take a bartender class', "completed": True},
        {"id": 6, "name": 'Give to someone in need', "completed": True},
        {"id": 7, "name": 'laugh as much as possible', "completed": True},
        {"id": 8, "name": 'Tell Scott to follow pep8', "completed": True},
        {"id": 9, "name": 'Improve product', "completed": False},
        {"id": 10, "name": 'Zen', "completed": False},
        {"id": 11, "name": 'Finish food', "completed": False},
        {"id": 12, "name": 'Clean room', "completed": False},
        {"id": 13, "name": 'Dance', "completed": False},
        {"id": 14, "name": 'Find Dance Partner', "completed": False},
        {"id": 15, "name": 'Call Doctor', "completed": False},
        {"id": 16, "name": 'Call Dentist', "completed": False},
        {"id": 17, "name": 'Call Mom', "completed": False},
        {"id": 18, "name": 'Call Sister for birthday', "completed": False},
        {"id": 19, "name": 'Organize secure docs', "completed": False},
        {"id": 20, "name": 'Apply for jobs', "completed": False},
    ]
    return HttpResponse(json.dumps(mocks))  