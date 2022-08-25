from django.db import models
from django.utils.translation import gettext_lazy as _


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, null=True)
    #publisher_id = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True)
    year = models.IntegerField(null=True)
    part = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)
    #table_of_content = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Cover(models.Model):
    class Size(models.TextChoices):
        SMALL = 'sm', _('Small')
        MEDIUM = 'md', _('Medium')
        LARGE = 'lg', _('Large')
        EXTRALARGE = 'xl', _('ExtraLarge')

    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=Size.choices, default=Size.EXTRALARGE)
    link = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)


class Genre(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
