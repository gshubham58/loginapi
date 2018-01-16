from django.db import models
class Detail(models.Model):
    username=models.CharField(max_length=120,primary_key=True)
    password=models.CharField(max_length=100)
    def __str__(self):
        return (self.username)
