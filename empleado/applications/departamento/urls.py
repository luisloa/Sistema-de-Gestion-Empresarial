from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path('new_departamento/', views.NewDepartView.as_view(), name='new_departamento'),
]