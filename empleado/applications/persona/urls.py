from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', 
        views.InicioView.as_view(), 
        name='inicio'),
    path('listar-todos-empleados/', 
        views.ListarTodosEmpleados.as_view(), 
        name='listar_empleados'),
    path('listar-por-departamento/<shorname>/', views.ListarPorArea.as_view(),),
    path('listar-por-trabajo/', views.ListarPorTrabajo.as_view(),),
    path('listar_persona_habilidades/', views.ListarHabilidadesEmpleado.as_view(),),
    path('detail_empleado/<pk>/', views.MODEL_NAMEDetailView.as_view(),),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='add-empleado',),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='update-empleado',),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete-empleado',),
]