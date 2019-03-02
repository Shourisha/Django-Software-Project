# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, "homepage.html")


def projects(req):
    context = {"projects": models.Project.objects.all()}
    return render(req, "projects.html", context)

def worker(req):
    context = {"workers": models.Worker.objects.all()}
    return render(req, "workers.html", context)


def displaysingleworker(req, name):
    name = name.replace("_", " ")
    name = name.split(" ")

    context = {"worker": models.Worker.objects.get(Lastname=name[-1])}
    return render(req, "displaysingleworker.html", context)


def displaysingleproject(req, name):
    name = name.replace("_", " ")
    context = {"project": models.Project.objects.get(Name=name)}
    return render(req, "displaysingleproject.html", context)

