from django.urls import path
from . import views

urlpatterns = [
   path('',views.login,name='login'),
   path('home',views.home,name='hi'),
   path('home/<str:id>',views.details,name='detail'),
   path('home/tec/<str:id>',views.goback,name='gobac'),
   path('home/com/<str:id>',views.cgoback,name='cgobac'),
   path('midterm/<str:id>',views.midterm,name='mid'),
   path('endterm/<str:id>',views.endterm,name='end'),
   path('home/C/<str:id>',views.cdetails,name='cdetail'),
   path('midterm/C/<str:id>',views.cmidterm,name='cmid'),
   path('endterm/C/<str:id>',views.cendterm,name='cend'),
   path('repo/<str:id>',views.mrepo,name='mrep'),
   # path('e/repo/<str:id>',views.erepo,name='erep')
   
]
