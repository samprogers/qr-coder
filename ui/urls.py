from django.urls import path

from ui import views

urlpatterns = [
    path("", views.index, name="index"),
    path("robots.txt", views.robots, name="robots"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("privacy", views.privacy, name="privacy"),
    path("cookies", views.cookies, name="cookies")
]
