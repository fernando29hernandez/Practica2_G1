Feature: Crear Cuenta

    Scenario: Agregar producto al carrito
        Given el usuario debe estar logueado
        When vea la pagina principal
        When se diriga a la pagina de productos
        Then le de agregar al articulo
        
    Scenario: Comprar articulos
    	Given el usuario debe estar logueado para ver carrito
    	When vea la pagina del carrito
    	Then le de comprar al lo que esta en el carrito