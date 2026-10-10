nombre_mascotas=[""]*3
edad_mascotas=[0]*3

def insertar():
   for i in range (len(nombre_mascotas)):
      nombre_mascotas[i]=input(f"ingrese nombre mascota:")
      edad_mascotas[i]=int(input(f"ingrese edad mascota:"))
def mostrar():
    for i in range (len(nombre_mascota)):
        print (f"nombre: {nombre_mascota[i]}, edad: {edad_mascotas[i]}")
def eliminar(nombreAborrar):
    for i in range (len(nombre_mascota)):
        if nombre_mascota[i] == nombreAborrar:
            for j in range (i, len (nombre_mascota)-1):
             nombre_mascota[j] = nombre_mascota[j+1]
             edad_mascotas[j] = edad_mascotas[j+1]
            
             nombre_mascota[-1]=""
             edad_mascotas[-1]= 0
             print (f"mascota eliminada {nombre_mascota[i]}")
def ordenarmascota():
    f
def main():
    global nombre_mascota, edad_mascotas
    nombre_mascota=[""]*3
    edad_mascotas=[0]*3

    opcion=0
    while opcion !=5:
        
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Insertar macotas (nombre | edad")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Ordenar mascotas alfabeticamente")
        print("[5] Salir..")
        opcion = int (input("elijo una opción"))
    if opcion ==1:
        insertar()
    elif opcion ==2:
        mostrar()
    elif opcion == 3:
        mascotaAborrar = input ("Ingrese mascota a borrar")
    elif opcion ==4:
        print("Ordenar")
    elif opcion ==5:
        print("Salir")
    else: print ("opcion invalida")
    if opcion !=5: int ("Presione para continuar..")
