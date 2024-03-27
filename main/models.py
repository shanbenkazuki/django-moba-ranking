from django.db import models

# Create your models here.
class Hero(models.Model):
    ROLE_CHOICES = [
        ('Support', 'Support'),
        ('Fighter', 'Fighter'),
        ('Tank', 'Tank'),
        ('Assassin', 'Assassin'),
        ('Mage', 'Mage'),
        ('Marksman', 'Marksman'),
    ]

    name_jp = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image_url = models.URLField()
    article_url = models.URLField()

    def __str__(self):
        return self.name_en