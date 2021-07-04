from bulk_update_or_create import BulkUpdateOrCreateQuerySet

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Book(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    book_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=256, blank=True)
    authors = ArrayField(models.CharField(max_length=256), default=list, blank=True, null=True)
    published_date = models.DateField(null=True)
    categories = ArrayField(models.CharField(max_length=256), default=list, blank=True, null=True)
    average_rating = models.FloatField(null=True)
    ratings_count = models.PositiveIntegerField(null=True)
    thumbnail = models.URLField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book_id} - {self.title}'
