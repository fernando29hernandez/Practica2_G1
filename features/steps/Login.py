from behave import * 
from browser import Browser
from selenium import webdriver

#Escenario donde se ingresa un usuario que no existe
@given(u'el usuario se dirige a la pagina de login2')
def impl(context):
    context.browser.visit('/accounts/logout/') #Primero me tengo que desloguear de la sesion anterior
    context.browser.visit('/accounts/login/')  
@when(u'el usuario rellene el campo username con un usuario que no existe')
def step_impl(context):  
    username_field = context.browser.find_by_name("username")
    username_field.send_keys('UsuarioInvalido')
@when(u'el usuario rellene el campo password2')
def step_impl(context):  
    password_field = context.browser.find_by_name("password")
    password_field.send_keys('contra123')
@then('cuando le de aceptar al formulario lo dirige a la pagina de datos incorrectos')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/accounts/invalid/')



#Escenario donde se ingresa un usuario correcto, pero contraseña incorrecta
@given(u'el usuario se dirige a la pagina de login3')
def impl(context):
    context.browser.visit('/accounts/logout/') #Primero me tengo que desloguear de la sesion anterior
    context.browser.visit('/accounts/login/')  
@when(u'el usuario rellene el campo username2')
def step_impl(context):  
    username_field = context.browser.find_by_name("username")
    username_field.send_keys('UsuarioNuevo')
@when(u'el usuario rellene el campo password con una contrasena incorrecta')
def step_impl(context):  
    password_field = context.browser.find_by_name("password")
    password_field.send_keys('incorrecta123')
@then('cuando le de aceptar al formulario lo dirige a la pagina de datos incorrectos2')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/accounts/invalid/')




@given(u'el usuario va a la pagina de login')
def impl(context):
    context.browser.visit('/accounts/login/')  
@when(u'el usuario rellene el campo username')
def step_impl(context):  
    username_field = context.browser.find_by_name("username")
    username_field.send_keys('UsuarioNuevo')
@when(u'el usuario rellene el campo password')
def step_impl(context):  
    password_field = context.browser.find_by_name("password")
    password_field.send_keys('contra123')
@then('le de aceptar al formulario y se vea la pagina principal')
def step_impl(context):
    br = context.browser
    br.find_by_name('submit').click()
    # Checks success status
    assert br.driver.current_url.endswith('/accounts/loggedin/')