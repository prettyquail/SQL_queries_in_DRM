from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.selectall,name='selectall'),
     path('1/',views.selected,name='selected'),
     path('2/',views.aggregate,name='aggregate'),
    
]