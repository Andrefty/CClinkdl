from re import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Link
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'linkdl/index.html'
    context_object_name = 'latest_link_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Link.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Link
    template_name = 'linkdl/detail.html'
# def index(request):
#     latest_link_list = Link.objects.all()[:5]
#     context = {
#         'latest_link_list': latest_link_list,
#     }
#     return render(request, 'linkdl/index.html', context)
# def detail(request, link_id):
#     link = get_object_or_404(Link,pk=link_id)
#     return render(request, 'linkdl/detail.html', {'link': link})
def submit(request):
    return HttpResponse("You're submitting a link.")
