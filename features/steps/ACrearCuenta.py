from behave import * 
from browser import Browser
from selenium import webdriver

@given(u'el usuario va a la pagina de crearcuenta')
def impl(context):
    context.browser.visit('/crearUsuario/')  
    assert True

@when(u'el usuario rellene el campo usuario')
def step_impl(context):  
    username_field = context.browser.find_by_name("username")
    username_field.send_keys('UsuarioNuevo')
@when(u'el usuario rellene el campo contrasena')
def step_impl(context):  
    password_field = context.browser.find_by_name("password")
    password_field.send_keys('contra123')
@when(u'el usuario rellene el campo nombre')
def step_impl(context):  
    first_name_field = context.browser.find_by_name("first_name")
    first_name_field.send_keys('nombre de usuario')
@when(u'el usuario rellene el campo apellido')
def step_impl(context):  
    last_name_field = context.browser.find_by_name("last_name")
    last_name_field.send_keys('apellido de usuario')
@when(u'el usuario rellene el campo correo')
def step_impl(context):  
    email_field = context.browser.find_by_name("email")
    email_field.send_keys('usuario@gmail.com')
@then('le de aceptar al formulario y se cree la cuenta')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/accounts/login/')

