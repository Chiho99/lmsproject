from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import LmsModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # error handling
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'}) 
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

@login_required #decorator
def listfunc(request):
    object_list = LmsModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def goalfunc(request):
    return render(request, 'goal.html')

# class LmsStart(CreateView):
#     template_name = 'start.html'
#     model = LmsModel
#     fields = ('date','start',)
#     success_url = reverse_lazy('list')

class LmsFinish(CreateView):
    template_name = 'finish.html'
    model = LmsModel
    fields = ('memo',)
    success_url = reverse_lazy('list')

class LmsDelete(DeleteView):
    template_name = 'lmsmodel_confirm_delete.html'
    model = LmsModel
    success_url = reverse_lazy('list')