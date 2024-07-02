from django.http import JsonResponse, HttpRequest
import requests
from ipware import get_client_ip

def get_weather(request: HttpRequest):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip, is_routable = get_client_ip(request)
    location = get_location(client_ip)
    temperature = get_temperature(location)
    greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}."
    data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': greeting,
    }
    return JsonResponse(data)

def get_location_view(request: HttpRequest):
    client_ip, is_routable = get_client_ip(request)
    location = get_location(client_ip)
    message = f"This is your IP ({client_ip}) and your city is {location}."
    data = {
        'client_ip': client_ip,
        'location': location,
        'message': message,
    }
    return JsonResponse(data)

def get_location(ip: str) -> str:
    access_token = '78925fc3f875af'  # Your IPinfo access token
    url = f"https://ipinfo.io/{ip}/json?token={access_token}"
    response = requests.get(url)
    data = response.json()
    return data.get('city', 'Unknown')  # Use 'Unknown' if 'city' key is not present

def get_temperature(location: str) -> str:
    if location == 'Unknown':
        return 'error'
    api_key =  api_key = '63af0f513fc9af819af5def04505c748' # Your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'main' in data:
            return str(data['main']['temp'])
    return 'error'

api_key = '63af0f513fc9af819af5def04505c748' 
access_token = '78925fc3f875af' 
