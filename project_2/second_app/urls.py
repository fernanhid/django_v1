from django.urls import path
from second_app import views
from django.conf.urls import url, include

# urlpatterns = [

# path('', views.index, name = 'index'),
# path('help/', views.help, name = 'help'),
# path('info/', views.info, name = 'info'),

# ]

urlpatterns = [

path('', views.index, name = 'index'),
path('help/', views.help, name = 'help'),
path('info/', views.info, name = 'info'),

]