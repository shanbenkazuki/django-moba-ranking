from django.shortcuts import render
from .models import Hero

# Create your views here.
def hero_list(request):
    heroes = Hero.objects.all().values_list('name_jp', flat=True)
    context = {
        'heroes': heroes
    }
    return render(request, 'main/hero_list.html', context)