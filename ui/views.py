import re
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponsePermanentRedirect
from django.template.loader import render_to_string, get_template
from django.conf import settings

def index(request):
    host = request.get_host()

    #always redirect to apex domain without www
    if re.search('www', host, re.IGNORECASE):
        return HttpResponsePermanentRedirect('https://' + settings.BASE_URL)

    return render(request, 'ui/index.html', {
        'box_sizes': range(1, 51),
        'borders': range(1, 21),
        'host': host,
        'description': 'Free QR code generator',
        'title': 'Absolutely Free QR Generator',
        'site_name': 'Free QR Code Generator'
    })

def robots(request):
    robots = open("/var/task/ui/static/ui/robots.txt", 'rb')
    return FileResponse(robots)

def privacy(request):
    return render(request, 'ui/privacy.html')

def cookies(request):
    return render(request, 'ui/cookies.html')
