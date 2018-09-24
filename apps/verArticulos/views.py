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
from beautifultable import BeautifulTable
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
    subtotal = 0
    try:
        carr =  Carrito.objects.get(usuario_fk = usuario)
        subtotal = carr.monto_a_pagar
        try:
            Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod)
            det = Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod)
            det.cantidad_articulos += 1
            det.save()
            carr.monto_a_pagar = subtotal + (prod.precio * det.cantidad_articulos)
            carr.save()
        except Detalle_Carrito.DoesNotExist:
            det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
            carr.monto_a_pagar = subtotal + (prod.precio * det.cantidad_articulos)
            carr.save()
            print "cumplio con el if"
            print "paso por aqui"
    except Carrito.DoesNotExist:
        carr = Carrito.objects.create(usuario_fk = usuario, monto_a_pagar = 0)
        carr.save()
        det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
        carr.monto_a_pagar = subtotal + (prod.precio * det.cantidad_articulos)
        carr.save()
        print "entro a la exepcion"
        return render(request,"products1.html", {"productos":Articulo.objects.all(), "messages": messages.get_messages(request)})
    print "aqui esta al final"
    return render(request,"products1.html", {"productos":Articulo.objects.all(), "messages": messages.get_messages(request), "secciones":seccion})


@login_required
def list_facturas(request):
    return render(request,"listar_facturas.html", {"facturas": Factura.objects.all(), "messages": messages.get_messages(request) })

@login_required
def add_factura(request, carritoid):
    carr = Carrito.objects.get(id=carritoid)
    dett = Detalle_Carrito.objects.filter(carrito_fk = carritoid)

    table = BeautifulTable()
    table.column_headers = ['No.', 'Nombre', 'Precio', 'Cantidad']
    i = 1
    for dd in dett:
        
        table.append_row([i, dd.articulo_fk.nombre, dd.articulo_fk.precio, dd.cantidad_articulos])
        i = i + 1

    algo = "\n" + table.get_string()
    algo += "\n\n\t\t\tTotal: " + str(carr.monto_a_pagar)
    facc = Factura.objects.create(usuario_fk = carr.usuario_fk, descripcion = algo)
    facc.save()
    carr = Carrito.objects.get(id=carritoid)
    carr.delete()
    unaFac = Factura.objects.get(id = facc.id)
    return render(request,"factura.html", {"factura": unaFac})

