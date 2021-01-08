from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import LmsModel, GoalModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import Http404
# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password_2 = request.POST['password_2']
        # error handling
        try:
            user = User.objects.create_user(username, email, password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'This user is alredy registered.'}) 
    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error':'Please retry.'})
    return render(request, 'login.html', {})

# def get_user_func(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     context = {'user': user,}
#     return render(request, 'list.html', {'context':context})

@login_required #decorator   
def listfunc(request):
    # user = get_object_or_404(User, pk=user_id)
    # context = {
    #     'user': user,
    #     }
    # table(tb_1) Date
    current_time = timezone.now()
    # table(tb_1) Goal
    goal = GoalModel.objects.all()
    month = 30
    # table(tb_3) No.|Date|START/FINISH|MEMO
    object_list = LmsModel.objects.all()
    return render(request, 'list.html', {'current_time':current_time, 'goal':goal, 'month':month, 'object_list':object_list})


class GoalCreate(CreateView):
    template_name = 'goal_set.html'
    model = GoalModel
    fields = ('goal',)
    success_url = reverse_lazy('list')

# Delete兼用(UpdateView使用しない)
class GoalUpdate(UpdateView):
    template_name = 'goal_update.html'
    model = GoalModel
    fields = ('goal',)
    success_url = reverse_lazy('list')

class GoalDelete(DeleteView):
    template_name = 'goalmodel_confirm_delete.html'
    model = GoalModel
    success_url = reverse_lazy('list')

class LmsFinish(CreateView):
    template_name = 'finish.html'
    model = LmsModel
    fields = ('memo',)
    success_url = reverse_lazy('list')

class LmsDelete(DeleteView):
    template_name = 'lmsmodel_confirm_delete.html'
    model = LmsModel
    success_url = reverse_lazy('list')