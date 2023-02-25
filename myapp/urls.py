from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.lista_locacao, name='lista_locacao'), 
    path('form_locatario', views.form_locatario, name='criar_locatario'), 
    path('form_imovel', views.form_imovel, name='criar_imovel'), 
]

