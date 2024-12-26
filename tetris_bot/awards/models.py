from django.db import models

class AwardBlog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='awards_image/')
    description = models.TextField()

    def __str__(self):
        return self.title
