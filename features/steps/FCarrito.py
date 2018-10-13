from behave import * 
from browser import Browser
from selenium import webdriver

@given(u'el usuario debe estar logueado para agregar')
def impl(context):
    context.browser.visit('/accounts/loggedin/')  
    assert True
@when(u'vea la pagina principal para agregar')
def step_impl(context):  
    context.browser.visit('/accounts/loggedin/')  
    assert True
@when(u'se diriga a la pagina de productos para agregar')
def step_impl(context):
    context.browser.visit('/listarArticulos/lista/')
    assert True
@then('le de agregar al articulo para agregar al carrito')
def step_impl(context):
    br = context.browser
    br.find_by_name('1submit').click()

@given(u'el usuario debe estar logueado para ver carrito')
def impl(context):
    context.browser.visit('/accounts/loggedin/')
    assert True
@when(u'vea la pagina del carrito')
def step_impl(context):
    context.browser.visit('/carrito/list')
    assert True
@then(u'le de comprar al lo que esta en el carrito')
def step_impl(context):
    br = context.browser
    br.find_by_name('comprar').click()
