from django.db import models

# Create your models here.

STATE_CHOICE = ((
    ('karnali', 'karnali'),
    ('Sudurpashchim', 'Sudurpashchim'),
    ('Lumbini', 'Lumbini'),
    ('Gandaki', 'Gandaki'),
    ('Bagmati', 'Bagmati'),
    ('Madhesh', 'Madhesh'),
    ('Koshi', 'Koshi'),
    
))


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=200)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', blank=True)
    docfile = models.FileField(upload_to='docfile', blank=True)