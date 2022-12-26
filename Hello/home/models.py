from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField()

    def __str__(self):
        return self.name
