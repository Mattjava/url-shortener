from django.db import models

# Create your models here.

class Link(models.Model):
    code = models.TextField(primary_key=True, null=False)
    url = models.TextField(null=False)
