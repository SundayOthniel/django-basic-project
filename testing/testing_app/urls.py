from testing_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact')
]