from django.urls import path

#importing our function
from . import views

#creating URL patterns
urlpatterns = [
    path('', views.index, name = 'index')

]