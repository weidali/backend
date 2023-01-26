from django.db import models
from ckeditor.fields import RichTextField

from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=256, blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title
