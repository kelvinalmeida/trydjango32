from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def user_creation_view(request, *args, **kwargs):

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        return redirect('login')
    
    context = {
        "form": form
    }
    
    return render(request, "accounts/create.html", context)

def login_view(request):

    context = {}

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)   
        context['form'] = form
        
        # print(user)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../')
    else: 
        form = AuthenticationForm(request)
        context['form'] = form

    return render(request, 'accounts/login.html', context)


# def login_view(request):
#     # print(request.GET)
#     # print(request.GET.get('next'))
#     # if request.GET.get('next') is not None:
#     #     print('entrei')

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is None:
#             context = {
#                 'error': 'username or password is incorrect!'
#             }
#             return render(request, 'accounts/login.html', context)
        
#         # print(user)
#         login(request, user)
#         return redirect('../')

#     return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html', {})

