from django.shortcuts import render
from .models import Hero

# Create your views here.
def hero_ranking(request):
    heroes = Hero.objects.all().values_list('name_jp', 'image_url')
    context = {
        'heroes': heroes
    }
    return render(request, 'main/hero_ranking.html', context)