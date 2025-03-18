import qrcode

def qrFromUrl(request):
    url = request.GET.get('url')
    box_size = request.GET.get('box_size')
    border_size = request.GET.get('border_size')

    qr = qrcode.QRCode(version=3, box_size=box_size, border=border_size, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make()

    img = qr.make_image(Fit=True)
    img.save('/tmp/generated.png')
    return '/tmp/generated.png'
