from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_library, name='digital_library'),

]