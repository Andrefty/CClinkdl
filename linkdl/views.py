from re import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Link
# Create your views here.

def index(request):
    latest_link_list = Link.objects.all()[:5]
    context = {
        'latest_link_list': latest_link_list,
    }
    return render(request, 'linkdl/index.html', context)
def detail(request, link_id):
    link = get_object_or_404(Link,pk=link_id)
    return render(request, 'linkdl/detail.html', {'link': link})
def submit(request):
    return HttpResponse("You're submitting a link.")
