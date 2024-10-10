from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Machinery  # Ensure your Machinery model is imported
from django.contrib.auth.decorators import login_required
from .models import Machinery, Booking
from .forms import BookingForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



class MachineryListView(ListView):
    model = Machinery
    template_name = 'users/machinery_list.html'  # Specify the template to use
    context_object_name = 'machinery_list'  # Use this in the template to reference the list

class MachineryDetailView(DetailView):
    model = Machinery
    template_name = 'users/machinery_detail.html'  # Specify the template to use
    context_object_name = 'machinery'  # Use this in the template to reference the machinery object

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Replace 'booking_success' with your desired redirect path.
    else:
        form = BookingForm()
    
    return render(request, 'users/create_booking.html', {'form': form})
def profile(request):
    return render(request, 'users/profile.html')  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the user's profile or any other page after login
                return redirect('user_profile')  # Replace with the name of your profile URL
            else:
                # Add an error message if authentication fails
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the name of your login page URL pattern.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL pattern.
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


