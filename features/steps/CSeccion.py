from behave import * 
from browser import Browser
from selenium import webdriver

@given(u'el usuario va a la pagina de crear seccion')
def impl(context):
    context.browser.visit('/seccion/add/')  
    assert True

@when(u'el usuario rellene el campo nombre de seccion')
def step_impl(context):  
    username_field = context.browser.find_by_name("nombre")
    username_field.send_keys('Electrodomesticos')
@when(u'el usuario rellene el campo descripcion')
def step_impl(context):  
    password_field = context.browser.find_by_name("descripcion")
    password_field.send_keys('Seccion de electrodomesticos')
@then('le de aceptar al formulario y se cree la seccion')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    assert br.driver.current_url.endswith('/seccion/list/')

@given(u'el usuario va a la pagina de modificar seccion')
def impl(context):
    context.browser.visit('/seccion/list')
    br = context.browser
    br.find_by_id('1').click()
    assert True

@when(u'el usuario rellene el campo nombre para actualizarlo')
def step_impl(context):  
    username_field = context.browser.find_by_name("nombre")
    username_field.send_keys('')
    username_field.send_keys('Miselanea')
@when(u'el usuario rellene el campo descripcion para actualizarlo')
def step_impl(context):  
    password_field = context.browser.find_by_name("descripcion")
    password_field.send_keys('')
    password_field.send_keys('Seccion de Prueba')
@then('le de aceptar al formulario y se actualice la seccion')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/seccion/list/')

@given(u'el usuario va a la pagina de eliminar seccion')
def impl(context):
    context.browser.visit('/seccion/list')
    br = context.browser
    br.find_by_id('borrar1').click()
    assert True
@when('el usuario presione el boton de eliminar seccion')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/seccion/list/')
@then('se vefifique en la base de datos que se elimino la seccion')
def step_impl(context):
    br = context.browser
    assert br.driver.current_url.endswith('/seccion/list/')