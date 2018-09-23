# -*- coding: utf-8 -*-
from django.shortcuts import render
#from prettytable import PrettyTable
from beautifultable import BeautifulTable
# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404

from apps.Carrito_Ventas.models import Seccion,Articulo,Usuario,Carrito,Detalle_Carrito,Factura
from apps.Carrito_Ventas.forms import SeccionForm, CrearUsuarioForm, ArticuloForm
from apps.Carrito_Ventas.models import Articulo
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

# MANEJO DEL LOGIN
def home(request):
    return render(request, 'home.html')

def login(request):
	#c = {}
	#c.update(csrf(request))
	return render(request , 'LogIn/login.html')

def ver(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

@login_required
def loggedin(request):
	cursor = connection.cursor()
	resultado = cursor.execute("select tipo from Carrito_Ventas_usuario where id = %s", [request.user.id])
	
	results = dictfetchall(cursor)
	r = results[0]['tipo']
	
	#Verifico si es un administrador
	if r == 0:
		print "Administrador"
		return render(request,'LogIn/loggedin.html')


	#Si es un usuario normal (NO administrador)
	print "Usuario normal"
	return render(request,'LogIn/loggedin.html')
	
def invalid(request):
	return render_to_response('LogIn/invalid.html')

@login_required
def logout(request):
	auth.logout(request)
	return redirect(reverse('apps.Carrito_Ventas.views.login'))	
	
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class CrearUsuario2(CreateView):
	model = Usuario
	form_class = CrearUsuarioForm
	template_name = 'LogIn/crearUsuario.html'
	success_url = reverse_lazy('apps.Carrito_Ventas.views.login')
	#success_url = redirect(reverse('apps.Carrito_Ventas.views.login'))


def CrearUsuario(request):
	if request.method == 'POST':
		form = CrearUsuarioForm(request.POST)
		if form.is_valid():
			#form.save()
			v = form.save(commit = False)
			
			v.tipo = True #Indico que es un usuario normal
			v.password = encriptarpassword(v.password) #Veo si tengo que encriptar la contraseña
			v.save()
		else:
			print("ERROR")
		return redirect(reverse('apps.Carrito_Ventas.views.login'))	
	else:#Si es un GET se renderiza el formulario
		form = CrearUsuarioForm()

	#return redirect(reverse('apps.Carrito_Ventas.views.login'))
	return render(request,'LogIn/crearUsuario.html',{'form':form})

def encriptarpassword(password):
	#Verifica si la contrasea ya está encriptada
	#if encriptador.is_password_usable(password):
	#	return password #Si ya está encriptada regreso la misma contraseña
	#else:
	#	return encriptador.make_password(password,salt=None,hasher='default')

    #Siempre voy a encriptar
    return encriptador.make_password(password,salt=None,hasher='default')


@login_required
def list_secciones(request):
    return render_to_response("listar_secciones.html", {"secciones": Seccion.objects.all(), "messages": messages.get_messages(request)})

@login_required
def add_seccion(request):
    form = SeccionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been saved!")
            return HttpResponseRedirect("/seccion/list/")
 
    return render(request, 'crear_seccion.html', {'form': form})

@login_required
def update_seccion(request, seccionid):
    instance = get_object_or_404(Seccion, id=seccionid)
    form = SeccionForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been updated!")
            return HttpResponseRedirect("/seccion/list/")
 
    return render(request, 'crear_seccion.html', {'form': form})
 
@login_required
def delete_seccion(request, seccionid):
    instance =Seccion.objects.get(id=seccionid)
    if request.method == 'POST':
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "The post has been Deleted!")
        return HttpResponseRedirect("/seccion/list/")
    return render(request, 'eliminar_seccion.html',{'seccion':instance})
 
def list_articulos(request):
    return render_to_response("listar_articulos.html", {"articulos": Articulo.objects.all(), "messages": messages.get_messages(request)})


def add_articulo(request):
    form = ArticuloForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been saved!")
            return HttpResponseRedirect("/articulo/list/")
 
    return render(request, 'crear_articulo.html', {'form': form})
 
def update_articulo(request, articuloid):
    instance = get_object_or_404(Articulo, id=articuloid)
    form = ArticuloForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been updated!")
            return HttpResponseRedirect("/articulo/list/")
 
    return render(request, 'crear_articulo.html', {'form': form})
 
def delete_articulo(request, articuloid):
    instance =Articulo.objects.get(id=articuloid)
    if request.method == 'POST':
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "The post has been Deleted!")
        return HttpResponseRedirect("/articulo/list")
    return render(request, 'eliminar_articulo.html',{'articulo':instance})

def list_carrito(request):
    usuario = Usuario.objects.get(id = request.user.id)
    carr = Carrito.objects.get(usuario_fk = usuario)
    deta = Detalle_Carrito.objects.filter(carrito_fk = carr)
    return render_to_response("listar_carrito.html", {"carrito":carr, "detalle":deta, "messages": messages.get_messages(request) })

def list_articulo_cliente(request):
    # print "hola"
    return render_to_response("listar_articulos_cliente.html", {"articulos":Articulo.objects.all(), "messages": messages.get_messages(request), "user":request.user} )

def add_carrito(request, productoid):
    usuario = Usuario.objects.get(id = request.user.id)
    prod =  Articulo.objects.get(id = productoid)
    try:
        carr =  Carrito.objects.get(usuario_fk = usuario)
        if Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod) == Detalle_Carrito.DoesNotExist:
            det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
            carr.monto_a_pagar = prod.precio
            carr.save()
        else:
            det = Detalle_Carrito.objects.get(carrito_fk = carr, articulo_fk = prod)
            det.cantidad_articulos += 1
            det.save()
            carr.monto_a_pagar = prod.precio * det.cantidad_articulos
            carr.save()

    except Carrito.DoesNotExist:
        carr = Carrito.objects.create(usuario_fk = usuario, monto_a_pagar = 0)
        carr.save()
        det = Detalle_Carrito.objects.create(carrito_fk = carr, articulo_fk = prod,cantidad_articulos = 1)
        carr.monto_a_pagar = prod.precio
        carr.save()
        return render(request,"listar_articulos_cliente.html", {"articulos":Articulo.objects.all(), "messages": messages.get_messages(request)})
    
    return render(request,"listar_articulos_cliente.html", {"articulos":Articulo.objects.all(), "messages": messages.get_messages(request)})


def list_facturas(request):
    return render_to_response("listar_facturas.html", {"facturas": Factura.objects.all()})

def add_factura(request, carritoid):
    carr = Carrito.objects.get(id=carritoid)
    dett = Detalle_Carrito.objects.filter(carrito_fk = carritoid)

    table = BeautifulTable()
    table.column_headers = ['No.', 'Nombre', 'Precio', 'Cantidad']
    i = 1
    for dd in dett:
        
        table.append_row([i, dd.articulo_fk.nombre, dd.articulo_fk.precio, dd.cantidad_articulos])
        i = i + 1

    print(table)
    algo = "\n" + table.get_string()
    algo += "\n\n\t\t\tTotal: " + str(carr.monto_a_pagar)
    facc = Factura.objects.create(usuario_fk = carr.usuario_fk, descripcion = algo)
    facc.save()
    # Detalle_Carrito.objects.filter(carrito_fk = carritoid).delete()
    # Detalle_Carrito.save()
    unaFac = Factura.objects.get(id = facc.id)
    return render_to_response("factura.html", {"factura": unaFac})
    