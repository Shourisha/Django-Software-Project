# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from . import forms

from django.shortcuts import render
from . import models

# Create your views here.

def blog(req):
    context = {"blogs": models.Blog.objects.all()}
    return render(req, 'Blogindex.html', context)

def create(req):
    if req.method == "POST":
        f = forms.BlogForm(req.POST)
        if(f.is_valid()):
            f.save()
        return redirect("/Blog")
    else:
        f = forms.BlogForm()
        context = {"inputform" : f}
        return render(req, "create.html", context)