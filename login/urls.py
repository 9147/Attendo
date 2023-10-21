from django.urls import path,include
app_name = 'login'
from .views import login

urlpatterns = [
    path('', login, name='login'),
]