from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:field_id>/', views.fields, name="fields")
]
