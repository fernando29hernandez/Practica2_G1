Feature: Listar Articulos

    Scenario: El usuario desea ver la pagina de listar productos
      Given el usuario debe estar logueado para listar productos
      When vea la pagina principal para listar productos
      Then se dirige a la pagina de listar productos