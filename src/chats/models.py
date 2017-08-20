from django.db import models

# Create your models here.
class todoitem(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField()

    def __str__(self):
        return self.text
