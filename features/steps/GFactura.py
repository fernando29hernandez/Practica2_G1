from behave import * 
from browser import Browser
from selenium import webdriver

@given(u'el usuario debe estar logueado para ver factura')
def impl(context):
    context.browser.visit('/accounts/loggedin/')  
    assert True
@when(u'el usuario vea la pagina principal')
def step_impl(context):  
    context.browser.visit('/accounts/loggedin/')  
    assert True
@when(u'el usuario se diriga a la pagina de productos')
def step_impl(context):
    context.browser.visit('/factura/list/')
    assert True
@then('esta cargue la lista de facturas')
def step_impl(context):
    br = context.browser
    assert br.driver.current_url.endswith('/factura/list/')



