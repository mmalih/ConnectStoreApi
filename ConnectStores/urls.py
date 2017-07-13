from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/', views.article, name='article'),
    url(r'^panier/', views.panier, name='panier'),
    url(r'^categorie/', views.categorie, name='categorie'),
    url(r'^client/', views.client, name='client')
]