from django.db import models

class ReviewReport(models.Model):
    name = models.TextField()
    book = models.FilePathField(path="tempXls")
    counter = models.IntegerField(default=0)

class Report(models.Model):
    book = models.TextField()

# Create your models here.
