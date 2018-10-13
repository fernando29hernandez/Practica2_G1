Feature: Factura
    Scenario: Listar Facturas
      Given el usuario debe estar logueado para ver factura
      When el usuario vea la pagina principal
      When el usuario se diriga a la pagina de productos
      Then esta cargue la lista de facturas