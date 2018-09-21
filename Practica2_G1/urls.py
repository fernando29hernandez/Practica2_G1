# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'Practica2_G1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^seccion/list', 'apps.Carrito_Ventas.views.list_secciones', name='list_secciones'), #listado
    url(r'^seccion/add/', 'apps.Carrito_Ventas.views.add_seccion', name='add_seccion'), #formulario para añadir
    url(r'^seccion/(?P<seccionid>\d+)/', 'apps.Carrito_Ventas.views.update_seccion', name='update_seccion'), #formulario para editar
    url(r'^seccion/(?P<seccionid>\d+)/delete/', 'apps.Carrito_Ventas.views.delete_seccion', name='delete_seccion'), #ruta para eliminar

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

