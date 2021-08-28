from django.db import models

# Create your models here.

class User(models.Model):
	product_name = models.CharField(max_length=50)
	volume = models.CharField(max_length=60)
	market_capital = models.CharField(max_length=50)
	credit_rating = models.CharField(max_length=40)