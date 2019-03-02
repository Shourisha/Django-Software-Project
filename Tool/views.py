# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from resources import Histogram

# Create your views here.
def index(req):
    if req.method == "POST":
        data = Histogram.hist(req.POST.get("data", ""))
        print data
        context = {"data" : data}
        return render(req, "display.html", context)
    else:
        return render(req, "index.html")

