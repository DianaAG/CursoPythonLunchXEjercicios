# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
speed = 40
size = 50
if speed > 25 and size > 25: print("Hay peligro inmimnente de caida de un asteroide en la tierra")
elif speed >= 20: print("Se puede observar como cae un asteroide")
elif size < 25: print("Todo normal")
else: print("Todo normal")