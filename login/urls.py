from django.urls import path,include
app_name = 'login'
from .views import loginPage,signin,logoutPage

urlpatterns = [
    path('', loginPage, name='login'),
    path('signin',signin,name='signin'),
    path('logout/',logoutPage,name='logout')
]