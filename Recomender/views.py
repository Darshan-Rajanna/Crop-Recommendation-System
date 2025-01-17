from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import LoginView
from .forms import SignUpForm, CropRecommendationForm
from .models import CropHistory
import pickle

# Load the model
with open('C:/Users/admin/OneDrive/Desktop/New/myenv/CropRecomendation/Recomender/RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

def index(request):
    return render(request, 'Recomender/index.html' )

# def home(request):
#     return render(request, 'Recomender/home.html' )

def about(request):
    return render(request, 'Recomender/about_us.html' )

def recommend_crop(request):
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            user_data = [instance.N, instance.P, instance.K, instance.temperature, instance.humidity, instance.ph, instance.rainfall]
            predicted_crop = model.predict([user_data])[0]
            instance.recommended_crop = predicted_crop
            instance.save()
            return render(request, 'Recomender/recommendation_result.html', {'predicted_crop': predicted_crop})
    else:
        form = CropRecommendationForm()
    return render(request, 'Recomender/recommend_crop.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CropRecommendationForm
from .models import CropHistory

# Load the model
with open('C:/Users/admin/OneDrive/Desktop/New/myenv/CropRecomendation/Recomender/RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

def index(request):
    return render(request, 'Recomender/index.html' )

def about(request):
    return render(request, 'Recomender/about_us.html' )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'Recomender/signup.html', {'form': form})

@login_required
def recommend_crop(request):
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            user_data = [instance.N, instance.P, instance.K, instance.temperature, instance.humidity, instance.ph, instance.rainfall]
            predicted_crop = model.predict([user_data])[0]
            instance.recommended_crop = predicted_crop
            instance.save()
            return redirect('history')
    else:
        form = CropRecommendationForm()
    return render(request, 'Recomender/recommend_crop.html', {'form': form})

@login_required
def history(request):
    recommendations = CropHistory.objects.filter(user=request.user)
    return render(request, 'Recomender/history.html', {'recommendations': recommendations})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a homepage or dashboard after login
    else:
        form = LoginForm()
    return render(request, 'Recomender/login.html', {'form': form})
