from django.shortcuts import render
import requests
import datetime

appid = '2e966663bf20f96321e32ce20eebb027'

def index(request):
    # Get city from the POST request or set a default value
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Toshkent'
    # Prepare the URL and parameters for the API request
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': appid, 'units': 'metric'}
    
    # Make the request to the OpenWeather API
    r = requests.get(url=url, params=params)
    
    # Check if the city is found (status code 200 means success)
    if r.status_code == 200:
        res = r.json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temp = res['main']['temp']
        day = datetime.date.today()
        
        # Prepare weather data to send to the template
        weather = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'error': "You made a mistake. The city was not found. Please try again." # No error
        }
    else:
        # If the city is not found, set an error message
        weather = {
            'description': None,
            'icon': None,
            'temp': "You did a mistake!",
            'day': "You did a mistake!",
            'city': city,
            'error': "You made a mistake. The city was not found. Please try again."
        }
    
    # Render the template with the weather or error message
    return render(request, 'obihavoapp/index.html', weather)

#2
# def index(request):
#     warning = None  # Initialize warning message

#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'Toshkent'

#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'appid': appid, 'units': 'metric'}

#     r = requests.get(url=url, params=params)
#     res = r.json()
    
#     # Check if the API response contains an error (like "city not found")
#     if r.status_code == 200:
#         description = res['weather'][0]['description']
#         icon = res['weather'][0]['icon']
#         temp = res['main']['temp']
#         day = datetime.date.today()
#         weather = {
#             'description': description,
#             'icon': icon,
#             'temp': temp,
#             'day': day,
#             'city': city
#         }
#     else:
#         # If the city is not found, set a warning message
#         warning = "City not found. Please enter a valid city name."
#         weather = {}

#     return render(request, 'obihavoapp/index.html', weather)

#3
# def index(request):

#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'Toshkent'
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'appid': appid, 'units': 'metric'}
#     r = requests.get(url=url, params=params)
#     res = r.json()
#     description = res['weather'][0]['description']
#     icon = res['weather'][0]['icon']
#     temp = res['main']['temp']
#     day = datetime.date.today()
#     weather = {
#         'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city
#     }
#     return render(request, 'obihavoapp/index.html', weather)


