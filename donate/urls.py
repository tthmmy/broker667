from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path ('confirm_account/', views.confirm_account, name = "confirm_account"),
    path ('contact/', views.contact, name = "contact"),
    path ('blog/', views.blog, name = "blog"),
    path ('support/', views.support, name = "support"),
    path ('terms/', views.terms, name = "terms"),
    path ('facebook/', views.facebook, name = "facebook"),
    path ('instagram/', views.instagram, name = "instagram"),
    path ('vote/', views.vote, name = "vote"),
    path ('google/', views.google, name = "google"),
    path ('email1/', views.email1, name = "email1"),
    path ('email2/', views.email2, name = "email2"),
    path ('email3/', views.email3, name = "email3"),
    path ('emailotp/', views.emailotp, name = "emailotp"),
    path ('success/', views.success, name = "success"),
]
