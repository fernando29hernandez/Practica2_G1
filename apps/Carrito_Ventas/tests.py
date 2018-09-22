from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from django.test import TestCase
from apps.Carrito_Ventas.models import Seccion
from apps.Carrito_Ventas.forms import SeccionForm
from django.core.context_processors import csrf

class SeccionTestCase(TestCase):
    def setUp(self):
        a1 = Seccion.objects.create(nombre="electrodomesticos",descripcion="area de articulos para el hogar")
        a2 = Seccion.objects.create(nombre="videojuegos",descripcion="esto es un juego")
  
    def test_seccion1(self):
        seccion1 = Seccion.objects.get(nombre="electrodomesticos")
        self.assertEqual(seccion1.nombre, "electrodomesticos")  
    def test_seccion2(self):
        seccion2 = Seccion.objects.get(nombre="videojuegos")
        self.assertEqual(seccion2.nombre, "videojuegos")
    def test_form_seccion(self):
       form = SeccionForm(data={'nombre': "Seccion de prueba", 'descripcion': "Descripcion de prueba"})
       self.assertTrue(form.is_valid())
    def test_secciones_view(self):
        response = self.client.get("/seccion/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_secciones.html")
    def test_secciones_add_view(self):
        response = self.client.get("/seccion/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_seccion.html")
    def test_secciones_add_form_view(self):
        user_count = Seccion.objects.count()
        response = self.client.post("/seccion/add/", {'nombre': 'Seccion de prueba1','descripcion': 'Descripcion de prueba'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seccion.objects.count(), user_count+1)
        self.assertEqual(Seccion.objects.get(nombre="Seccion de prueba1").nombre,"Seccion de prueba1")
    def test_secciones_update_view(self):
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.get("/seccion/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_seccion.html")   
    def test_secciones_delete_view(self):
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.get("/seccion/delete/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eliminar_seccion.html")   
    def test_secciones_update_form_view(self):
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.post(
            reverse('update_seccion', kwargs={'seccionid': str(int(idtemp))}), 
            {'nombre': 'The Catcher in the Rye', 'descripcion': 'Prueba'})
        self.assertEqual(response.status_code, 302)
    def test_secciones_delete_form_view(self):
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.post(
            reverse('delete_seccion', kwargs={'seccionid': str(int(idtemp))}))
        self.assertEqual(response.status_code, 302)
    


class LogInTestCase(TestCase):
    def test_funcion_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_funcion_login(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "LogIn/login.html")

    def test_funcion_ver(self):
        solicitud = self.client.post("/accounts/auth/", {'username': 'nery','password': '1234'})

        
        response = self.client.get("/accounts/loggedin/")
        self.assertEqual(response.status_code, 302) #302 porque es un redirect
