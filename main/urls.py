from main.views import external_redirect

from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),  # URL raiz para o template base.html
    path('login/', views.login_view, name='login'),
    path('login/cadastro/', views.cadastro_view, name='cadastro'),
    path('login/denuncia/', views.denuncia_view, name='denuncia'),
    path('login/reset/', views.reset_view, name='reset'),
    path('external_url/', external_redirect, name='external_url'),
]

