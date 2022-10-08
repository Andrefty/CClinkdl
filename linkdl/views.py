from re import template
from sre_constants import SUCCESS
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views import generic
import requests
from .models import Link
from .forms import LinkForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'linkdl/index.html'
    context_object_name = 'latest_link_list'

    def get_queryset(self):
        """Return the last published questions."""
        return Link.objects.order_by('-id')

class DetailView(generic.DetailView):
    model = Link
    template_name = 'linkdl/detail.html'

class SubmitView(generic.CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'linkdl/submit.html'
    success_url = reverse_lazy('linkdl:index')
    def download_img(self,link,filename):
        r = requests.get(link)
        response = HttpResponse(r.content, content_type='image/jpeg',)
        # response['Content-Length'] = os.path.getsize(r.content)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename 
        return response
    def form_valid(self, form):
        link = form.cleaned_data['link']
        filename = form.cleaned_data['filename']
        super().form_valid(form)
        return self.download_img(link,filename)#super().form_valid(form)
# def index(request):
#     latest_link_list = Link.objects.all()[:5]
#     context = {
#         'latest_link_list': latest_link_list,
#     }
#     return render(request, 'linkdl/index.html', context)
# def detail(request, link_id):
#     link = get_object_or_404(Link,pk=link_id)
#     return render(request, 'linkdl/detail.html', {'link': link})
# def submit(request):
#     return HttpResponse("You're submitting a link.")
