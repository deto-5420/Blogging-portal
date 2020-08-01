from django.db import models
from django.contrib.auth.models import User
def yahaPer(instance,filename):
    return "profile_pics/{user}/{filename}".format(user=instance.user,filename=filename)
# Create your models her
class StatusModel(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    content=models.TextField()
    image= models.ImageField(default='profile_pics/default.jpg',upload_to=yahaPer)
    updated=models.DateTimeField( auto_now=True )
    timestamp=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
    