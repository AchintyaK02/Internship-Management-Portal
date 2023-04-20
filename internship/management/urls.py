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
   # path('e/repo/<str:id>',views.erepo,name='erep'),
   path('Compform/C/<str:id>',views.Compform,name='cform'),
   path('SCompform/<str:id>',views.SCompform,name='scform'),
   path('Sprogeval/<str:id>',views.Sprogresseval,name='spro'),
   path('Cprogeval/C/<str:id>',views.Cprogresseval,name='cpro'),
   path('svpro/<str:id>',views.Svpro,name='Sview'),
   # path('sepro/<str:id>',views.Sepro,name='Sedit'),
   path('cvpro/<str:id>',views.cvpro,name='cview'),
   # path('cepro/<str:id>',views.cepro,name='cedit'),
   path('internfeedback/<str:id>' , views.fillInternFeedback , name=  'fillInternFeedbacks' ),

  

]
