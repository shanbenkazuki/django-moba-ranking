# Generated by Django 5.0.3 on 2024-03-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('win_rate', models.FloatField()),
                ('pick_rate', models.FloatField()),
                ('ban_rate', models.FloatField()),
                ('reference_date', models.DateField()),
                ('rank_level', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('name', 'rank_level', 'reference_date')},
            },
        ),
    ]
