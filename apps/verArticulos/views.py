from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from apps.Carrito_Ventas.models import Articulo
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404

from apps.Carrito_Ventas.models import Seccion,Articulo,Usuario,Carrito,Detalle_Carrito,Factura
from apps.Carrito_Ventas.forms import SeccionForm, CrearUsuarioForm, ArticuloForm
from apps.Carrito_Ventas.models import Articulo
from apps.Carrito_Ventas.models import Seccion
from apps.Carrito_Ventas.forms import ArticuloForm
from django.contrib import messages
from django.http import HttpResponse

from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.urlresolvers  import reverse
from django.shortcuts import redirect
from django.db import connection
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
import django.contrib.auth.hashers as encriptador
# Create your views here.
def show_listaArticulos(request):
    consulta = Articulo.objects.all()
    seccion = Seccion.objects.all()
    return render(request, 'products1.html',{'productos':consulta, 'secciones':seccion})

def filtrar_categorias(request):
    seccion = Seccion.objects.all()
    if request.method == 'POST':
        a = request.POST['selector']
        consulta = Articulo.objects.filter(seccion_fk=a)
        return render(request, 'products1.html',{'productos':consulta, 'secciones':seccion})
    return render(request, 'products1.html',{'secciones':seccion})

def add_carrito(request, productoid):
    usuario = Usuario.objects.get(id = request.user.id)
    prod =  Articulo.objects.get(id = productoid)
    seccion = Seccion.objects.all()
    print "va por aqui"
    try:
        carr =  Carrito.objects.get(usuario_fk = usuario)
        try:
            Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod)
            det = Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod)
            det.cantidad_articulos += 1
            det.save()
            carr.monto_a_pagar = prod.precio * det.cantidad_articulos
            carr.save()
        except Detalle_Carrito.DoesNotExist:
            det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
            carr.monto_a_pagar = prod.precio
            carr.save()
            print "cumplio con el if"
            print "paso por aqui"
    except Carrito.DoesNotExist:
        carr = Carrito.objects.create(usuario_fk = usuario, monto_a_pagar = 0)
        carr.save()
        det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
        carr.monto_a_pagar = prod.precio
        carr.save()
        print "entro a la exepcion"
        return render(request,"products1.html", {"productos":Articulo.objects.all(), "messages": messages.get_messages(request)})
    print "aqui esta al final"
    return render(request,"products1.html", {"productos":Articulo.objects.all(), "messages": messages.get_messages(request), "secciones":seccion})
