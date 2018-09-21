# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from apps.Carrito_Ventas import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Practica2_G1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','apps.Carrito_Ventas.views.home'),
    url(r'^accounts/login/$', 'apps.Carrito_Ventas.views.login'),
	url(r'^accounts/auth/$', 'apps.Carrito_Ventas.views.ver'),
	url(r'^accounts/logout/$', 'apps.Carrito_Ventas.views.logout'),
	url(r'^accounts/loggedin/$', 'apps.Carrito_Ventas.views.loggedin'),
	url(r'^accounts/invalid/$', 'apps.Carrito_Ventas.views.invalid'),

    url(r'^crearUsuario2/', views.CrearUsuario2.as_view(), name="CrearUsuario2"),
    url(r'^crearUsuario/', views.CrearUsuario, name="CrearUsuario"),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^seccion/list', 'apps.Carrito_Ventas.views.list_secciones', name='list_secciones'), #listado
    url(r'^seccion/add/', 'apps.Carrito_Ventas.views.add_seccion', name='add_seccion'), #formulario para añadir
    url(r'^seccion/(?P<seccionid>\d+)/', 'apps.Carrito_Ventas.views.update_seccion', name='update_seccion'), #formulario para editar
    url(r'^seccion/(?P<seccionid>\d+)/delete/', 'apps.Carrito_Ventas.views.delete_seccion', name='delete_seccion'), #ruta para eliminar

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

