Feature: Crear Cuenta

    Scenario: Agregar producto al carrito
        Given el usuario debe estar logueado para agregar
        When vea la pagina principal para agregar
        When se diriga a la pagina de productos para agregar
        Then le de agregar al articulo para agregar al carrito
        
    Scenario: Comprar articulos
    	Given el usuario debe estar logueado para ver carrito
    	When vea la pagina del carrito
    	Then le de comprar al lo que esta en el carrito