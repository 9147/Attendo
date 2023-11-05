from django.urls import path,include
app_name = 'mainapp'
from .views import home,about,docs,swapy,optionSelect,mark,attendance,edit,editmain,update,sheet,getData

urlpatterns = [
    path('', home, name='home'),
    path('getdata/',getData,name='getData'),
    path('edit/<str:option>', edit, name='edit'),
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