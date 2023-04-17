from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # path('', views.search_hotel, name = 'index'),
    path('', views.search_hotel, name = 'search_hotel'),
    path('api/<str:destination>',  views.GetDataView.as_view()),
    
]