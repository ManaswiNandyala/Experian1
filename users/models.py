from django.db import models
import random

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    higher_education = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    user_id = models.CharField(max_length=6, unique=True, default=''.join([str(random.randint(0, 9)) for _ in range(6)]))
