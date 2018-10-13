from behave import * 
from browser import Browser
from selenium import webdriver

@given(u'el usuario debe estar logueado para listar productos')
def impl(context):
    context.browser.visit('/accounts/loggedin')  
    assert True
@when(u'vea la pagina principal para listar productos')
def step_impl(context):  
    context.browser.visit('/accounts/loggedin')  
    assert True
@then(u'se dirige a la pagina de listar productos')
def step_impl(context):  
    context.browser.visit('/listarArticulos/lista/')
    assert True
  

