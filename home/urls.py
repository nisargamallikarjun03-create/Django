from django.urls import path
from . import views

urlpatterns = [
    path('', views.january, name='march'),
    
    path('student/', views.student),
    path('january/', views.january, name='january'),
    path('feb/', views.january, name='feb'),
    path('march/', views.january, name='march'),
    path('intro/', views.january, name='intro'),
    
]