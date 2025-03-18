from django.urls import path

from ui import views

urlpatterns = [
    path("privacy", views.privacy, name="privacy"),
    path("cookies", views.cookies, name="cookies")
]
