""""
Crear una clase de Python llamada Usuario 
que use el método init y cree un nombre de usuario y una contraseña.
Crea un objeto usando la clase.
"""




class Usuario:
   
    def __init__(self, nombre_usuario, contraseña):
       
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Creando el objeto que use la clase Usuario
usuario1 = Usuario("Sammy_Dutton", "catworld1330")

# Accediendo a los atributos del objeto
print(f"Nombre de usuario: {usuario1.nombre_usuario}")
print(f"Contraseña: {usuario1.contraseña}")


