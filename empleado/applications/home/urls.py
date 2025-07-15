from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('prueba/', views.PruebaListView.as_view()),
    path('prueba2/', views.ModeloPruebaListView.as_view(),),
    path('add-libro/', views.PruebaCreateView.as_view()),
]
