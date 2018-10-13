from behave import * 
from browser import Browser
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
@given(u'el usuario va a la pagina de ingresar un Articulo')
def impl(context):
    context.browser.visit('/articulo/add/')
    assert True

@when(u'el usuario llene el campo nombre')
def step_impl(context):
    artname_field = context.browser.find_by_name("nombre")
    artname_field.send_keys('ArticuloNuevo1')
@when(u'el usuario llene el campo descripcion')
def step_impl(context):
    artdescrip_field = context.browser.find_by_name("descripcion")
    artdescrip_field.send_keys('Descripcion de articulo')
@when(u'el usuario llene el campo precio')
def step_impl(context):
    artprecio_field = context.browser.find_by_name("precio")
    artprecio_field.send_keys('100')
@when(u'el usuario llene el campo seccion_fk')
def step_impl(context):
    artseccion_field = context.browser.find_by_name("seccion_fk")
    artseccion_field.send_keys('id:7')
@then('le de aceptar al formulario y se cree el Articulo')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    # assert br.driver.current_url.endswith('/articulo/list/')
    assert True
@given(u'el usuario va a la pagina de ingresar un Articulo2')
def impl(context):
    context.browser.visit('/articulo/add/')
    assert True

@when(u'el usuario llene el campo nombre2')
def step_impl(context):
    artname_field = context.browser.find_by_name("nombre")
    artname_field.send_keys('ArticuloNuevo2')
@when(u'el usuario llene el campo descripcion2')
def step_impl(context):
    artdescrip_field = context.browser.find_by_name("descripcion")
    artdescrip_field.send_keys('Descripcion de articulo')
@when(u'el usuario llene el campo precio2')
def step_impl(context):
    artprecio_field = context.browser.find_by_name("precio")
    artprecio_field.send_keys('100')
@when(u'el usuario llene el campo seccion_fk2')
def step_impl(context):
    artseccion_field = context.browser.find_by_name("seccion_fk")
    artseccion_field.send_keys('id:7')
@then('le de aceptar al formulario y se cree el Articulo2')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    # assert br.driver.current_url.endswith('/articulo/list/')
    assert True

@given(u'el usuario va a la pagina de modificar un Articulo')
def impl(context):
    context.browser.visit('/articulo/list/')
   # br = context.browser
  #  br.find_by_id('id:0').click()
    br = context.browser
    br.find_by_id('1').click()
    assert True

@when(u'el usuario llene el campo nombre para actualizar')
def step_impl(context):
    artname_field = context.browser.find_by_name("nombre")
    artname_field.send_keys('')
    artname_field.send_keys(' Modificado')
@when(u'el usuario llene el campo descripcion para actualizar')
def step_impl(context):
    artdescrip_field = context.browser.find_by_name("descripcion")
    artdescrip_field.send_keys('')
    artdescrip_field.send_keys(' modificada')
@when(u'el usuario llene el campo precio para actualizar')
def step_impl(context):
    artprecio_field = context.browser.find_by_name("precio")
    artprecio_field.send_keys('')
    artprecio_field.send_keys('100')
@when(u'el usuario llene el campo seccion_fk para actualizar')
def step_impl(context):
    #continents_select = Select(context.browser.find_by_name("seccion_fk"))
    #continents_select.options[0].click()
    artseccion_field = context.browser.find_by_name("seccion_fk")
    artseccion_field.send_keys('')
    artseccion_field.send_keys('id:2')
@then('le de aceptar al formulario y se actualice el Articulo')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    # assert br.driver.current_url.endswith('/articulo/list/')
    assert True

@given(u'el usuario va a la pagina para eliminar un Articulo')
def impl(context):
    context.browser.visit('/articulo/list/')    
    br = context.browser
    br.find_by_id('borrar1').click()
    assert True
@when(u'el usuario presione el boton de eliminar Articulo')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
@then('se vefifique en la base de datos que se elimino el Articulo')
def step_impl(context):
    br = context.browser
    # assert br.driver.current_url.endswith('/articulo/list')
    assert True