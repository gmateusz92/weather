from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=b4b82500101d2170ffdaaec273c5cc54').read() #zawiera wszystki pliki JSON z API
        list_of_data = json.loads(source) #importuje wszystki pliki JSON z adresu source
        data = {
             "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    return render(request, 'weather/index.html', data)

