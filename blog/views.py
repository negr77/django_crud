from django.shortcuts import render
from .models import Mypost
from django.utils import timezone

def index(request):
    posts = Mypost.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)
# Create your views here.
