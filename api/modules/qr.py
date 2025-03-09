import qrcode

def qrFromUrl(url: str):
    qr = qrcode.QRCode(version=15, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=False)

    img = qr.make_image()
    img.save('/var/task/qr-coder/generated.png')
    return '/var/task/qr-coder/generated.png'