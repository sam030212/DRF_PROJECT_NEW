from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    def _str_(self):
        return self.name