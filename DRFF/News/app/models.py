from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='product/', blank=True, null=True)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='news/', blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    email = models.EmailField()
    age = models.IntegerField()
    username = models.CharField(max_length=20)
    sms = models.CharField(max_length=10)

    def __str__(self):
        return self.email


class NewAccount(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.username

class Money(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Advertsiment(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    photo = models.ImageField(upload_to='advertsiment', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    discount = models.IntegerField()

    def __str__(self):
        return self.title

class Sale(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    sale = models.IntegerField()

    def __str__(self):
        return self.name






