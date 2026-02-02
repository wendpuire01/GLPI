from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name="home"),
    path('inventaire/',views.inventaire,name="inventaire"),
    path('acquisition/',views.acquisition,name="acquisition"),
    path('attribution/',views.attribution,name="attribution"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('panne/',views.panne,name="panne"),
    path('licence/',views.licence,name="Licence"),
    path('personne/',views.personne,name="personne"),
    path('',views.login,name='login'),
    #path('',views.CustomLoginView,name='login'),
    path('PrintInventaire/',views.print_inventaire, name='PrintInventaire'),
    path('licences/', views.licence_list, name='licence_list'),
    #path('register/', register_licence, name='register_licence'),
    path('toggle-visibility/<int:pk>/', views.toggle_visibility, name='toggle_visibility'),
    path('sheet/', views.sheet_view, name='sheet-view'),
    path('demande/',views.de_maintenance,name='maintenance'),
    path('modifier_personne/<int:pk>/',views.modifier_personne,name="modifier_personne"),
    path('supprimer_personne/<int:pk>/',views.supprimer_personne,name="supprimer_personne"),
    path('api/machines-par-mois/', views.machines_par_mois, name='machines_par_mois'),           
]