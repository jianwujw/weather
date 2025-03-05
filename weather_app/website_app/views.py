from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
from django.conf import settings
import datetime

# Create your views here.
def weather():
    api_key = settings.API_KEY
    cities = ['Los Angeles','Denver','San Diego', 'New York City', 'Dallas','Miami','Portland', 'San Francisco','Houston','Seattle']
    dictionary = {}
    for city in cities:
        try:
            lon_lat_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(lon_lat_url)
            lon_lat_data = response.json()
            sunrise = lon_lat_data['sys']['sunrise'] 
            sunrise_formatted = datetime.datetime.fromtimestamp(sunrise).strftime('%I:%M %p')

            sunset = lon_lat_data['sys']['sunset'] 
            sunset_formatted = datetime.datetime.fromtimestamp(sunset).strftime('%I:%M %p')
            label = ""
            if lon_lat_data['timezone'] == -28800:
                label = "PDT"
            else:
                label = "PST"
            weather_conditions= []
            for condition in lon_lat_data['weather']:
                weather_conditions.append({
                    'main':condition['main'],
                    'description':condition['description'],
                    'icon':condition['icon'] #http://openweathermap.org/img/wn/{weather_icon}.png
                })
            dictionary[city]= {
                'city': lon_lat_data['name'],
                'sys_country': lon_lat_data['sys']['country'],
                'weather_conditions':weather_conditions, #api returns list so need to parse all of the list and return all the conditions
                'main_temp': round(((lon_lat_data['main']['temp'])-273.15)*9/5 + 32),
                'main_temp_min': round(((lon_lat_data['main']['temp_min'])-273.15)*9/5 + 32),
                'main_temp_max': round(((lon_lat_data['main']['temp_max'])-273.15)*9/5 + 32),
                'sys_sunrise': sunrise_formatted,
                'sys_sunset': sunset_formatted,
                'label': label,
            }
            #print(dictionary)
        except requests.exceptions.RequestException as e:
            # Handle exceptions raised during the request
            print(f'Error during API request: {e}')
        except KeyError as e:
            # Handle exceptions related to missing keys in the JSON response
            print(f'Error accessing JSON data: {e}')
        except ValueError as e:
            # Handle exceptions related to JSON parsing errors
            print(f'Error parsing JSON: {e}')
        except Exception as e:
            # Handle other unexpected exceptions
            print(f'Unexpected error: {e}')
    return dictionary
def index(request):
    dictionary = weather()
    return render(request,'index.html',{'dictionary':dictionary})

# def log(request):
#     return render(request,'login.html')

# def authenticate_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
    
#         user = authenticate(username = username, password = password)

 
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})

# def register(request):
#     return render(request,'register.html')
    
# def authenticate_register(request):
#     if request.method == 'POST':

#         username = request.POST['username']
#         password = request.POST['password']

#     if len(username) < 5:
#         return render(request,'register.html',{'error': 'Username is too short'})


#     #check db for user
#     if User.objects.filter(username = username).exists():
#         return render(request, 'register.html', {'error': 'Existing Username'})
        
#     else:
#         try:
#             user = User.objects.create_user(username=username,password=password)
#             user.save()
#         except ValueError:
#             return render(request, 'register.html',{'error': 'Not a valid Username'})

#         return redirect('/log/')


    