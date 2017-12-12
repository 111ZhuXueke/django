from django.db import models

# Create your models here.
from django.db import models

class users(models.Model):
    name = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50, default="China")  # address属性，字段

    # class Meta:
    #     app_label = 'demo1'
    def __str__(self):
        return self.id + self.name + self.address

class info(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name