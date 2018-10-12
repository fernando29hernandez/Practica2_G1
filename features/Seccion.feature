Feature: Seccion
    Scenario: Crear seccion
      Given el usuario va a la pagina de crear seccion
      When el usuario rellene el campo nombre de seccion
      When el usuario rellene el campo descripcion
      Then le de aceptar al formulario y se cree la seccion
    Scenario: Modificar seccion
      Given el usuario va a la pagina de modificar seccion 
      When el usuario rellene el campo nombre para actualizarlo
      When el usuario rellene el campo descripcion para actualizarlo
      Then le de aceptar al formulario y se actualice la seccion
    Scenario: Eliminar seccion
      Given el usuario va a la pagina de eliminar seccion
      When el usuario presione el boton de eliminar seccion
      Then se vefifique en la base de datos que se elimino la seccion
