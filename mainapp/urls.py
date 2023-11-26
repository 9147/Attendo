from django.urls import path,include
app_name = 'mainapp'
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('deletedata/',deletedata,name='deletedata'),
    path('demo/',demo,name='demo'),
    path('getdata/',getData,name='getData'),
    path('edit/<str:option>', edit, name='edit'),
    path('uploaddata/',uploadData,name='uploaddata'),
    path('editmain/<str:option>/<str:id>', editmain, name='editmain'),
    path('list/sheet/<int:id>',sheet,name='sheet'),
    path('editmain/<str:option>/send/<str:id>', update, name='update'),
    path('about/', about,name='about'),
    path('docs/', docs,name='docs'),
    path('prof/options/<int:sid>',optionSelect,name='options'),
    path('1/attendance/<int:sid>', swapy, name='swapy'),
    path('2/attendance/<int:sid>', mark, name='mark'),
    path('attendance/<int:sid>',attendance,name='attendance'),
]