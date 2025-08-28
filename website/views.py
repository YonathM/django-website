from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News
# Create your views here.
def home(request):
    news_list = News.objects.filter(status='published').order_by('-published_date')
    paginator = Paginator(news_list, 3)  # Show 3 news items per page

    page_number = request.GET.get('page')
    news_items = paginator.get_page(page_number)

    return render(request, 'home.html', {'news_items': news_items})
def about (request):
    return render(request, 'about.html')
def events(request):
    return render(request, 'events.html')
def contact(request):
    return render(request, 'contact.html')
