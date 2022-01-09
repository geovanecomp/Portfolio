from django.db import models

class Job(models.Model):
    """
    Stores a single job entry, related to :model:`blog.Blog`.
    """
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
