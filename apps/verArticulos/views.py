from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
# Create your views here.
def show_listaArticulos(request):
    return render(request, 'products1.html',{})
