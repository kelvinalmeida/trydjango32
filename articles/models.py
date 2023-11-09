from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=69)
    content = models.TextField(blank=False, null=False)