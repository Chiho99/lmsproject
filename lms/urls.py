from django.contrib import admin
from django.urls import path, include
from .views import listfunc, LmsFinish, LmsDelete, GoalCreate, GoalUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', listfunc, name='list'),
    # path('start/', LmsStart.as_view(), name='start'),
    path('finish/', LmsFinish.as_view(), name='finish'),
    path('goal_set/', GoalCreate.as_view(), name='goal_set'),
    path('goal_update/<int:pk>', GoalUpdate.as_view(), name='goal_update'),
    path('delete/<int:pk>/', LmsDelete.as_view(), name='delete')
]