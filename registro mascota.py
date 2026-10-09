nombre_mascotas=[""]*3
edad_mascotas=[0]*3

def insertar():
   for i in range ((nombre_mascotas)):
      nombre_mascotas[i]=input(f"ingrese nombre mascota:")
      edad_mascotas[i]=int(input(f"ingrese edad mascota:"))

def main():
    global nombre_mascota, edad_mascotas
    nombre_mascota=[""]*3
    edad_mascotas=[0]*3

    opcion=0
    while opcion !=4:
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Insertar macotas (nombre | edad")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] salir")
        opcion = int (input("elijo una opción"))
    if opcion ==1:
        insertar()
    elif opcion ==2:
        print ("Mostrar")
    elif opcion == 3:
        print("eliminar")
    elif opcion ==4:
        print("saliendo...")
    else: print ("opcion invalida")
 
