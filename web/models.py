from django.db import models
from django.utils import timezone
from django.urls import reverse

class Shop(models.Model):
    name = models.CharField(max_length=100, unique=False)
    logo = models.TextField()
    owner = models.CharField(max_length=100, unique=False)
    location = models.CharField(max_length=100, unique=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('web-home')

class ForumPost(models.Model):
    title = models.CharField(max_length=100, unique=False)
    profile_picture = models.CharField(max_length=10000, unique=False)
    author = models.CharField(max_length=100, unique=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('web-forum')

class JobPost(models.Model):
    position = models.CharField(max_length=100, unique=False)
    shop = models.CharField(max_length=100, unique=False)
    logo = models.CharField(max_length=10000, unique=False)
    content = models.TextField()
    external_link = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_due = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.shop

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('web-vacancy')

class PromotionPost(models.Model):
    title = models.CharField(max_length=100, unique=False)
    logo = models.CharField(max_length=10000, unique=False)
    content = models.TextField()
    external_link = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_due = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('web-deals')