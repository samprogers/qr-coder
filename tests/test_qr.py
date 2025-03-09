from django.test import Client


def test_get_url_qr():
    client = Client()
    response = client.get("/api/generate?url=https://www.google.com")
    assert response.status_code == 200
