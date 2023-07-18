from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.


class Category (models.Model):
    title = models.CharField(name='title', max_length=100)
    decsciption = models.TextField(name='decsciption', max_length=500)
    created_at = models.DateTimeField(name="created_at", auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    def get_req(self):
        return [self, self.title, self.decsciption, self.pk]