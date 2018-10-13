Feature: Login

    Scenario: Loguearse con usuario incorrecto
      Given el usuario se dirige a la pagina de login2
      When el usuario rellene el campo username con un usuario que no existe
      When el usuario rellene el campo password2
      Then cuando le de aceptar al formulario lo dirige a la pagina de datos incorrectos
    
    Scenario: Loguearse con contrasena incorrecta
      Given el usuario se dirige a la pagina de login3
      When el usuario rellene el campo username2
      When el usuario rellene el campo password con una contrasena incorrecta
      Then cuando le de aceptar al formulario lo dirige a la pagina de datos incorrectos2

    Scenario: Loguearse con usuario creado
      Given el usuario va a la pagina de login
      When el usuario rellene el campo username
      When el usuario rellene el campo password
      Then le de aceptar al formulario y se vea la pagina principal