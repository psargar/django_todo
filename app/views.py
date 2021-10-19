from django.contrib.auth import authenticate, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required
from todo.settings import AUTH_PASSWORD_VALIDATORS

# Create your views here.


@login_required(login_url='login')
def home(request):
    form = TODOForm()
    user = request.user
    todos = TODO.objects.filter(user=user).order_by('priority')
    return render(request, 'index.html', context={'form' : form, 'todos' : todos})

    

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm(data=request.POST)
        context = {
        'form':form
        }
        return render(request, 'login.html',context= context)
    else:
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('/')
        else:
            context={
            'form':form
            }
            return render(request, 'login.html', context=context)


def signup(request):
    if request.method =='GET':
        form = UserCreationForm()
        context= {
        'form' : form
            }
        return render(request, 'signup.html', context=context)

    else:
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)
    
@login_required(login_url='login')
def add_todo(request):

    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('/')
        else:
             return render(request, 'index.html', context={'form': form})

def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect('/')

def status_todo(request, id, Status):
    todo = TODO.objects.get(pk = id)
    todo.Status=Status
    todo.save()
    return redirect('/')

@login_required(login_url='login')

def signout(request):
    logout(request)
    return redirect('login')
    