# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from apps.Carrito_Ventas.models import Seccion
from apps.Carrito_Ventas.forms import SeccionForm
from django.contrib import messages
 
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
    instance =Seccion.objects.get(id=seccionid)
    if request.method == 'POST':
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "The post has been Deleted!")
        return HttpResponseRedirect("/seccion/list/")
    return render(request, 'eliminar_seccion.html',{'seccion':instance})
 