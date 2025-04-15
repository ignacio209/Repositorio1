def verificar_contraseña(contraseña):
  contraseña_ingresada = input("Ingrese la contraseña: ")
  if contraseña_ingresada == contraseña:
    print("Contraseña correcta")
    print("Contraseña Correcta. Bienvenido.")
    return True
  else:
    print("Contraseña Incorrecta. NO PUEDE PASAR.")
    return False

Contraseña_objetivo = "01022019"
verificar_contraseña(Contraseña_objetivo)

if verificar_contraseña(Contraseña_objetivo):
  print("Acceso concedido.")
else:
  print("Intente nuevamente o Error al ingresar contraseña.")