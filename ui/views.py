from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

def index(request):
    return render(request, 'ui/index.html', {
        'box_sizes': range(1, 51),
        'borders': range(1, 21)
    })

def privacy(request):
    return render(request, 'ui/privacy.html')

def cookies(request):
    return render(request, 'ui/cookies.html')
