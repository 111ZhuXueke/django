from django.db import models
from abc import ABCMeta,abstractmethod,abstractproperty

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



class Animal(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name;

    @abstractmethod
    def run(self):
        print(self.name + " is run")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name

