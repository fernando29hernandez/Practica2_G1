Feature: Login

    Scenario: Loguearse con usuario creado
      Given el usuario va a la pagina de login
      When el usuario rellene el campo username
      When el usuario rellene el campo password
      Then le de aceptar al formulario y se vea la pagina principal