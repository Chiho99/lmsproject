from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfunc ,listfunc, LmsFinish, LmsDelete, GoalCreate, GoalUpdate, GoalDelete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', signupfunc),
    path('admin/', admin.site.urls),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('list/', listfunc, name='list'),
    # path('start/', LmsStart.as_view(), name='start'),
    path('finish/', LmsFinish.as_view(), name='finish'),
    path('goal_set/', GoalCreate.as_view(), name='goal_set'),
    # path('goal_update/<int:pk>', GoalUpdate.as_view(), name='goal_update'),
    path('goal_remove/<int:pk>/', GoalDelete.as_view(), name='goal_remove'),
    path('delete/<int:pk>/', LmsDelete.as_view(), name='delete')
]