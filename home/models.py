from django.db import models
import uuid

# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(null=True,blank=True)
    is_published = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return f"{self.title} {self.author}"