from django.db import models
from django.contrib.auth.models import User  

class Blogs(models.Model):
    title=models.CharField(max_length=255,blank=False )
    subtitle=models.CharField(max_length=255,blank=False,null=False )
    description=models.TextField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1) #yo chai user xaina vane tesko blog pani huna vayena ni ta so 
    created_at=models.DateTimeField(auto_now_add=True)
