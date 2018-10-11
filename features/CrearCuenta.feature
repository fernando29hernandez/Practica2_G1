Feature: Crear Cuenta

    Scenario: Crear cuenta usuario normal
      Given el usuario va a la pagina de crearcuenta
      When el usuario rellene el campo usuario
      When el usuario rellene el campo contrasena
      When el usuario rellene el campo nombre 
      When el usuario rellene el campo Apellido
      When el usuario rellene el campo correo
      Then le de aceptar al formulario y se cree la cuenta