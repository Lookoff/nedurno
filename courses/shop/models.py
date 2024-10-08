from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    watches_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.title