from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm,UserRegistrationForm
from django.urls import reverse_lazy
from .models import UserModel
from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from RecipeModel.models import Recipe
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['usernames'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated successfully')
                    return render(request, 'userModel/dashboard.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'userModel/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('userModel/login.html')
    #return render(request, 'userModel/login.html')
    # Redirect to a success page.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the User object
            new_user.save()
            return render(request, 'userModel/register_done.html',
                          {'new_user': new_user})
        else:
            return render(request, 'userModel/register.html',
                          {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'userModel/register.html',
                      {'user_form': user_form})



@login_required
def dashboard(request):
    user = User.objects.filter(email=request.user.email)
    return render(request, 'userModel/dashboard.html', {'user':user})

@login_required
def user_email_detail(request,email):
    user = get_object_or_404(get_user_model(), email=email, is_active=True)
    if Recipe.objects.filter(user=user).exists():
        try:
            recipe = Recipe.objects.filter(user=user)
        except ObjectDoesNotExist:
            return HttpResponse('The entry doesn\'t exist.')
        return render(request, 'userModel/detail.html',{'user': user,'recipe': recipe})
    else:
        return HttpResponse('The entry doesn\'t exist.')
        #return render(request, 'userModel/detail.html',{'user': user})
