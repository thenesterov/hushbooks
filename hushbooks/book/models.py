from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT)
    year = models.IntegerField()
    part = models.IntegerField()
    page_count = models.IntegerField()
    table_of_content = models.JSONField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)

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

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
