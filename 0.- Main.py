"""

Aqui vamos a poner el menu principal que de acceso a las diferentes funciones.

1.- Ver mapa de puntos de medida.

2.- Ver datos que ofrece cada punto de medida

3.- Acceder a los valores horarios de un punto de medición dado en un periodo de tiempo dado.

  Periodo de tiempo: desde yyyy-mm-dd-hh hasta yyyy-mm-dd-hh
  Retornará los valores medios de cada una de las horas del día (la media de los cuatro valores horarios) en el medidor dado.
  
  Sirve básicamente para poder acceder a los datos de una forma ordenada.
  

4.- Acceder a la media de los valores horarios de un punto de medición dado en un periodo de tiempo dado.

  Periodo de tiempo: desde yyyy-mm-dd-hh hasta yyyy-mm-dd-hh
  Retornará un valor medio de todas las mediciones horarias comprendidas en el rango de tiempo dado.
  
  Sirve para medir la imd media en periodos de tiempo determinados (un día concreto, una hora concreta, horas punta…)
  

5.- Comparador de valores horarios entre dos puntos de medición dados en un periodo de tiempo dado.

  Periodo de tiempo: desde yyyy-mm-dd-hh hasta yyyy-mm-dd-hh.
  Retornará los valores medios de cada una de las horas del día en ambos medidores con la variación en %.

6.- Comparador de la media de los valores horarios de dos puntos de medición dados en un periodo de tiempo dado.

  Periodo de tiempo: desde yyyy-mm-dd-hh hasta yyyy-mm-dd-hh.
  Retornará la media de ambos puntos en el periodo de tiempo dado acompañado de su variación en %.


"""

from io import open
from Modulos.Modulos import *
import os.path
import os
import openpyxl
from openpyxl import Workbook

seguimos=True

while(seguimos):


  opcion=0
  error_cont=0
  ruta_main=os.path.dirname(os.path.abspath(__file__))


  print ("*** Visor de datos de tráfico de Madrid ***")
  print("\nMENU PRINCIPAL:")
  
  print("\n1.- Ver el mapa de medidores.")
  print("2.- Ver definicion de los datos")
  print("3.- Acceder a los los valores de un punto concreto en un periodo de tiempo.")
  print("4.- Comparar los valores de un punto en concreto en un periodo de x días a partir de dos días dados.")
  print("5.- Media de los valores de un punto concreto en un periodo de tiempo.")
  print("6.- Comparar la media de los valores de un punto concreto en un periodo de tiempo.")
  print("7.- Salir")
  print("\nSomos conscientes del tema tildes :( Estamos trabajando en ello.")


  while(opcion<1 or opcion>7):
    try:
      opcion=int(input("\nElige una opción: "))
      if (opcion<1 or opcion>7):
        print("No valido. Elige una opción entre 1 y 7.")
    except ValueError:
      error_cont+=1
      if error_cont==15:
        print("Ánimo, sigue intentándolo.")
      elif error_cont==30:
        print("Nope.")
      elif error_cont==45:
        print("Si quieres resultados distintos, prueba con algo diferente.")
    print("\n")

#--------------------------------------------------------------------------------------------------

  if(opcion==1):
    print("Es mentira, el mapa no está listo, pero podemos mostrar una lista de todos los medidores")
    print("\n¿Quieres ver la lista de medidores? S/N")
    print("\nOjo, que son bastantes y la cosa tarda lo suyo.\n")
    pide_opcion1=True

    #Esto de pedir si/no lo podriamos transformar en funcion.

    while(pide_opcion1):
      op1_op=input("")
      print("\n")
      if(op1_op=="S" or op1_op=="s" or op1_op=="Si" or op1_op=="si"):
        pide_opcion1=False
        lista=cargar_datos_espiras_lista()
        #print(f'Total score for {name} is {score}')
        for i in lista:
          print(f"Código del medidor: {i[0]}. Tipo: {i[2]}. Descripción: {i[1]}")


      elif(op1_op=="N" or op1_op=="n" or op1_op=="No" or op1_op=="no"):
        pide_opcion1=False

    print("\n\n")

#--------------------------------------------------------------------------------------------------
  
  if(opcion==2):
    print("Aqui debería ir una explicación detallada de:")
    print("- La red de medición")
    print("- Los tipos de medidores")
    print("- La información que da cada medidor")
    print("- Qué tratamiento tienen y para qué se usan los datos")

    print("\n\n")

#--------------------------------------------------------------------------------------------------

  if(opcion==3):  #Acceder a los los valores de un punto concreto en un periodo de tiempo

    medidor3=0 #medidor de la opción 3, por si utilizamos otras variables medidor en el programa, para que esta quede limpia.

    print("")

    while (medidor3==0): #or not(comprobar_medidor(medidor))): #un comprobar medidor de un medidor valido nos daria true, por eso lo negamos, para que no entre en el bucle si el medidor es correcto, la función está por hacer
      try:
        medidor3=int(input("Introduce un codigo de medidor valido: "))
      except ValueError:
        pass

    #Llamamos a pidedias
    fechas3=pide_dias() # que nos devuelve esto:  [anio_inicial, mes_inicial, dia_inicial, hora_inicial, anio_final, mes_final, dia_final, hora_final]
    #Llamamos a genera_fechas, que nos pide       (anio_inicial, mes_inicial, dia_inicial, hora_inicial, anio_final, mes_final, dia_final, hora_final)  ->  Lista de listas: [año] [mes] [dia] [hora inicial] [hora final]
    lista_fechas3=genera_fechas(fechas3[0],fechas3[1],fechas3[2],fechas3[3],fechas3[4],fechas3[5],fechas3[6],fechas3[7])
    print("")

    #aqui gestionamos cómo va a querer el usuario que se muestren los datos, si en mediciones horarias o cada 15 minutos

    minutos3=True

    operador3=0

    while (operador3!=1 and operador3!=2):
      try:
        operador3=int(input("\n1.- Mostrar el resultado en mediciones cada 15 minutos\n2.- Mostrar el resultado horario\n"))
      except ValueError:
        pass

    if (operador3==2):
      minutos3=False



    #Ya tenemos el código del medidor en medidor3 y la lista de fechas del periodo en lista_fechas3, ahora accedemos a los datos y los imprimimos en pantalla.
    #Para ello utilizamos la función extrae líneas y la función genera_ruta

    """
     def extrae_lineas(codigo, ruta_archivo, hora_inicial, hora_final): -> lista de listas donde cada línea es:

     [0]clave          int
     [1]fecha_anio     int
     [2fecha_mes       int
     [3]fecha_dia      int 
     [4]fecha_hora     int
     [5]fecha_minuto   int
     [6]=descripcion   string
     [7]=intensidad    int
     [8]=ocupacion     int
     [9]=carga         int
     [10]=vmed         int
     [11]=error        string
     [12]=periodo      int
    """
    # def genera_ruta_archivo(anio, mes, dia, ruta_main): -> "Directorio del main"\\Datos Trafico Madrid\\Febrero 2018\\2018-02-03

    for i in lista_fechas3:
      rutai=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) #genera_ruta_archivo(año, mes, dia, ruta_main)
      listai=extrae_lineas(medidor3, rutai, i[3], i[4])

      if(minutos3):
        for j in listai:
          print(f"El medidor {medidor3} el día {j[3]} del mes {j[2]} del año {j[1]} a las {j[4]} horas y {j[5]} minutos tuvo unas mediciones de {j[7]} intensidad, {j[8]} ocupación, {j[9]} carga y {j[10]} velocidad media")

      else: #Aquí habría que hacer una nueva llamada a la función agrupar_mediciones_horarias(lista_origen): -> lista de listas con los valores horarios
        lista_horariai=agrupar_mediciones_horarias(listai)
        for j in lista_horariai:
          print(f"El medidor {medidor3} el día {j[3]} del mes {j[2]} del año {j[1]} a las {j[4]} horas tuvo unas mediciones de {j[7]} intensidad, {j[8]} ocupación, {j[9]} carga y {j[10]} velocidad media con {j[13]} mediciones en esa hora.")


    print("\n\n")


    operador_hoja_de_calculo3=0
    sacar_a_hoja_de_calculo3=False

    while (operador_hoja_de_calculo3!=1 and operador_hoja_de_calculo3!=2):
      try:
        operador_hoja_de_calculo3=int(input("\n1.-Copiar el resultado en un archivo de hoja de cálculo?\n2.-No, con esto me vale.\n"))
      except ValueError:
        pass

    if (operador_hoja_de_calculo3==1):
      sacar_a_hoja_de_calculo3=True

    if(sacar_a_hoja_de_calculo3):
      if(minutos3):
        print("Generando archivo de mediciones.")
        Lista_minutos_a_hoja_de_calculo(medidor3, fechas3, listai, ruta_main)
      else:
        print("Generando archivo de mediciones horarias.")
        Lista_horaria_a_hoja_de_calculo(medidor3, fechas3, lista_horariai, ruta_main)

    print("\n\n")


#-------------------------------------------------------------------------------------------------------------------
    
  if (opcion==4): # Comparar los valores de un punto en concreto en un periodo de x días a partir de dos días dados.

    """
    Pillar los datos del medidor
    Pillar el día 1
    Pillar el día 2
    Pillar el periodo de tiempo (dias)

    Preguntar por los resultados, si en horarias o cada 15 minutos.

    Elaborar la lista de rutas correspondiente a dia 1
    Elaborar la lista de rutas correspondiente a día 2

    Hacer la consulta y guardarla en resultado4_1
    Hacer la consulta y guardarla en resultado4_2

   

    Comprobar que el número de mediciones es igual

    Montar la salida

    """

    #Pedimos los datos

    medidor4=0

    while (medidor4==0): #or not(comprobar_medidor(medidor))): #un comprobar medidor de un medidor valido nos daria true, por eso lo negamos, para que no entre en el bucle si el medidor es correcto, la función está por hacer
        try:
          medidor4=int(input("Introduce un codigo de medidor valido: "))
        except ValueError:
          pass

    print("Te vamos a pedir la primera fecha: \n")
    fecha4_1=pide_solo_fecha()
    print("\n")

    print("Te vamos a pedir la segunda fecha")
    fecha4_2=pide_solo_fecha()
    print("\n")

    n_dias4=0

    while(n_dias4<=0):
      try:
        n_dias4=int(input("¿Qué cantidad de días quieres comparar? (si pones 1 será un único día) \n"))
      except ValueError:
        pass


    minutos4=True

    operador4=0

    while (operador4!=1 and operador4!=2):
      try:
        operador4=int(input("\n1.- Mostrar el resultado en mediciones cada 15 minutos\n2.- Mostrar el resultado horario \n"))
      except ValueError:
        pass

    if (operador4==2):
      minutos4=False


    #Elaborar la lista de rutas correspondiente a dia 1
    #Elaborar la lista de rutas correspondiente a día 2
    #Los días los tenemos en una lista tipo [año, mes, día]
    #Elaboramos una lista con todos los días

    lista_dias4_1=[] #inicializamos las listas y les añadimos los 
    lista_dias4_1.append(fecha4_1)
    dia_actual4_1=fecha4_1

    lista_dias4_2=[]
    lista_dias4_2.append(fecha4_2)
    dia_actual4_2=fecha4_2

    dia_aux4=[]

    for i in range(n_dias4-1): #llamamos a suma_dia(año, mes, día) -> [año, mes, día]
      dia_actual4_1=suma_dia(dia_actual4_1[0], dia_actual4_1[1], dia_actual4_1[2]) #actualizamos el día_actual con el día siguiente
      lista_dias4_1.append(dia_actual4_1) #y lo añadimos a la lista

      dia_actual4_2=suma_dia(dia_actual4_2[0], dia_actual4_2[1], dia_actual4_2[2]) #actualizamos el día_actual con el día siguiente
      lista_dias4_2.append(dia_actual4_2) #y lo añadimos a la lista

    #Teniendo ya la lista de fechas ya podemos generar las rutas y las listas resultado correspondientes.

    # def genera_ruta_archivo(anio, mes, dia, ruta_main): -> "Directorio del main"\\Datos Trafico Madrid\\Febrero 2018\\2018-02-03

    lista_resultado4_1=[] #aqui guardaremos el conjunto de listas que corresponden a la medición de los sucesivos días en formato medición 15 minutos
    lista_resultado4_2=[]

    for i in lista_dias4_1:
      lista_aux4_1=[]
      ruta4_i=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) #genera_ruta_archivo(año, mes, dia, ruta_main)
      lista_aux4_1=extrae_lineas(medidor4, ruta4_i, 0, 23) #(codigo, ruta_archivo, hora_inicial, hora_final), nos genera una lista de listas
      for j in lista_aux4_1:
        lista_resultado4_1.append(j) #pasamos cada una de las lineas a la lista resultado

    for i in lista_dias4_2:
      lista_aux4_2=[]
      ruta4_i=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) #genera_ruta_archivo(año, mes, dia, ruta_main)
      lista_aux4_2=extrae_lineas(medidor4, ruta4_i, 0, 23) #(codigo, ruta_archivo, hora_inicial, hora_final), nos genera una lista de listas
      for j in lista_aux4_2:
        lista_resultado4_2.append(j) #pasamos cada una de las lineas a la lista resultado

    longitud4_1=len(lista_resultado4_1)
    longitud4_2=len(lista_resultado4_2)

    if(longitud4_1!=longitud4_2 and minutos4):
      print("OJO, el número de mediciones de ambos periodos es distinto :(\n")

    print(f"\nDatos comparativos del medidor {medidor4}\n")

    if(minutos4): #ahora hay que resolver el cacao de cómo presentar los datos porque tenemos que ir recorriendo dos listas a la vez sin tener garantías de que tengan el mismo número de mediciones.
      for j in range(longitud4_1):
        varia_intensidad=(lista_resultado4_1[j][7]-lista_resultado4_2[j][7])
        varia_ocupacion=(lista_resultado4_1[j][8]-lista_resultado4_2[j][8])
        varia_carga=(lista_resultado4_1[j][9]-lista_resultado4_2[j][9])

        print(f"{lista_resultado4_1[j][3]}:{lista_resultado4_1[j][2]}:{lista_resultado4_1[j][1]} - {lista_resultado4_1[j][4]}:{lista_resultado4_1[j][5]} Intensidad={lista_resultado4_1[j][7]} Ocupación={lista_resultado4_1[j][8]} Carga={lista_resultado4_1[j][9]}\n{lista_resultado4_2[j][3]}:{lista_resultado4_2[j][2]}:{lista_resultado4_2[j][1]} - {lista_resultado4_2[j][4]}:{lista_resultado4_2[j][5]} Intensidad={lista_resultado4_2[j][7]} Ocupación={lista_resultado4_2[j][8]} Carga={lista_resultado4_2[j][9]}")
        print(f"Variación: Intensidad {varia_intensidad}  Carga {varia_carga}  Ocupación {varia_ocupacion} \n")


    else: #Aquí habría que hacer una nueva llamada a la función agrupar_mediciones_horarias(lista_origen): -> lista de listas con los valores horarios
      lista_horaria4_1=agrupar_mediciones_horarias(lista_resultado4_1)
      lista_horaria4_2=agrupar_mediciones_horarias(lista_resultado4_2)

      longitud_horaria4_1=len(lista_horaria4_1)
      longitud_horaria4_2=len(lista_horaria4_2)

      if(longitud_horaria4_1!=longitud_horaria4_2):
        print("OJO, el número de mediciones de ambos periodos es distinto :(\n")

      for j in range(longitud_horaria4_1):
        varia_intensidad=(lista_horaria4_1[j][7]-lista_horaria4_2[j][7])
        varia_ocupacion=(lista_horaria4_1[j][8]-lista_horaria4_2[j][8])
        varia_carga=(lista_horaria4_1[j][9]-lista_horaria4_2[j][9])

        print(f"{lista_horaria4_1[j][3]}:{lista_horaria4_1[j][2]}:{lista_horaria4_1[j][1]} - {lista_horaria4_1[j][4]} horas. Intensidad={lista_horaria4_1[j][7]} Ocupación={lista_horaria4_1[j][8]} Carga={lista_horaria4_1[j][9]}\n{lista_horaria4_2[j][3]}:{lista_horaria4_2[j][2]}:{lista_horaria4_2[j][1]} - {lista_horaria4_2[j][4]} horas. Intensidad={lista_horaria4_2[j][7]} Ocupación={lista_horaria4_2[j][8]} Carga={lista_horaria4_2[j][9]}")
        print(f"Variación: Intensidad {varia_intensidad}  Carga {varia_carga}  Ocupación {varia_ocupacion} \n")

    print("\n\n")
        


  #-------------------------------------------------------------------------------

  if (opcion==5): #Media de los valores de un punto concreto en un periodo de tiempo."

    """
    Pedir medidor
    Pedir periodo
    Hacer la consulta
    Inicializar los acumuladores
    Inicializar el contador de mediciones
    Recorrer la lista 
    Si no hay error en la medición, se suma a los acumuladores y al contador
    Se dividen los acumuladores por el contador y esa es la media.


    """

    medidor5=0

    lineas_resultado_5=[]

    while (medidor5==0): #or not(comprobar_medidor(medidor))): #un comprobar medidor de un medidor valido nos daria true, por eso lo negamos, para que no entre en el bucle si el medidor es correcto, la función está por hacer
      try:
        medidor5=int(input("Introduce un codigo de medidor valido: "))
      except ValueError:
        pass

    fechas5=pide_dias() # que nos devuelve esto:  [anio_inicial, mes_inicial, dia_inicial, hora_inicial, anio_final, mes_final, dia_final, hora_final]

    #Llamamos a genera_fechas, que nos pide       (anio_inicial, mes_inicial, dia_inicial, hora_inicial, anio_final, mes_final, dia_final, hora_final)  ->  Lista de listas: [año] [mes] [dia] [hora inicial] [hora final]
    lista_fechas5=genera_fechas(fechas5[0],fechas5[1],fechas5[2],fechas5[3],fechas5[4],fechas5[5],fechas5[6],fechas5[7])

    for i in lista_fechas5:
      rutai=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) #genera_ruta_archivo(año, mes, dia, ruta_main)
      listai=extrae_lineas(medidor5, rutai, i[3], i[4]) #(medidor, ruta archivo diario, hora inicial, hora final) -> lista de listas con los valores cada 15 minutos (12 campos)
      for j in listai:
        lineas_resultado_5.append(j) #Añadimos cada línea de medición a la lista final, que es con la que haremos la media final.

    #En lineas_resultado_5 tenemos todas las mediciones cada 15 minutos, formato 12 campos. La recorremos con los acumuladores y hacemos las medias.

    acum_intensidad5=0
    acum_carga5=0
    acum_ocupacion5=0

    lecturas_error=0

    contador5=0
    
    for i in lineas_resultado_5:

      if i[11]=="N":
        acum_intensidad5+=i[7]
        acum_ocupacion5+=i[8]
        acum_carga5+=i[9]
        contador5+=1
      elif i[11]=="Y":
        lecturas_error+=1
      
    
    try:
      intensidad_final5=acum_intensidad5/contador5
    except ZeroDivisionError:
      intensidad_final5=0
      print("Algo raro ha pasado con las mediciones de intensidad, no hay mediciones válidas.")

    try: 
      ocupacion_final5=acum_ocupacion5/contador5
    except ZeroDivisionError:
      ocupacion_final5=0
      print("Algo raro ha pasado con las mediciones de ocupación, no hay mediciones válidas.")

    try:
      carga_final5=acum_carga5/contador5
    except ZeroDivisionError:
      carga_final5=0
      print("Algo raro ha pasado con las mediciones de carga, no hay mediciones válidas.")

    intensidad_final5=round(intensidad_final5,2)
    ocupacion_final5=round(ocupacion_final5,2)
    carga_final5=round(carga_final5,2)
    


    print(f"\nValores medios del medidor {medidor5} desde {fechas5[2]}-{fechas5[1]}-{fechas5[0]} a las {fechas5[3]}:00 hasta {fechas5[6]}-{fechas5[5]}-{fechas5[4]} a las {fechas5[7]}:00 ")
    print(f"\nIntendidad media: {intensidad_final5}. Ocupación media: {ocupacion_final5}. Carga media: {carga_final5}")
    print(f"\nNúmero de mediciones: {contador5}. Número de errores: {lecturas_error}")

    print("\n\n")

  
  #-------------------------------------------------------------------------------

  if (opcion==6): #Comparar la media de los valores de un punto concreto en un periodo de tiempo.

    #Es básicamente hacer dos veces lo que hacemos en el apartado 5 y luego comparar resultados.

    medidor6=0

    lineas_resultado6_1=[] #resultados del primer periodo
    lineas_resultado6_2=[] #resultados del segundo periodo

    while (medidor6==0): #or not(comprobar_medidor(medidor))): #un comprobar medidor de un medidor valido nos daria true, por eso lo negamos, para que no entre en el bucle si el medidor es correcto, la función está por hacer
      try:
        medidor6=int(input("Introduce un codigo de medidor valido: "))
      except ValueError:
        pass

    print("\nTe vamos a pedir el primer periodo de tiempo")

    periodo_inicial6=pide_dias()

    print("\nA continuación te vamos a pedir el segundo periodo de tiempo")
    print(f"\n Recordatorio, el primer periodo de tiempo es desde {periodo_inicial6[2]}-{periodo_inicial6[1]}-{periodo_inicial6[0]} a las {periodo_inicial6[3]}:00 hasta {periodo_inicial6[6]}-{periodo_inicial6[5]}-{periodo_inicial6[4]} a las {periodo_inicial6[7]}:00")

    periodo_final6=pide_dias()

    lista_fechas_inicial6=genera_fechas(periodo_inicial6[0],periodo_inicial6[1],periodo_inicial6[2],periodo_inicial6[3],periodo_inicial6[4],periodo_inicial6[5],periodo_inicial6[6],periodo_inicial6[7])

    lista_fechas_final6=genera_fechas(periodo_final6[0],periodo_final6[1],periodo_final6[2],periodo_final6[3],periodo_final6[4],periodo_final6[5],periodo_final6[6],periodo_final6[7])

    for i in lista_fechas_inicial6:
      rutai=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) 
      listai=extrae_lineas(medidor6, rutai, i[3], i[4]) 
      for j in listai:
        lineas_resultado6_1.append(j)

    for i in lista_fechas_final6:
      rutai=genera_ruta_archivo(i[0], i[1], i[2], ruta_main) 
      listai=extrae_lineas(medidor6, rutai, i[3], i[4]) 
      for j in listai:
        lineas_resultado6_2.append(j)


    #Hacemos las medias


    #1

    acum_intensidad6_1=0
    acum_carga6_1=0
    acum_ocupacion6_1=0

    lecturas_error6_1=0
    contador6_1=0

    for i in lineas_resultado6_1:

      if i[11]=="N":
        acum_intensidad6_1+=i[7]
        acum_ocupacion6_1+=i[8]
        acum_carga6_1+=i[9]
        contador6_1+=1
      elif i[11]=="Y":
        lecturas_error6_1+=1

    try:
      intensidad_final6_1=acum_intensidad6_1/contador6_1
    except ZeroDivisionError:
      intensidad_final6_1=0
      print("Algo raro ha pasado con las mediciones de intensidad del primer periodo, no hay mediciones válidas.")

    try: 
      ocupacion_final6_1=acum_ocupacion6_1/contador6_1
    except ZeroDivisionError:
      ocupacion_final6_1=0
      print("Algo raro ha pasado con las mediciones de ocupación del primer periodo, no hay mediciones válidas.")

    try:
      carga_final6_1=acum_carga6_1/contador6_1
    except ZeroDivisionError:
      carga_final6_1=0
      print("Algo raro ha pasado con las mediciones de carga del primer periodo, no hay mediciones válidas.")

    intensidad_final6_1=round(intensidad_final6_1,2)
    ocupacion_final6_1=round(ocupacion_final6_1,2)
    carga_final6_1=round(carga_final6_1,2)


    #2

    acum_intensidad6_2=0
    acum_carga6_2=0
    acum_ocupacion6_2=0

    lecturas_error6_2=0
    contador6_2=0

    for i in lineas_resultado6_2:

      if i[11]=="N":
        acum_intensidad6_2+=i[7]
        acum_ocupacion6_2+=i[8]
        acum_carga6_2+=i[9]
        contador6_2+=1
      elif i[11]=="Y":
        lecturas_error6_2+=1

    try:
      intensidad_final6_2=acum_intensidad6_2/contador6_2
    except ZeroDivisionError:
      intensidad_final6_2=0
      print("Algo raro ha pasado con las mediciones de intensidad del segundo periodo, no hay mediciones válidas.")

    try: 
      ocupacion_final6_2=acum_ocupacion6_2/contador6_2
    except ZeroDivisionError:
      ocupacion_final6_2=0
      print("Algo raro ha pasado con las mediciones de ocupación del segundo periodo, no hay mediciones válidas.")

    try:
      carga_final6_2=acum_carga6_2/contador6_2
    except ZeroDivisionError:
      carga_final6_2=0
      print("Algo raro ha pasado con las mediciones de carga del segundo periodo, no hay mediciones válidas.")

    intensidad_final6_2=round(intensidad_final6_2,2)
    ocupacion_final6_2=round(ocupacion_final6_2,2)
    carga_final6_2=round(carga_final6_2,2)


    #Visualizar los resultados:

    #Mostrar media del primer periodo
    #Mostrar media del segundo periodo

    #Mostrar comparativa de ambos periodos.

    print(f"\nValores medios del medidor {medidor6} desde {periodo_inicial6[2]}-{periodo_inicial6[1]}-{periodo_inicial6[0]} a las {periodo_inicial6[3]}:00 hasta {periodo_inicial6[6]}-{periodo_inicial6[5]}-{periodo_inicial6[4]} a las {periodo_inicial6[7]}:00 ")
    print(f"\nIntendidad media: {intensidad_final6_1}. Ocupación media: {ocupacion_final6_1}. Carga media: {carga_final6_1}")
    print(f"\nNúmero de mediciones: {contador6_1}. Número de errores: {lecturas_error6_1}")

    print(f"\nValores medios del medidor {medidor6} desde {periodo_final6[2]}-{periodo_final6[1]}-{periodo_final6[0]} a las {periodo_final6[3]}:00 hasta {periodo_final6[6]}-{periodo_final6[5]}-{periodo_final6[4]} a las {periodo_final6[7]}:00 ")
    print(f"\nIntendidad media: {intensidad_final6_2}. Ocupación media: {ocupacion_final6_2}. Carga media: {carga_final6_2}")
    print(f"\nNúmero de mediciones: {contador6_2}. Número de errores: {lecturas_error6_2}")

    variacion_intensidad6=0
    variacion_ocupacion6=0
    variacion_carga6=0

    if(intensidad_final6_2>0 and intensidad_final6_1>0):
      variacion_intensidad6=round((((intensidad_final6_1-intensidad_final6_2)/intensidad_final6_1)*100)*-1,2) #el -1 es para que salga bien el signo de la variación

    if(ocupacion_final6_2>0 and ocupacion_final6_1>0):
      variacion_ocupacion6=round((((ocupacion_final6_1-ocupacion_final6_2)/ocupacion_final6_1)*100)*-1,2)

    if(carga_final6_2>0 and carga_final6_1>0):
      variacion_carga6=round((((carga_final6_1-carga_final6_2)/carga_final6_1)*100)*-1, 2)


    print(f"\nVariación:\nIntensidad: {variacion_intensidad6}%\nOcupación: {variacion_ocupacion6}%\nCarga: {variacion_carga6}%")

    print("\n\n")


  #-------------------------------------------------------------------------------

  if (opcion==7):
    print("Adiooooooos")
    seguimos=False


