from behave import * 
from browser import Browser
from selenium import webdriver

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
