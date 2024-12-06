from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
