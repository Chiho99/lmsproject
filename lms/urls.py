from django.contrib import admin
from django.urls import path, include
from .views import listfunc, LmsFinish, goalfunc, LmsDelete

urlpatterns = [
path('admin/', admin.site.urls),
path('list/', listfunc, name='list'),
# path('start/', LmsStart.as_view(), name='start'),
path('finish/', LmsFinish.as_view(), name='finish'),
path('goal/', goalfunc, name='goal'),
path('delete/<int:pk>/', LmsDelete.as_view(), name='delete')
]