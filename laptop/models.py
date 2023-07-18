from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.

class Laptop (models.Model):

    title = models.CharField(
        default=0,
        null=False,
        blank=False,
        name='title',
        max_length=50,
    )
    image = models.ImageField(
        null=False,
        blank=True,
        name='image',
        upload_to='images/', 
    )

    author = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        name='author',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'category.Category',
        null=False,
        blank=False,
        name='category',
        on_delete=models.CASCADE,
    )
    count = models.SmallIntegerField(
        default=0,
        null=False,
        blank=False,
        name='count',
    )
    price = models.DecimalField(
        null=False,
        blank=False,
        name='price',
        max_digits=10,
        decimal_places=2
    )
    color = models.CharField(
        null=False,
        blank=False,
        name='color',
        max_length=20,
    )
    led_panel = models.CharField(
        null=False,
        blank=False,
        name='led_panel',
        max_length=50,
    )
    processor = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        name='processor',
    )
    video_card = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        name='video_card',
    )
    memory = models.CharField(
        null=False,    
        blank=False,
        name='memory',
        max_length=10,
    )
    ram = models.CharField(
        name='ram',
        null=False,
        blank=False,
        max_length=200
    )
    keyboard = models.CharField(  
        null=False,
        blank=False,
        name='keyboard',
        max_length=200
    )
    battery = models.CharField(   
        null=False,
        blank=False,
        name='battery',
        max_length=200,
    )
    created_at = models.DateTimeField(name="created_at", auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    def get_req(self):
        return [self, self.title, self.price, self.image, self.category, self.pk]