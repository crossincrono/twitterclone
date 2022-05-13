
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    
    name = models.CharField(
        'Name' , blank=False, null=False, max_length=140, db_index=True, default='Annoymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Create DateTime', blank=True, auto_now_add=True
    )
    image= CloudinaryField('image',blank=True, db_index=True)

    def __str__(self):
        return self.name

    likes= models.PositiveBigIntegerField(
        'like',default=0, db_index=True, blank=True
    )