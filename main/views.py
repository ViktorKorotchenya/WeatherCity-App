import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'cc399769634b089445b10da8fd6063ab'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'feels_like': res['main']['feels_like'],
            'pressure': res['main']['pressure'],
            'wind': res['wind']['speed'],
            'visibility': res['visibility'],
            'humidity': res['main']['humidity'],


        }
        print(res)
        all_cities.insert(0, city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'main/index.html', context)
