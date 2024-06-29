from django.shortcuts import render
import requests
from datetime import datetime, timezone, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from .models import Profile

def index(request):
    api_key = '1159e40c585eda94f896a0c6087aece2'
    city = request.GET.get('city', 'London')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        timezone_offset = data['timezone']
        local_time = datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'air_condition': data['main']['pressure'],
            'timezone': data['timezone'] // 3600,  # Convert seconds to hours
            'date': local_time,
            'local_time': local_time.strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        weather = {
            'city': city,
            'temperature': 'N/A',
            'humidity': 'N/A',
            'description': 'City not found',
            'air_condition':'N/A',
            'icon': '',
            'date': 'N/A',
            'timezone': 'N/A',
            'local_time': 'N/A'
        }
    return render(request, 'weather.html', {'weather': weather})

######################################## Weather #########

def hello(request):
    return render(request,'hello.html')

######################################## Hello ##########

def news(request):
    api_key = '73d5fb0573f14a21ab273d5951ac63ce'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render(request, 'news.html', {'articles': articles})

################################################################# NEWS ########

def home(request):
    return render(request,'base.html')
#####################################################################

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            Profile.objects.create(name=name,dob = dob, phone_number=phone_number, email=email, password=password).save()
            return redirect('success')  # Redirect to success page after registration
    else:
        form = SignUpForm()

    return render(request, 'signup.html',{'form':form})
                  
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})