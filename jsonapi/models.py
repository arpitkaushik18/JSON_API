from django.db import models

class User(models.Model):
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

class ActivityPeriod(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
   start_time=models.DateTimeField()
   end_time=models.DateTimeField()
