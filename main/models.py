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

    name_jp = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image_url = models.URLField()
    article_url = models.URLField()

    def __str__(self):
        return self.name_en

class HeroMetaData(models.Model):
    name = models.TextField()
    win_rate = models.FloatField()
    pick_rate = models.FloatField()
    ban_rate = models.FloatField()
    reference_date = models.DateField()
    rank_level = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('name', 'rank_level', 'reference_date'),)
