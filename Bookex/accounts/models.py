# account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    phonenumber = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)


class Exchange(models.Model):
    thebook = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book', default=None)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrower_exchanges')
    lender = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField(editable=False)

