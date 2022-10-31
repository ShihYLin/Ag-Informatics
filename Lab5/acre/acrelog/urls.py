from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fields/<str:field_name>/', views.fields, name="fields"),
    path('secret-sauce/', views.secret, name="secret-sauce"),
]


