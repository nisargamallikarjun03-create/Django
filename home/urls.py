from django.urls import path
from . import views

urlpatterns = [
    path('', views.january, name='march'),
    
    path('student/', views.student),
    path('january/', views.january, name='january'),
    path('feb/', views.feb, name='feb'),
    path('march/', views.march, name='march'),
    path('intro/', views.intro, name='intro'),
    
]