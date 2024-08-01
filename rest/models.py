from django.db import models
from django.contrib.auth.models import User
class foods(models.Model) :
    name = models.TextField(max_length=100)
    desc = models.TextField(max_length=500)
    price = models.IntegerField(null='True')
    def __str__ (self):
        return self.name
class profile(models.Model) :
    usern = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ManyToManyField(foods ,blank='False')
    def __str__(self) :
        return str(self.usern)
class contact(models.Model) :
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    email = models.EmailField()
    desc = models.TextField(max_length=255)
    def __str__(self) :
        return str(self.username)