from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'login_reg/index.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'login_reg/success.html')
        else:
            return render(request, 'login_reg/index.html', {'error':'Passwords don\'t match!'})
    else:
        return render(request, 'login_reg/index.html')
def loginview(request):
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return render(request, 'login_reg/success.html')
            else:
                return render(request, 'login_reg/loggedin.html', {'error':'Passwords don\'t match!'})
        else:
            return render(request, 'login_reg/loggedin.html')
