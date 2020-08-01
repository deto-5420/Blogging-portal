from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE ,default=1)

def __str__(self):
    return self.title


#def get_absolute_url(self):
#        return reverse('post-detail', kwargs={'pk': self.pk})  
