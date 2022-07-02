from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Movie'

    class Meta:
        ordering = ["-pk"]
