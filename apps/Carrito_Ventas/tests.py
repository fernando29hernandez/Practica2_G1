# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from django.test import TestCase

from apps.Carrito_Ventas.models import Seccion, Articulo, Usuario, Carrito, Detalle_Carrito, Factura
from apps.Carrito_Ventas.forms import SeccionForm, ArticuloForm
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import Client
from datetime import datetime
from django.contrib.auth import authenticate, login

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
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/seccion/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_secciones.html")
    def test_secciones_add_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/seccion/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_seccion.html")
    def test_secciones_add_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        user_count = Seccion.objects.count()
        response = self.client.post("/seccion/add/", {'nombre': 'Seccion de prueba1','descripcion': 'Descripcion de prueba'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seccion.objects.count(), user_count+1)
        self.assertEqual(Seccion.objects.get(nombre="Seccion de prueba1").nombre,"Seccion de prueba1")
    def test_secciones_update_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.get("/seccion/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_seccion.html")   
    def test_secciones_delete_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.get("/seccion/delete/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eliminar_seccion.html")   
    def test_secciones_update_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.post(
            reverse('update_seccion', kwargs={'seccionid': str(int(idtemp))}), 
            {'nombre': 'The Catcher in the Rye', 'descripcion': 'Prueba'})
        self.assertEqual(response.status_code, 302)
    def test_secciones_delete_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        
        idtemp=Seccion.objects.get(nombre="electrodomesticos").id
        response = self.client.post(
            reverse('delete_seccion', kwargs={'seccionid': str(int(idtemp))}))
        self.assertEqual(response.status_code, 302)
    


class LogInTestCase(TestCase):
    def test_model_usuario(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.assertEqual(self.user.__str__(),str(self.user.id) +" "+self.user.username)
    def test_funcion_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_funcion_login(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "LogIn/login.html")

    def test_funcion_ver(self):
        #Cuando se quiere iniciar sesión con credenciales incorrectas
        solicitud = self.client.post("/accounts/auth/", {'username': 'nery','password': '1234'})

        #Cuando voy a iniciar sesión con credenciales validas
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=False)
        solicitud = self.client.post("/accounts/auth/", {'username': 'admin','password': 'pass@123'})
        
        #self.client.login(username='admin', password='pass@123')


    def test_funcion_loggedin(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='user', password='pass@123', email='user@user.com',tipo=False)
        self.client.login(username='user', password='pass@123')

        response = self.client.get("/accounts/loggedin/")
        ##self.assertEqual(response.status_code, 302) #302 porque es un redirect
        self.assertEqual(response.status_code, 200) #302 porque es un redirect


        #Para cuando es ADMINISTRADOR
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        
        response = self.client.get("/accounts/loggedin/")
        ##self.assertEqual(response.status_code, 302) #302 porque es un redirect
        self.assertEqual(response.status_code, 200) #302 porque es un redirect

    def test_funcion_invalid(self):
        response = self.client.get("/accounts/invalid/")
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "LogIn/login.html")

    def test_funcion_logout(self):    
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='user', password='pass@123', email='user@user.com',tipo=False)
        self.client.login(username='user', password='pass@123')

        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 302)    


        self.client.logout()
        
        #self.client.login(username='admin', password='pass@123')

    def test_funcion_crearUsuario(self):
        #Método get de crear usuario
        response = self.client.get("/crearUsuario/")
        self.assertEqual(response.status_code, 200)

        #Método POST de crear usuario con un formulario válido
        solicitud = self.client.post("/crearUsuario/", {'username': 'admin','password': 'pass@123'})

        #Método POST de crear usuario con un formulario NO válido
        solicitud = self.client.post("/crearUsuario/", {'username': 'admin'})
    def test_view_user(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/usuario/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_usuarios.html")
    def test_secciones_update_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')        
        response = self.client.get("/usuario/"+str(self.user.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editar_usuario.html")   
    def test_secciones_delete_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/usuario/delete/"+str(self.user.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eliminar_usuario.html")   
    def test_usuario_update_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.post(
            reverse('update_usuario', kwargs={'usuarioid': str(int(self.user.id))}), 
            {'username': 'prueba', 'email': 'hola@gmail.com','password':'asafdf52s+A','tipo':0,'last_name':'sdsd','first_name':'sdsds'})
        self.assertEqual(response.status_code, 302)
    def test_usuario_delete_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.post(
            reverse('delete_usuario', kwargs={'usuarioid': str(int(self.user.id))}))
        self.assertEqual(response.status_code, 302)

class CarritoTestCase(TestCase):
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
        ca = Carrito.objects.create(usuario_fk=self.user, monto_a_pagar=500)
        carr = Carrito.objects.get(usuario_fk=self.user, monto_a_pagar=500)
        response = self.client.get("/carrito/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_carrito.html")

    def test_list_articulo_clienteo(self):
        usua = Usuario.objects.get(username="yoselin")
        carr = Carrito.objects.get(usuario_fk = usua)
        prod = Articulo.objects.get(nombre="Escudo")
        self.assertEqual(carr.usuario_fk, usua)
        self.assertEqual(prod.nombre, "Escudo")
        response = self.client.get("/articulosCliente/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_articulos_cliente.html")

    def test_add_carrito(self):
        idarti=Articulo.objects.get(nombre="Escudo").id

        self.client = Client()        
        self.user = Usuario.objects.create_user(username='admin2', password='pass2@123', email='admin2@admin.com',tipo=True)         
        self.client.login(username='admin2', password='pass2@123')
        prod =  Articulo.objects.get(id = idarti)

        try:
            carr = Carrito.objects.get(usuario_fk=self.user, monto_a_pagar=500) 

        except Carrito.DoesNotExist: 
            response = self.client.get("/articulosCliente/add_carrito/"+str(idarti)+"/")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "listar_articulos_cliente.html")

        response = self.client.get("/articulosCliente/add_carrito/"+str(idarti)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_articulos_cliente.html")

    def test_add_carrito2(self):
        idarti=Articulo.objects.get(nombre="Escudo").id

        self.client = Client()        
        self.user = Usuario.objects.create_user(username='admin2', password='pass2@123', email='admin2@admin.com',tipo=True)         
        self.client.login(username='admin2', password='pass2@123')
        prod =  Articulo.objects.get(id = idarti)
        response = self.client.get("/articulosCliente/add_carrito/"+str(idarti)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_articulos_cliente.html")
         
class ArticuloTestCase(TestCase):
    def setUp(self):
        a1 = Seccion.objects.create(nombre="consolas",descripcion="consolas de video juegos")
        a2 = Seccion.objects.create(nombre="videojuegos",descripcion="esto es un juego")
        Articulo.objects.create(nombre="play station", descripcion="consola de 500Gb",precio=3000,seccion_fk=a1,imagen="Articulo/switch.jpg")
        Articulo.objects.create(nombre="Spider-Man", descripcion="juego para play station 4",precio=700,seccion_fk=a2,imagen="Articulo/switch.jpg")
    def test_model_articulo(self):
        a3 = Seccion.objects.create(nombre="consolas",descripcion="consolas de video juegos")
        self.articulo1 = Articulo.objects.create(nombre="play station4", descripcion="consola de 500Gb",precio=3000,seccion_fk=a3,imagen="Articulo/switch.jpg")
        self.assertEqual(self.articulo1.__str__(),str(self.articulo1.id) +" "+self.articulo1.nombre)    
    def test_articulo1(self):
        articulo1 = Articulo.objects.get(nombre="play station")
        self.assertEqual(articulo1.nombre,"play station")
        self.assertEqual(articulo1.descripcion, "consola de 500Gb")
        self.assertEqual(articulo1.precio, 3000)
        self.assertEqual(articulo1.imagen, "Articulo/switch.jpg")
    def test_articulo2(self):
        articulo1 = Articulo.objects.get(nombre="Spider-Man")
        self.assertEqual(articulo1.nombre,"Spider-Man")
        self.assertEqual(articulo1.descripcion, "juego para play station 4")
        self.assertEqual(articulo1.precio, 700)    
        self.assertEqual(articulo1.imagen, "Articulo/switch.jpg")
    def test_articulo1_seccion1(self):
        articulo1 = Articulo.objects.get(nombre="play station")
        self.assertEqual(articulo1.seccion_fk.nombre, "consolas")
    def test_articulo2_seccion2(self):
        articulo1 = Articulo.objects.get(nombre="Spider-Man")
        self.assertEqual(articulo1.seccion_fk.nombre, "videojuegos")
    def test_form_articulo(self):
        #img = SimpleUploadedFile('C:/Users/LuisOmar/Pictures/logo.png', "file_content" ,content_type='image/png')
        #img = Image.open("C:/Users/LuisOmar/Pictures/logo.png")   
        form = ArticuloForm(data={'nombre': 'play station', 'descripcion': 'consola de 500Gb','precio': '3000', 'seccion_fk': str(int(Seccion.objects.get(nombre="consolas").id))})
        print(form.errors)
        self.assertTrue(form.is_valid())
    def test_articulos_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/articulo/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_articulos.html")
    def test_articulos_add_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        response = self.client.get("/articulo/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_articulo.html")
    def test_articulos_add_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        seccionprueba = Seccion.objects.create(nombre="hola",descripcion="prueba")
        user_count = Articulo.objects.count()
        response = self.client.post("/articulo/add/", {'nombre': 'prueba1',
                'descripcion': 'Descripcion de prueba', 'precio':'100', 'seccion_fk': str(int(seccionprueba.id))})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Articulo.objects.count(), user_count+1)
        self.assertEqual(Articulo.objects.get(nombre="prueba1").nombre,"prueba1")
    def test_articulo_update_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        idtemp=Articulo.objects.get(nombre="play station").id
        response = self.client.get("/articulo/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crear_articulo.html")  
    def test_articulo_delete_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        idtemp=Articulo.objects.get(nombre="play station").id
        response = self.client.get("/articulo/delete/"+str(idtemp)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eliminar_articulo.html")
    def test_articulo_update_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        idtemp=Articulo.objects.get(nombre="play station").id
        secc_fk = Articulo.objects.get(nombre="play station").seccion_fk
        response = self.client.post(
            reverse('update_articulo', kwargs={'articuloid': str(int(idtemp))}), 
            {'nombre': 'prueba', 'descripcion': 'Prueba descripcion','precio': '100', 
                'seccion_fk':str(int(Seccion.objects.get(nombre="consolas").id))})
        self.assertEqual(response.status_code, 302)
    def test_articulo_delete_form_view(self):
        self.client = Client() # May be you have missed this line
        self.user = Usuario.objects.create_user(username='admin', password='pass@123', email='admin@admin.com',tipo=True)
        self.client.login(username='admin', password='pass@123')
        idtemp=Articulo.objects.get(nombre="play station").id
        response = self.client.post(
            reverse('delete_articulo', kwargs={'articuloid': str(int(idtemp))}))
        self.assertEqual(response.status_code, 302) 
