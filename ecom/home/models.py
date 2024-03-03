from django.db import models

# Create your models here.


class Task(models.Model):
    name=models.CharField(max_length=100,default="")
    is_completed=models.BooleanField(default=False)
    created_date=models.DateField(auto_now=True)
    completed_date=models.DateField(auto_now=True)

    

    def __str__(self):
        return self.name
    