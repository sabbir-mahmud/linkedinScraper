# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from .models import Profile


def scrape_linkedin_profile(url):
    options = Options()
    options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    name_element = soup.find(
        "h1", class_="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0")
    name = name_element.get_text(strip=True) if name_element else ""
    Profile.objects.create(name=name)

    driver.quit()


def scrape_profile(request):
    if request.method == 'POST':
        # Assuming you have a form field with name 'url'
        url = request.POST.get('url')
        scrape_linkedin_profile(url)
        return render(request, 'scrape_success.html')
    return render(request, 'scrape_profile.html')
