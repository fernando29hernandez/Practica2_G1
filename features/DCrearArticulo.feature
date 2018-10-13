Feature: Crear Articulo

    Scenario: Ingresar un nuevo Articulo
        Given el usuario va a la pagina de ingresar un Articulo
        When el usuario llene el campo nombre
        When el usuario llene el campo descripcion
        When el usuario llene el campo precio
        When el usuario llene el campo seccion_fk
        Then le de aceptar al formulario y se cree el Articulo

    Scenario: Modificar Articulo
        Given el usuario va a la pagina de modificar un Articulo
        When el usuario llene el campo nombre para actualizar
        When el usuario llene el campo descripcion para actualizar
        When el usuario llene el campo precio para actualizar
        When el usuario llene el campo seccion_fk para actualizar
        Then le de aceptar al formulario y se actualice el Articulo
    
    Scenario: Eliminar Articulo
        Given el usuario va a la pagina para eliminar un Articulo
        When el usuario presione el boton de eliminar Articulo
        Then se vefifique en la base de datos que se elimino el Articulo