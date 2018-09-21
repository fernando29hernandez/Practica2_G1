# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from apps.Carrito_Ventas.models import Seccion, Usuario
from apps.Carrito_Ventas.forms import SeccionForm, CrearUsuarioForm
from django.contrib import messages
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
    c = {}
    c.update(csrf(request))
    return render(request , 'LogIn/login.html', c)

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
	resultado = cursor.execute("select tipo from carrito_ventas_usuario where id = %s", [request.user.id])
	
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
	if encriptador.is_password_usable(password):
		return password #Si ya está encriptada regreso la misma contraseña
	else:
		return encriptador.make_password(password,salt=None,hasher='default')








def list_secciones(request):
    return render_to_response("listar_secciones.html", {"secciones": Seccion.objects.all(), "messages": messages.get_messages(request)})
 
def add_seccion(request):
    form = SeccionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been saved!")
            return HttpResponseRedirect("/seccion/list/")
 
    return render(request, 'crear_seccion.html', {'form': form})
 
def update_seccion(request, seccionid):
    instance = get_object_or_404(Seccion, id=seccionid)
    form = SeccionForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been updated!")
            return HttpResponseRedirect("/seccion/list/")
 
    return render(request, 'crear_seccion.html', {'form': form})
 
def delete_seccion(request, seccionid):
    instance = get_object_or_404(Seccion, id=seccionid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "The post with id %s has been deleted!" % seccionid)
    return HttpResponseRedirect("/seccion/list/")