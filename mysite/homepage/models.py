from django.db import models
from enum import Enum


# Create your models here.
class Questionbase(models.Model):
    tagChoice=(
    ("Math","Mathematics"),("Eng","English")
    )
    question=models.TextField()
    answer=models.TextField()
    tag=models.CharField(max_length=20,choices=tagChoice,default="Math")
    def __str__(self):
        return "Question #{}".format(self.id)
