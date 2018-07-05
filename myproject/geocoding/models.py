from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    docfile = models.FileField(null = True, blank = True)

    def __str__(self):
        return str(self.title)

