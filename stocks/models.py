from django.db import models

# Create your models here.

class Stock(models.Model):
    name_tag = models.CharField(max_length=20)
    chart_img = models.ImageField(upload_to='media/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_tag
