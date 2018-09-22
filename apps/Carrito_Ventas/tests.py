from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from django.test import TestCase
from apps.Carrito_Ventas.models import Seccion,Articulo,Usuario,Carrito,Detalle_Carrito,Factura
from apps.Carrito_Ventas.forms import SeccionForm
from datetime import datetime  
from django.test import Client 
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

class SeccionTestCase(TestCase):
    def setUp(self):
        a1 = Seccion.objects.create(nombre="electrodomesticos",descripcion="area de articulos para el hogar")
        a2 = Seccion.objects.create(nombre="videojuegos",descripcion="esto es un juego")
        art1 = Articulo.objects.create(nombre="Micro Ondas",descripcion="micro",precio=300,imagen="Articulo/Under_the_bridge.jpg",seccion_fk=a1)
        art2 = Articulo.objects.create(nombre="Escudo",descripcion="USAC",precio=100,imagen="Articulo/logo.png",seccion_fk=a2)
        u1 = Usuario.objects.create(password="1234",is_superuser=1,username="yoselin",first_name="yoselin",last_name="lemus",email="yoselin@yo.com",is_staff=1,is_active=1,date_joined=datetime.now(),tipo=1)
        self.user = u1
        ca = Carrito.objects.create(usuario_fk=u1,monto_a_pagar=500)
        de1 = Detalle_Carrito.objects.create(carrito_fk=ca,articulo_fk=art1,cantidad_articulos=1)
        de2 = Detalle_Carrito.objects.create(carrito_fk=ca,articulo_fk=art2,cantidad_articulos=1)
          
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
    
    def test_carrito(self):
        u1 = Usuario.objects.get(username="yoselin",first_name="yoselin",last_name="lemus",email="yoselin@yo.com")
        carrito1 = Carrito.objects.get(usuario_fk=u1,monto_a_pagar=500)
        self.assertEqual(carrito1.usuario_fk, u1)  
    def test_detalle1(self):
        u1 = Usuario.objects.get(username="yoselin",first_name="yoselin",last_name="lemus",email="yoselin@yo.com")
        carrito1 = Carrito.objects.get(usuario_fk=u1,monto_a_pagar=500)
        art1 = Articulo.objects.get(nombre="Micro Ondas")
        detalle1 = Detalle_Carrito.objects.get(carrito_fk=carrito1,articulo_fk=art1,cantidad_articulos=1)
        self.assertEqual(detalle1.carrito_fk, carrito1)  
    def test_detalle2(self):
        u1 = Usuario.objects.get(username="yoselin",first_name="yoselin",last_name="lemus",email="yoselin@yo.com")
        carrito1 = Carrito.objects.get(usuario_fk=u1,monto_a_pagar=500)
        art2 = Articulo.objects.get(nombre="Escudo")
        detalle2 = Detalle_Carrito.objects.get(carrito_fk=carrito1,articulo_fk=art2,cantidad_articulos=1)
        self.assertEqual(detalle2.carrito_fk, carrito1)

    def test_carrito_view(self):
        self.client = Client()        
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)         
        self.client.login(username='admin', password='pass@123')
        # ca = Carrito.objects.create(usuario_fk=self.user, monto_a_pagar=500)
        # carr = Carrito.objects.get(usuario_fk=self.user, monto_a_pagar=500)
        response = self.client.get("/carrito/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_carrito.html")
        # response = self.client.post('/carrito/list/', {'usuario_fk':"1", 'monto_a_pagar': "300"})
        # self.assertTemplateUsed(response, "listar_carrito.html")

    def test_list_articulo_clienteo(self):
        usua = Usuario.objects.get(username="yoselin")
        carr = Carrito.objects.get(usuario_fk = usua)
        prod = Articulo.objects.get(nombre="Escudo")
        self.assertEqual(carr.usuario_fk, usua)
        self.assertEqual(prod.nombre, "Escudo")
        response = self.client.get("/articulosCliente/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_articulos_cliente.html")

    # def test_add_carrito(self):
