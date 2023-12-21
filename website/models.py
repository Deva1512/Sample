from django.db import models
from django.forms import ModelForm

class Login(models.Model):
    
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=30,null=False)
    password=models.CharField(max_length=20,null=False)


    class Meta:
        db_table='Login'


class Loginform(ModelForm):

    class Meta:
        models=Login
        fields=['name','email','password']


class Contact(models.Model):
    name = models.CharField(max_length=20,blank='False')
    email = models.EmailField(max_length=20,default='')
    contact = models.FloatField()
    subject = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=300,default='')
    status = models.CharField(max_length=300,default='')
    comment = models.CharField(max_length=300,default='')
    objects = models.Manager()

    class Meta:
        db_table = "contact"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'contact',
            'email',
            'subject',
            'message',
        ]








