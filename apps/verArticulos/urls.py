from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'Practica2_G1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'lista', 'apps.verArticulos.views.show_listaArticulos', name='show_articulos'), #ruta para listar productos
    url(r'add_carrito/(?P<productoid>\d+)/', 'apps.verArticulos.views.add_carrito', name="add_carrito"), #add carrito
    url(r'filtrar_categorias', 'apps.verArticulos.views.filtrar_categorias', name='filtrar_categorias'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
