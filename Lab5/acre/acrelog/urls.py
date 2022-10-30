from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:field_name>/', views.fields, name="fields")
]


