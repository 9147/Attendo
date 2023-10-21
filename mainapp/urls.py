from django.urls import path,include
app_name = 'mainapp'
from .views import home,about,docs

urlpatterns = [
    path('', home, name='home'),
    path('about/', about,name='about'),
    path('docs/', docs,name='docs'),
]