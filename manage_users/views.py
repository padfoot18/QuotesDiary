from django.shortcuts import render, redirect
from manage_users import my_forms
from manage_users.models import User


def login(request):
    if request.method == 'POST':
        loginform = my_forms.LoginForm(request.POST, auto_id='my-forms-%s')
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            user = User.objects.filter(username=username)
            if user.exists():
                user = user.get()
                if user.password == loginform.cleaned_data['password']:
                    request.session['username'] = username
                    return redirect('/')
    else:
        loginform = my_forms.LoginForm(auto_id='my-forms-%s')
    return render(request, 'my_form.html',
                  context={'form': loginform.as_p, 'local_css': ['css/myforms.css', ], 'type': 'login'})


def signup(request):
    if request.method == 'POST':
        signupform = my_forms.SignupForm(request.POST, auto_id='my-forms-%s')
        if signupform.is_valid():
            username = signupform.cleaned_data['username']
            password = signupform.cleaned_data['password']
            first_name = signupform.cleaned_data['first_name']
            last_name = signupform.cleaned_data['last_name']
            user = User(username, password, first_name, last_name)
            user.save()
            return redirect('/user/login/')
    else:
        signupform = my_forms.SignupForm(auto_id='my-forms-%s')
    return render(request, 'my_form.html',
                  context={'form': signupform.as_p, 'local_css': ['css/myforms.css', ], 'type': 'signup'})


def logout(request):
    request.session.pop('username')
    return redirect('/user/login/')
