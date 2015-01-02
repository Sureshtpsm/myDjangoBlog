from django.db import models

# Create your models here.
class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.CharField(max_length=600)
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title,self.post_content


class Comments(models.Model):
    post = models.ForeignKey(Posts)
    comments = models.CharField(max_length=600)
    comments_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comments