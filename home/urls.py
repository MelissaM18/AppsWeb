from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Prueba.as_view(), name="prueba"),
]