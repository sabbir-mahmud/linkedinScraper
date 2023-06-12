from django.contrib import admin
from django.urls import path

from scraper.views import scrape_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape_profile)
]
