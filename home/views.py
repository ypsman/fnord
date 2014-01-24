from django.shortcuts import render
from home.models import Newsartikel

def index(request):
    news = Newsartikel.objects.all().order_by('-pub_date')[:5]
    context = {'news' : news}
    return render(request, 'home/news.html', context)