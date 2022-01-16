from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    """
    Stores a single project entry, related to :model:`project.Project`.
    """
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    repository_link = models.URLField(max_length=200)
    priority_order = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0, 'Priority must be between 0 and 20'),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.title
