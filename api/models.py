from django.db import models
from django.utils import timezone


class Topics(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    published_date = models.TextField(null=True)
    author = models.TextField(null=True)
    topic_url = models.TextField(null=True)
    image_url = models.TextField(null=True)
    top_news = models.CharField(max_length=8, null=True)
    domain_tags = models.TextField()
    sentimental = models.TextField(null=True)

    def publish(self):
        self.upload_date = timezone.now()

        self.save()

    def __str__(self):
        return self.title

    def __str__(self):
        return self.description

    def __str__(self):
        return self.published_date

    def __str__(self):
        return self.author

    def __str__(self):
        return self.image_url

    def __str__(self):
        return self.domain_tags

    def __str__(self):
        return self.sentimental


class Bookmark(models.Model):
      username = models.TextField(null=True)
      title = models.TextField(null=True)
      description = models.TextField(null=True)
      published_date = models.TextField(null=True)
      author = models.TextField(null=True)
      topic_url = models.TextField(null=True)
      image_url = models.TextField(null=True)
      sentimental = models.TextField(null=True)


# Create your models here.
