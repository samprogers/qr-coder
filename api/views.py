from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.http import FileResponse
from api.modules import qr
import qrcode
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.
def generate(request):
    validate = URLValidator()
    url = request.GET.get('url')

    try:
        validate(url)
    except ValidationError as e:
        return JsonResponse({'error': 'Invalid URL'}, status=400)

    qr_path = qr.qrFromUrl(url)
    image = open(qr_path, "rb")
    response = HttpResponse(image, content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename=qrcode.png'
    return response
