import os, re, datetime
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
    host = request.get_host()
    rsp = render(request, 'ui/robots.txt', {
        'host': host,
    })
    rsp.headers['Content-Type'] = 'text/plain'
    return rsp

def sitemap(request):
    host = request.get_host()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    last_modified = os.environ.get('SERVERLESS_LAST_MODIFIED') if os.environ.get('SERVERLESS_LAST_MODIFIED') is not None else now
    rsp = render(request, 'ui/sitemap.xml', {
        'host': host,
        'last_modified': last_modified

    })
    rsp.headers['Content-Type'] = 'application/xml'
    return rsp

def privacy(request):
    return render(request, 'ui/privacy.html')

def cookies(request):
    return render(request, 'ui/cookies.html')
