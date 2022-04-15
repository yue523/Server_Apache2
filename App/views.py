from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

'''

from django.views import generic

class IndexViews(generic.TemplateView):
    template_name="index.html"
'''