# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import PatientForm, AddPatientForm
from django.contrib import messages
from .models import Patient

def homepage(request):
    return render(request, 'patient/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient:dashboard')
            else:
                return render(request, 'patient/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'patient/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('patient:homepage')

@login_required
def dashboard(request):
    return render(request, 'patient/doctor_dashboard.html')

@login_required
def doctor_reset_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        request.user.set_password(password)
        request.user.save()
        login(request, request.user)
        return redirect("patient:homepage")

    return render(request, "patient/reset_password.html")

def password_reset(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            # Redirect to a page where the user can set a new password
            return redirect("patient:password_reset_confirm", user_id=user.id)
        except User.DoesNotExist:
            return render(request, "patient/password_reset.html", {
                "error": "User does not exist"
            })

    return render(request, "patient/password_reset.html")

def password_reset_confirm(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        password = request.POST.get("password")
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("patient:homepage")

    return render(request, "patient/password_reset_confirm.html", {"user_id": user_id})

@login_required
def quick_add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patient:quick_add_patient')  # Redirect after successful POST
    else:
        form = PatientForm()
    
    return render(request, 'patient/quick_add_patient.html', {
        'form': form,
    })

def all_patients(request):
    data = Patient.objects.all().order_by('-id')
    return render(request, 'patient/all-patients.html',{
        "data": data,
    })

@login_required
def add_patient(request):
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patient:add-patient') 
    else:
        form = AddPatientForm()
    
    return render(request, 'patient/add-patient.html', {
        'form': form,
    })

@login_required
def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        form = AddPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patient:all-patients') 
    else:
        form = AddPatientForm(instance=patient)
    
    return render(request, 'patient/update-patient.html', {
        'form': form,
    })

@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully!')
    return redirect('patient:all-patients')
