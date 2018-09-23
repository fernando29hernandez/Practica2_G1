from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'Practica2_G1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^listarArticulos/', 'apps.verArticulos.views.show_listaArticulos', name='show_articulos'), #ruta para listar productos
]
urlpatterns += staticfiles_urlpatterns()
