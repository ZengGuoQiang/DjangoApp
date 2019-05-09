from django.db import models
import uuid

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
    name = models.CharField(max_length=6, null=False)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now=True, null=False)

# Create your models here.
class Link(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length = 200)