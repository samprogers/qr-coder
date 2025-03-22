from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string, get_template

def index(request):
    return render(request, 'ui/index.html', {
        'box_sizes': range(1, 51),
        'borders': range(1, 21)
    })
    
def robots(request):
    robots = open('static/ui/robots.txt', 'rb')
    return FileResponse(robots)

def privacy(request):
    return render(request, 'ui/privacy.html')

def cookies(request):
    return render(request, 'ui/cookies.html')
