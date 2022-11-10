from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from .forms import SignupForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.http import HttpResponse
from .models import *


def home(request):
    if 'username' in request.session:
        user = request.user
        name = user.first_name+' '+user.last_name
        user = request.user
        return render(request, 'main/home.html', {'name':name, 'user': user})
    else:
        return redirect('/')

def profile(request):
    if 'username' in request.session:
        context = {}
        profile = Profile.objects.get(name=request.user)
        fullname = profile.name.first_name +' '+ profile.name.last_name # Get first and last name from user model
        context = {'dataset': profile, 'fullname': fullname}
        return render(request, 'main/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            messages.success(request, 'Profile created. You can log in now!')    
            return redirect('login')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if 'username' in request.session:
        return redirect('home/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            messages.success(request, 'loggedin successfully')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    username = request.session.get('username')
    del username
    return render(request, 'accounts/logout.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            print(data)
            associated_users = ExtendUser.objects.filter(Q(email=data))
            
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password/password_reset.html", context={"password_reset_form": password_reset_form})
