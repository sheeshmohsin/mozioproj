from __future__ import unicode_literals

import uuid

from django.contrib.gis.db import models

# Create your models here.

unit_srid = 4326

class Provider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    language = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    
    def __unicode__(self):
        return self.name

class ServiceAreas(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    geom = models.PolygonField(srid=unit_srid)
    objects = models.GeoManager()

    def __unicode__(self):
        return "Unit %s" % (self.name)
