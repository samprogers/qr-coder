from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

def index(request):
    return render(request, 'ui/index.html')
