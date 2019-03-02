# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    Name            = models.CharField(max_length=250)
    Budget          = models.IntegerField()
    Workers         = models.ManyToManyField('Worker', blank = True)

    def __str__(self):
        return self.Name + " - " + str(self.Budget)

    def to_url(self):
        ret = str(self.Name.replace(" ", "_"))
        return ret

    def to_name(self):
        ret = str(self.to_url().replace("_", " "))
        return ret


class Worker(models.Model):
    Firstname       = models.CharField(max_length=100)
    Lastname        = models.CharField(max_length=100)
    Age             = models.IntegerField()
    Project         = models.ForeignKey(Project, blank=True, null=True)
    Full_name       = str(Firstname) + " " + str(Lastname)

    def __str__(self):
        return self.Firstname + " " + self.Lastname + ", " + str(self.Age) + " years old"

    def to_url(self):
        firstname = self.Firstname.replace(" ", "_")
        ret = str(firstname) + "_" + str(self.Lastname)
        return ret


