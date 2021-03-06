import tkinter
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from PIL import Image, ImageTk
from html2image import Html2Image
from AFDERRORES import *
import sys
import webbrowser

#Variables Globales
ruta = ''

def Cargar_Archivo():
    global ruta
    print('Se cargara el archivo')
    archivo = filedialog.askopenfilename(title='File Chooser',filetypes=[('Image Files', ['.pxla'])])
    print(archivo)
    ruta = archivo
def Abrir_Archivo(Direccion):
    Dir = str(Direccion)
    primeras_lineas = []
    primeras_lineas_error =[]
    cache = ''
    cache2 = ''
    cache3 = ''
    print('Abriendo Archivo para lectura')
    try:
        file_entrada = open(Dir,'r')
        primera_lectura = file_entrada.read()

        #print(primera_lectura)
    except:
        print('Error al intentar abrir el archivo')
        messagebox.showwarning(message="ERROR al intentar abrir archivo de entrada ", title="ERROR")
    else:
        print('Se logro abrir archivo de entrada con exito')
        messagebox.showinfo(message="Se logro abrir el archivo de entrada", title="CONFIRMACION")
        primeros_caracteres = list(primera_lectura)
        #print(primeros_caracteres)
        # PARA AFD
        for i in range(0,len(primeros_caracteres)):
            if str(primeros_caracteres[i]) != '\n' and str(primeros_caracteres[i]) != '\t':
                if str(primeros_caracteres[i]) != ' ':
                    cache = cache + str(primeros_caracteres[i])
            if str(primeros_caracteres[i]) == '\n' or str(primeros_caracteres[i]==''):
                primeras_lineas.append(cache)
                cache = ''
        #PARA AFD2
        for j in range(0, len(primeros_caracteres)):
            if str(primeros_caracteres[j]) != '' and str(primeros_caracteres[j]) != '\t':
                if str(primeros_caracteres[j]) != ' ':
                    cache2 = cache2 + str(primeros_caracteres[j])
        cache2 = cache2 + '$'
        filtrar_lineas = list(cache2)

        for k in range(0,len(filtrar_lineas)):
            if str(filtrar_lineas[k]) != '\n' and str(filtrar_lineas[k]) != '$':
                cache3 = cache3 + str(filtrar_lineas[k])
            if str(filtrar_lineas[k]) == '\n' or str(filtrar_lineas[k]) == '$':
                primeras_lineas_error.append(cache3)
                cache3 = ''
        #print('lista e', primeras_lineas_error)





        #print('primeras lineas',primeras_lineas)
        return primeras_lineas_error
def Analizar():
    #try:
    dir = ruta
    print('Se analizara el archivo')
    print(dir)
    primeras_lineas = Abrir_Archivo(dir)
    AFD_ERRORES(primeras_lineas)
    AFD(primeras_lineas)



    #except:
        #tkinter.messagebox.showwarning('ERROR','Aun no hay una ruta para analizar ')
def AFD(lista_lineas):
    print('Iniciando Automata')
    lista_lineas = lista_lineas
    listaImagenes = []
    listaFilas2D=['','','','','','','']
    lista2D = []
    CrearUnaLinea = ''

    #print(lista_lineas)
    for h in range(0,len(lista_lineas)):
        CrearUnaLinea = CrearUnaLinea + str(lista_lineas[h])
    CrearUnaLinea = CrearUnaLinea + '$'
    LineaUnica = list(CrearUnaLinea)
    #print('Conjunto de Caracteres:',end='\n')
    #print(LineaUnica)

    # Estados
    estado = 0
    estadoNombre = 0
    estadoAncho = 0
    estadoAlto = 0
    estadoFilas = 0
    estadoColumna = 0
    estadoCelda = 0
    estadoFiltro = 0
    estadoSeparador = 0
    # inicializamos cache
    cacheNombre = ''
    cacheAncho = ''
    cacheAlto = ''
    cacheFilas = ''
    cacheColumna = ''
    cacheCelda = ''
    cacheFiltro = ''
    cacheImagen = ''

    for j in range(0,len(LineaUnica)):
        #print(LineaUnica)
        if estado == 0:
            if str(LineaUnica[j]) != '@':
                cacheImagen = cacheImagen +str(LineaUnica[j])
                estado = 0
            if str(LineaUnica[j]) == '@':
                estado = 1
            if str(LineaUnica[j]) == '$':
                listaImagenes.append(cacheImagen)
                #print(cacheImagen)
                estado = 0
            continue
        if estado == 1:
            if str(LineaUnica[j]) == '@':
                estado = 2
            continue
        if estado == 2:
            if str(LineaUnica[j]) == '@':
                estado = 3
            continue
        if estado == 3:
            if str(LineaUnica[j]) == '@':
                listaImagenes.append(cacheImagen)
                #print(cacheImagen)
                cacheImagen = ''
                estado = 0


    #print(listaImagenes)

    for imagenes in range(0,len(listaImagenes)):
        separarImagenes = list(listaImagenes[imagenes])
        for separacion in range(0,len(separarImagenes)):
            if estadoNombre == 0:
                if str(separarImagenes[separacion]) == 'T':
                    estadoNombre = 1
                continue
            if estadoNombre == 1:
                if str(separarImagenes[separacion]) == 'I':
                    estadoNombre = 2
                continue
            if estadoNombre == 2:
                if str(separarImagenes[separacion]) == 'T':
                    estadoNombre = 3
                continue
            if estadoNombre == 3:
                if str(separarImagenes[separacion]) == 'U':
                    estadoNombre = 4
                continue
            if estadoNombre == 4:
                if str(separarImagenes[separacion]) == 'L':
                    estadoNombre = 5
                continue
            if estadoNombre == 5:
                if str(separarImagenes[separacion]) == 'O':
                    estadoNombre = 6
                continue
            if estadoNombre == 6:
                if str(separarImagenes[separacion]) == '=':
                    estadoNombre = 7
                continue
            if estadoNombre == 7:
                if str(separarImagenes[separacion]) == '"':
                    estadoNombre = 8
                continue
            if estadoNombre == 8:
                if str(separarImagenes[separacion]) != '"':
                    cacheNombre = cacheNombre + str(separarImagenes[separacion])
                    estadoNombre = 8
                if str(separarImagenes[separacion]) == '"':
                    estadoNombre = 9
                continue
            if estadoNombre == 9:
                if str(separarImagenes[separacion]) == ';':
                    #print('este es el cache Nombre', cacheNombre)
                    listaFilas2D[0] = cacheNombre
                    cacheNombre = ''
                    estadoNombre = 0
                continue
        for ancho in range(0, len(separarImagenes)):
            if estadoAncho == 0:
                if str(separarImagenes[ancho]) == 'A':
                    estadoAncho = 1
                continue
            if estadoAncho == 1:
                if str(separarImagenes[ancho]) == 'N':
                    estadoAncho = 2
                continue
            if estadoAncho == 2:
                if str(separarImagenes[ancho]) == 'C':
                    estadoAncho = 3
                continue
            if estadoAncho == 3:
                if str(separarImagenes[ancho]) == 'H':
                    estadoAncho = 4
                continue
            if estadoAncho == 4:
                if str(separarImagenes[ancho]) == 'O':
                    estadoAncho = 5
                continue
            if estadoAncho == 5:
                if str(separarImagenes[ancho]) == '=':
                    estadoAncho = 6
                continue
            if estadoAncho == 6:
                if str(separarImagenes[ancho]) != ';':
                    estadoAncho = 6
                    cacheAncho = cacheAncho + str(separarImagenes[ancho])
                if str(separarImagenes[ancho]) == ';':
                    #print('este es el Ancho', cacheAncho)
                    listaFilas2D[1] = cacheAncho
                    cacheAncho = ''
                    estadoAncho = 0
                    #lista_informacion_filtrada.append(cacheAncho)
                    continue
        for alto in range(0, len(separarImagenes)):
            if estadoAlto == 0:
                if str(separarImagenes[alto]) == 'A':
                    estadoAlto = 1
                continue
            if estadoAlto == 1:
                if str(separarImagenes[alto]) == 'L':
                    estadoAlto = 2
                continue
            if estadoAlto == 2:
                if str(separarImagenes[alto]) == 'T':
                    estadoAlto = 3
                continue
            if estadoAlto == 3:
                if str(separarImagenes[alto]) == 'O':
                    estadoAlto = 4
                continue
            if estadoAlto == 4:
                if str(separarImagenes[alto]) == '=':
                    estadoAlto = 5
                continue
            if estadoAlto == 5:
                if str(separarImagenes[alto]) != ';':
                    global correcto
                    try:
                        validarNumero = int(separarImagenes[alto])
                        correcto = True
                    except:
                        correcto = False
                    if correcto == True:
                        cacheAlto = cacheAlto + str(separarImagenes[alto])
                if str(separarImagenes[alto]) == ';'and correcto == True:
                    #print('este es el cache Alto',cacheAlto)
                    listaFilas2D[2] = cacheAlto
                    #lista_informacion_filtrada.append(cacheAlto)
                    cacheAlto = ''
                    estadoAlto = 0
                continue
        for filas in range(0, len(separarImagenes)):
            if estadoFilas == 0:
                if str(separarImagenes[filas]) == 'F':
                    estadoFilas = 1
                continue
            if estadoFilas == 1:
                if str(separarImagenes[filas]) == 'I':
                    estadoFilas = 2
                continue
            if estadoFilas == 2:
                if str(separarImagenes[filas]) == 'L':
                    estadoFilas = 3
                continue
            if estadoFilas == 3:
                if str(separarImagenes[filas]) == 'A':
                    estadoFilas = 4
                continue
            if estadoFilas == 4:
                if str(separarImagenes[filas]) == 'S':
                    estadoFilas = 5
                continue
            if estadoFilas == 5:
                if str(separarImagenes[filas]) == '=':
                    estadoFilas = 6
                continue
            if estadoFilas == 6:
                if str(separarImagenes[filas]) != ';':
                    estadoFilas = 6
                    cacheFilas = cacheFilas + str(separarImagenes[filas])
                if str(separarImagenes[filas]) == ';':
                    #print('este es el numero de Filas', cacheFilas)
                    listaFilas2D[3] = cacheFilas
                    #lista_informacion_filtrada.append(cacheFilas)
                    cacheFilas = ''
                    estadoFilas = 0
        for columnas in range(0, len(separarImagenes)):

            if estadoColumna == 0:
                if str(separarImagenes[columnas]) == 'C':
                    estadoColumna = 1

                continue
            if estadoColumna == 1:
                if str(separarImagenes[columnas]) == 'O':
                    estadoColumna = 2
                continue
            if estadoColumna == 2:
                if str(separarImagenes[columnas]) == 'L':
                    estadoColumna = 3
                continue
            if estadoColumna == 3:
                if str(separarImagenes[columnas]) == 'U':
                    estadoColumna = 4
                continue
            if estadoColumna == 4:
                if str(separarImagenes[columnas]) == 'M':
                    estadoColumna = 5

                continue
            if estadoColumna == 5:
                if str(separarImagenes[columnas]) == 'N':
                    estadoColumna = 6

                continue
            if estadoColumna == 6:
                if str(separarImagenes[columnas]) == 'A':
                    estadoColumna = 7

                continue
            if estadoColumna == 7:
                if str(separarImagenes[columnas]) == 'S':
                    estadoColumna = 8

                continue
            if estadoColumna == 8:
                if str(separarImagenes[columnas]) == '=':
                    estadoColumna = 9

                continue
            if estadoColumna == 9:
                if str(separarImagenes[columnas]) != ';':
                    estadoColumna = 9
                    cacheColumna = cacheColumna + str(separarImagenes[columnas])
                if str(separarImagenes[columnas]) == ';':
                    #print('Este es el cache columnas', cacheColumna)
                    listaFilas2D[4] = cacheColumna
                    cacheColumna = ''
                    estadoColumna = 0
                    #lista_informacion_filtrada.append(cacheColumna
        for celda in range(0, len(separarImagenes)):

            if estadoCelda == 0:
                if str(separarImagenes[celda]) == 'C':
                    estadoCelda = 1
                continue
            if estadoCelda == 1:
                if str(separarImagenes[celda]) == 'E':
                    estadoCelda = 2
                continue
            if estadoCelda == 2:
                if str(separarImagenes[celda]) == 'L':
                    estadoCelda = 3
                continue
            if estadoCelda == 3:
                if str(separarImagenes[celda]) == 'D':
                    estadoCelda = 4
                continue
            if estadoCelda == 4:
                if str(separarImagenes[celda]) == 'A':
                    estadoCelda = 5
                continue
            if estadoCelda == 5:
                if str(separarImagenes[celda]) == 'S':
                    estadoCelda = 6
                continue
            if estadoCelda == 6:
                if str(separarImagenes[celda]) == ' ':
                    estadoCelda = 6
                if str(separarImagenes[celda]) == '=':
                    estadoCelda = 7
                continue
            if estadoCelda == 7:
                if str(separarImagenes[celda]) == ' ':
                    estadoCelda = 7
                if str(separarImagenes[celda]) == '{':
                    estadoCelda = 8
                continue
            if estadoCelda == 8:
                if str(separarImagenes[celda]) != '}':
                    #if str(separarImagenes[celda]) != '{':
                    estadoCelda = 8;
                    cacheCelda = cacheCelda + str(separarImagenes[celda])
                if str(separarImagenes[celda]) == '}':
                   estadoCelda = 9
                continue
            if estadoCelda == 9:
                if str(separarImagenes[celda]) == ';':
                    #print('este es el cahe Celda', cacheCelda)
                    listaFilas2D[5] = cacheCelda
                    cacheCelda = ''
                    estadoCelda = 0


        for filtro in range(0, len(separarImagenes)):
            if estadoFiltro == 0:
                if str(separarImagenes[filtro]) == 'F':
                   estadoFiltro = 1
                continue
            if estadoFiltro == 1:
                if str(separarImagenes[filtro]) == 'I':
                    estadoFiltro = 2
                continue
            if estadoFiltro == 2:
                if str(separarImagenes[filtro]) == 'L':
                    estadoFiltro = 3
                continue
            if estadoFiltro == 3:
                if str(separarImagenes[filtro]) == 'T':
                    estadoFiltro = 4
                continue
            if estadoFiltro == 4:
                if str(separarImagenes[filtro]) == 'R':
                    estadoFiltro = 5
                continue
            if estadoFiltro == 5:
                if str(separarImagenes[filtro]) == 'O':
                    estadoFiltro = 6
                continue
            if estadoFiltro == 6:
                if str(separarImagenes[filtro]) == 'S':
                    estadoFiltro = 7

                continue
            if estadoFiltro == 7:
                if str(separarImagenes[filtro]) == ' ':
                    estadoFiltro = 7
                if str(separarImagenes[filtro]) == '=':
                    estadoFiltro = 8
                continue
            if estadoFiltro == 8:
                if str(separarImagenes[filtro]) == ' ':
                    estadoFiltro = 8
                if str(separarImagenes[filtro]) != ';':
                    estadoFiltro = 8
                    cacheFiltro = cacheFiltro + str(separarImagenes[filtro])

                if str(separarImagenes[filtro]) == ';':
                    #print('estos son los filtros: ', cacheFiltro)
                    listaFilas2D[6] = cacheFiltro
                    cacheFiltro = ''
                    estadoFiltro = 0
                #lista_informacion_filtrada.append(cacheFiltro)
        #print(listaFilas2D)

        lista2D.append(listaFilas2D)
        listaFilas2D = ['','','','','','','']
    print('Primer Filtrado:', end='\n')
    for k in range(0,len(lista2D)):
        print(lista2D[k],end='\n')
    Filtro2(lista2D)
def Filtro2(lista_2D):
    tama??oXpixel = 0
    tama??oYpixel = 0
    print('este es filtro 2')
    #fila,columna,valicion,color
    listaCelda = ['','','','']
    listaCelda2D =[]

    state = 0
    cacheF=''
    cacheC=''
    cacheFpixel = ''
    cacheCpixel = ''
    cacheV =''
    cacheCol = ''
    tama??oI = ''
    for i in range(0,len(lista_2D)):
        nombre = str(lista_2D[i][0])
        Tx = int(lista_2D[i][1])
        Ty = int(lista_2D[i][2])
        NC = int(lista_2D[i][3])
        NF = int(lista_2D[i][4])
        filtrosSucios =str(lista_2D[i][6])
        tama??oXpixel = int(Tx/NC)
        tama??oYpixel = int(Ty/NF)
        tama??oI = str(Tx)+'x'+str(Ty)
        lista1 = []
        lista2 = []
        tama??oF = NF
        tama??oC = NC

        for artificial1 in range(0, tama??oF):
            for artificial2 in range(0, tama??oC):
                lista1.append('')
            lista2.append(lista1)
            lista1 = []
        print(lista2)

        celda = str(lista_2D[i][5])
        cadenaCelda = list(celda)
        for letra in range(0,len(cadenaCelda)):
            if state == 0:
                if str(cadenaCelda[letra])=='[':
                    state = 1
                continue
            if state == 1:
                if str(cadenaCelda[letra]) != ',':
                    state =1
                    cacheF = cacheF + str(cadenaCelda[letra])
                    cacheFpixel = cacheFpixel + str(cadenaCelda[letra])
                if str(cadenaCelda[letra]) == ',':
                    state = 2
                    listaCelda[0]=int(cacheFpixel)*tama??oXpixel

                continue
            if state == 2:
                if str(cadenaCelda[letra]) != ',':
                    cacheC = cacheC + str(cadenaCelda[letra])
                    cacheCpixel = cacheCpixel + str(cadenaCelda[letra])
                    state = 2
                if str(cadenaCelda[letra]) == ',':
                    state = 3
                    listaCelda[1] = int(cacheCpixel)*tama??oYpixel
                continue
            if state == 3:
                if str(cadenaCelda[letra]) != ',':
                    cacheV = cacheV + str(cadenaCelda[letra])
                    state = 3
                if str(cadenaCelda[letra]) == ',':
                    if cacheV == 'TRUE' or cacheV  =='FALSE':
                        listaCelda[2]=cacheV
                        state = 4
                continue
            if state == 4:
                if str(cadenaCelda[letra]) != ']':
                    cacheCol = cacheCol +str(cadenaCelda[letra])
                    state = 4
                if str(cadenaCelda[letra]) == ']':
                    listaCelda[3]=cacheCol
                    print(listaCelda)
                    #listaCelda2D.append(listaCelda)
                    color = ''

                    if listaCelda[2] == 'TRUE':
                         color = str(listaCelda[3])



                    lista2[int(cacheF)][int(cacheC)] = color



                    cacheF = ''
                    cacheFpixel = ''
                    cacheC = ''
                    cacheCpixel = ''
                    cacheV = ''
                    cacheCol = ''
                    listaCelda = ['','','','']
                    state = 0


        print('esta es la imagen', i)

        pixel = ''
        for xi in range(0,tama??oF):
            for yi in range(0,tama??oC):
                if str(lista2[xi][yi]) != '':
                    pixel = pixel + ' ' + str(xi * int(tama??oXpixel)) + 'px ' + str(
                        yi * int(tama??oYpixel)) + 'px ' + str(lista2[xi][yi]) + ','
                else:
                    pixel = pixel + ' ' + str(xi * int(tama??oXpixel)) + 'px ' + str(
                        yi * int(tama??oYpixel)) + 'px ' + '#FFFFFF' + ','

        quitarCaracterFinal = list(pixel)
        Tcadena = len(quitarCaracterFinal)
        quitarCaracterFinal[Tcadena - 1] = '}'
        pixelRefinado = ''
        for j in range(0, len(quitarCaracterFinal)):
            pixelRefinado = pixelRefinado + str(quitarCaracterFinal[j])

        print('Crear HTML')
        dir = 'HTML y CSS/' + nombre
        FSalidaH = open(dir + '.html', 'w')
        contenidoH = '''<!DOCTYPE html>
                        <html lang="es">
                        <head>
                          <meta charset="UTF-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1.0">
                          <meta http-equiv="X-UA-Compatible" content="ie=edge">
                          <title>''' + nombre + '''</title>
                          <link rel="stylesheet" href="''' + nombre + '''.css">
                        </head>
                        <body>
                        <div>''' + tama??oI + '''</div>
                          <div class="pixel-art"></div>

                        </body>
                        </html>'''
        FSalidaH.write(contenidoH)
        FSalidaH.close()

        FSalidaC = open(dir + '.css', 'w')
        contenidoC = '''body {
                          background-color: white;
                        }

                        .pixel-art {
                          ''' + 'width:' + str(tama??oXpixel) + 'px;' + 'height:' + str(
            tama??oYpixel) + 'px;' + 'margin: 0px;transform: scale(1);box-shadow:' + pixelRefinado
        FSalidaC.write(contenidoC)
        FSalidaC.close()

        htmli = dir + '.html'
        cssi = dir + '.css'
        print(htmli)
        print(cssi)
        hti = Html2Image()
        hti.output_path = 'Imagenes'
        hti.screenshot(
            html_file=htmli, css_file=cssi,
            size=(Tx + 14, Ty + 34),
            save_as=nombre+ '.jpg')
        print('creando Imagen' + nombre)
        htmli = dir + '.html'
        cssi = dir + '.css'
        print(htmli)
        print(cssi)
        hti = Html2Image()
        hti.output_path = 'ImagenesF'
        hti.screenshot(
            html_file=htmli, css_file=cssi,
            size=(Tx + 14, Ty + 34),
            save_as=nombre + 'Original' +'.jpg')
        print('creando Imagen' + nombre)

        # Filtros
        listaF = []
        cacheF = ''
        filtrosSucios  = filtrosSucios + '$'
        print(filtrosSucios)
        listaFiltro = list(filtrosSucios)
        for revisar in range(0,len(listaFiltro)):
            if str(listaFiltro[revisar]) != '$' and str(listaFiltro[revisar]) != ',' :
                cacheF = cacheF + str(listaFiltro[revisar])
            elif str(listaFiltro[revisar])==',' or str(listaFiltro[revisar])=='$':
                listaF.append(cacheF)
                cacheF = ''

        print('lista Filtros', listaF)

        for f in range(0,len(listaF)):
            if str(listaF[f]) == 'MIRRORX':
                print('MIRRORX')
                listaAux3 = []
                listaAux4 = []
                pixelMirrorX = ''
                #                for oi in range(tama??oF - 1, -1, -1):
                #    for pi in range(0, tama??oC):

                #
                for li in range(tama??oF - 1, -1, -1):
                    for mi in range(0, tama??oC):
                        listaAux3.append(str(lista2[li][mi]))
                    listaAux4.append(listaAux3)
                    listaAux3 = []

                for aux4 in range(0, tama??oF):
                    for aux5 in range(0, tama??oC):
                        # print(lista2[aux4][aux5]+'VS'+listaAux4[aux4][aux5])
                        if str(listaAux4[aux4][aux5]) != '':
                            pixelMirrorX = pixelMirrorX + str(aux4 * tama??oXpixel) + 'px ' + str(
                                aux5 * tama??oYpixel) + 'px ' + str(listaAux4[aux4][aux5]) + ','
                        if str(listaAux4[aux4][aux5]) == '':
                            pixelMirrorX = pixelMirrorX + str(aux4 * tama??oXpixel) + 'px ' + str(
                                aux5 * tama??oYpixel) + 'px ' + '#FFFFFF' + ','

                quitarCaracterFinalMirrorX = list(pixelMirrorX)
                TcadenaMirrorX = len(quitarCaracterFinalMirrorX)
                quitarCaracterFinalMirrorX[TcadenaMirrorX - 1] = '}'
                pixelRefinadoMirrorX = ''
                for jisx in range(0, len(quitarCaracterFinalMirrorX)):
                    pixelRefinadoMirrorX = pixelRefinadoMirrorX + str(quitarCaracterFinalMirrorX[jisx])
                # print('NO'+pixelRefinado)
                # print('Mx '+pixelRefinadoMirrorX)

                print('Crear HTML Mirror X')
                dirMX = 'Filtros/MirrorX' + nombre
                FSalidaHMX = open(dirMX + '.html', 'w')
                contenidoHMX = '''<!DOCTYPE html>
                                                               <html lang="es">
                                                               <head>
                                                                 <meta charset="UTF-8">
                                                                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                                 <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                                                 <title>''' + nombre + '''</title>
                                                                 <link rel="stylesheet" href="''' + 'MirrorX' + nombre + '''.css">
                                                               </head>
                                                               <body>
                                                               <div>''' + tama??oI + '''</div>
                                                                 <div class="pixel-art"></div>

                                                               </body>
                                                               </html>'''
                FSalidaHMX.write(contenidoHMX)
                FSalidaHMX.close()

                FSalidaCMX = open(dirMX + '.css', 'w')
                contenidoCMX = '''body {
                                                                 background-color: white;
                                                               }

                                                               .pixel-art {
                                                                 ''' + 'width:' + str(
                    tama??oXpixel) + 'px;' + 'height:' + str(
                    tama??oYpixel) + 'px;' + 'margin: 0px;transform: scale(1);box-shadow:' + pixelRefinadoMirrorX
                FSalidaCMX.write(contenidoCMX)
                FSalidaCMX.close()
                htmliMX = dirMX + '.html'
                cssiMX = dirMX + '.css'
                print(htmliMX)
                print(cssiMX)
                htiMX = Html2Image()
                htiMX.output_path = 'ImagenesF'
                htiMX.screenshot(
                    html_file=htmliMX, css_file=cssiMX,
                    size=(Tx + 14, Ty + 34),
                    save_as='MirrorX'+nombre + '.jpg')
                print('creando Imagen' +'MirrorX'+nombre)

            elif str(listaF[f]) == 'MIRRORY':
                print('MIRRORY')
                listaAux5 = []
                listaAux6 = []
                pixelMirrorY = ''
                #                for li in range(0, tama??oF):
                #    for mi in range(tama??oC - 1, -1, -1):
                for oi in range(0, tama??oF):
                    for pi in range(tama??oC - 1, -1, -1):
                        listaAux5.append(str(lista2[oi][pi]))
                    listaAux6.append(listaAux5)
                    listaAux5 = []

                for aux5 in range(0, tama??oF):
                    for aux6 in range(0, tama??oC):
                        if str(listaAux6[aux5][aux6]) != '':
                            pixelMirrorY = pixelMirrorY + str(aux5 * tama??oXpixel) + 'px ' + str(
                                aux6 * tama??oYpixel) + 'px ' + str(listaAux6[aux5][aux6]) + ','
                        elif str(listaAux6[aux5][aux6]) == '':
                            pixelMirrorY = pixelMirrorY + str(aux5 * tama??oXpixel) + 'px ' + str(
                                aux6 * tama??oYpixel) + 'px ' + '#FFFFFF' + ','

                quitarCaracterFinalMirrorY = list(pixelMirrorY)
                TcadenaMirrorY = len(quitarCaracterFinalMirrorY)
                quitarCaracterFinalMirrorY[TcadenaMirrorY - 1] = '}'
                pixelRefinadoMirrorY = ''
                for jisxz in range(0, len(quitarCaracterFinalMirrorY)):
                    pixelRefinadoMirrorY = pixelRefinadoMirrorY + str(quitarCaracterFinalMirrorY[jisxz])
                print(pixelRefinadoMirrorY)

                print('Crear HTML Mirror Y')
                dirMY = 'Filtros/MirrorY' + nombre
                FSalidaHMY = open(dirMY + '.html', 'w')
                contenidoHMY = '''<!DOCTYPE html>
                                                                       <html lang="es">
                                                                       <head>
                                                                         <meta charset="UTF-8">
                                                                         <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                                         <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                                                         <title>''' + nombre + '''</title>
                                                                         <link rel="stylesheet" href="''' + 'MirrorY' + nombre + '''.css">
                                                                       </head>
                                                                       <body>
                                                                       <div>''' + tama??oI + '''</div>
                                                                         <div class="pixel-art"></div>

                                                                       </body>
                                                                       </html>'''
                FSalidaHMY.write(contenidoHMY)
                FSalidaHMY.close()

                FSalidaCMY = open(dirMY + '.css', 'w')
                contenidoCMY = '''body {
                                                                         background-color: white;
                                                                       }

                                                                       .pixel-art {
                                                                         ''' + 'width:' + str(
                    tama??oXpixel) + 'px;' + 'height:' + str(
                    tama??oYpixel) + 'px;' + 'margin: 0px;transform: scale(1);box-shadow:' + pixelRefinadoMirrorY
                FSalidaCMY.write(contenidoCMY)
                FSalidaCMY.close()
                htmliMY = dirMY + '.html'
                cssiMY = dirMY + '.css'
                print(htmliMY)
                print(cssiMY)
                htiMY = Html2Image()
                htiMY.output_path = 'ImagenesF'
                htiMY.screenshot(
                    html_file=htmliMY, css_file=cssiMY,
                    size=(Tx + 14, Ty + 34),
                    save_as='MirrorY' + nombre + '.jpg')
                print('creando Imagen' + 'MirrorY' + nombre)
            elif str(listaF[f]) == 'DOUBLEMIRROR':
                print('DOUBLEMIRROR')
                listaAuxiliar1 = []
                listaAuxiliar2 = []
                pixelDobleMirror = ''
                for hi in range(tama??oF - 1, -1, -1):
                    for ki in range(tama??oC - 1, -1, -1):
                        listaAuxiliar1.append(lista2[hi][ki])
                    listaAuxiliar2.append(listaAuxiliar1)
                    listaAuxiliar1 = []

                for auxi in range(0, tama??oF):
                    for auxj in range(0, tama??oC):
                        if str(listaAuxiliar2[auxi][auxj]) != '':
                            pixelDobleMirror = pixelDobleMirror + str(auxi * tama??oXpixel) + 'px ' + str(
                                auxj * tama??oYpixel) + 'px ' + str(listaAuxiliar2[auxi][auxj]) + ','
                        elif str(listaAuxiliar2[auxi][auxj]) == '':
                            pixelDobleMirror = pixelDobleMirror + str(auxi * tama??oXpixel) + 'px ' + str(
                                auxj * tama??oYpixel) + 'px ' + '#FFFFFF' + ','
                quitarCaracterFinalDobleMirror = list(pixelDobleMirror)
                TcadenaDobleMirror = len(quitarCaracterFinalDobleMirror)
                quitarCaracterFinalDobleMirror[TcadenaDobleMirror - 1] = '}'
                pixelRefinadoDobleMirror = ''
                for jis in range(0, len(quitarCaracterFinalDobleMirror)):
                    pixelRefinadoDobleMirror = pixelRefinadoDobleMirror + str(quitarCaracterFinalDobleMirror[jis])
                print(pixelRefinadoDobleMirror)
                print('Crear HTML Doble Mirror')
                dirDM = 'Filtros/DobleMirror' + nombre
                FSalidaHDM = open(dirDM + '.html', 'w')
                contenidoHDM = '''<!DOCTYPE html>
                                                       <html lang="es">
                                                       <head>
                                                         <meta charset="UTF-8">
                                                         <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                         <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                                         <title>''' + nombre + '''</title>
                                                         <link rel="stylesheet" href="''' + 'DobleMirror' + nombre + '''.css">
                                                       </head>
                                                       <body>
                                                       <div>''' + tama??oI + '''</div>
                                                         <div class="pixel-art"></div>

                                                       </body>
                                                       </html>'''
                FSalidaHDM.write(contenidoHDM)
                FSalidaHDM.close()

                FSalidaCDM = open(dirDM + '.css', 'w')
                contenidoCDM = '''body {
                                                         background-color: white;
                                                       }

                                                       .pixel-art {
                                                         ''' + 'width:' + str(tama??oXpixel) + 'px;' + 'height:' + str(
                    tama??oYpixel) + 'px;' + 'margin: 0px;transform: scale(1);box-shadow:' + pixelRefinadoDobleMirror
                FSalidaCDM.write(contenidoCDM)
                FSalidaCDM.close()
                htmliDM = dirDM + '.html'
                cssiDM = dirDM + '.css'
                print(htmliDM)
                print(cssiDM)
                htiDM = Html2Image()
                htiDM.output_path = 'ImagenesF'
                htiDM.screenshot(
                    html_file=htmliDM, css_file=cssiDM,
                    size=(Tx + 14, Ty + 34),
                    save_as='DoubleMirror' + nombre + '.jpg')
                print('creando Imagen' + 'DoubleMirror' + nombre)













        lista2 = []
        lista1 = []
def Abrir():
    new = Toplevel(window)
    new.geometry("350x350")
    new.title("Imagenes")
    # Create a Label in New window
    global my_listbox
    Label(new, text="Lista de Imagenes disponibles", font=('Helvetica 17 bold')).pack(pady=30)
    my_listbox = Listbox(new)
    my_listbox.pack(pady=15)

    #agreagar lista de items

    carpeta = os.listdir('Imagenes')

    for item in carpeta:
        my_listbox.insert(END,item)
    my_button2 = Button(new,text='Select',command = select)
    my_button2.pack(pady=10)

    global my_label
    my_label = Label(new,text='')
    my_label.pack(pady=5)
def select():
    global nombreImagen
    my_label.config(text=my_listbox.get(ANCHOR))
    nombreImagen = my_listbox.get(ANCHOR)
    print('Usted selecciono',nombreImagen)
def Ver_Imagen():
    try:
        nombreI = ''
        nombreI = nombreImagen
        print('Abriendo imagen:', nombreI)

        global imagen
        imagen = Image.open('Imagenes/'+nombreI)
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window,image=photo).place(x=250,y=50,width=450,height=600)
    except:
        print('Error en funcion select no ha seleccionado ninguna imagen')
        tkinter.messagebox.showwarning('ERROR', 'En funcion select no ha seleccionado ninguna imagen')
def Ver_Reportes():
    webbrowser.open_new_tab('ReportesHTML\Reporte_Errores.html')
    webbrowser.open_new_tab('ReportesHTML\Reporte_Tokens.html')
def Filtro_Original():
    print('Original')
    try:
        nombreI = ''
        nombreI = nombreImagen
        print('Abriendo imagen:', nombreI)

        global imagen
        imagen = Image.open('ImagenesF/' + nombreI)
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window, image=photo).place(x=250, y=50, width=450, height=600)
    except:
        print('Error en funcion select no ha seleccionado ninguna imagen')
        tkinter.messagebox.showwarning('ERROR', 'En funcion select no ha seleccionado ninguna imagen o no se encontro ningun filtro ')
def Filtro_MirrorX():
    print('MirrorX')
    try:
        nombreI = ''
        nombreI = nombreImagen
        print('Abriendo imagen con Filtro MirrorX:', nombreI)

        global imagen
        imagen = Image.open('ImagenesF/MirrorX' + nombreI)
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window, image=photo).place(x=250, y=50, width=450, height=600)
    except:
        print('Error en funcion select no ha seleccionado ninguna imagen')
        tkinter.messagebox.showwarning('ERROR', 'En funcion select no ha seleccionado ninguna imagen o no se encontro ningun filtro ')
def Filtro_MirrorY():
    print('MirrorY')
    try:
        nombreI = ''
        nombreI = nombreImagen
        print('Abriendo imagen con Filtro:', nombreI)

        global imagen
        imagen = Image.open('ImagenesF/MirrorY' + nombreI)
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window, image=photo).place(x=250, y=50, width=450, height=600)
    except:
        print('Error en funcion select no ha seleccionado ninguna imagen')
        tkinter.messagebox.showwarning('ERROR', 'En funcion select no ha seleccionado ninguna imagen o no se encontro ningun filtro ')
def Filtro_DoubleMirror():
    print('Double Mirror')
    try:
        nombreI = ''
        nombreI = nombreImagen
        print('Abriendo imagen con Filtro:', nombreI)

        global imagen
        imagen = Image.open('ImagenesF/DoubleMirror' + nombreI)
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window, image=photo).place(x=250, y=50, width=450, height=600)
    except:
        print('Error en funcion select no ha seleccionado ninguna imagen')
        tkinter.messagebox.showwarning('ERROR', 'En funcion select no ha seleccionado ninguna imagen o no se encontro ningun filtro ')


if __name__ == '__main__':

    print('generano interfaz Bitxelart')
    global window
    window = tkinter.Tk()
    window.title("Bitxelart")
    window.geometry('800x600')
    menubar = tkinter.Menu(window)
    window.config(menu=menubar)
    # Creamos menu
    filemenu = tkinter.Menu(menubar)
    # Creamos File item
    filemenu.add_separator()
    menubar.add_cascade(label='Cargar Archivo', command=Cargar_Archivo)

    # Crear analizar itme
    analizarmenu = tkinter.Menu(menubar)
    analizarmenu.add_separator()
    menubar.add_cascade(label='Analizar', command=Analizar)

    # Crear Reportes
    reportesmenu = tkinter.Menu(menubar)
    # Creamos File item
    reportesmenu.add_separator()

    # Seleccionar Imagen
    seleccionar = tkinter.Menu(menubar)
    menubar.add_cascade(label='Seleccionar Imagen', command=Abrir)
    # Ver imagen

    menubar.add_cascade(label='Ver Imagen', command=Ver_Imagen)
    repo = tkinter.Menu(menubar)
    menubar.add_cascade(label='Reportes', command=Ver_Reportes)
    repo = tkinter.Menu(menubar)
    # Crear Salir items
    reportesmenu = tkinter.Menu(menubar)
    # Creamos Salir item
    reportesmenu.add_separator()
    menubar.add_cascade(label='Salir', command=window.quit)

    tkinter.Button(window, text="Original",command =Filtro_Original).place(x=25,y=100,width=100,height=30)
    tkinter.Button(window, text="Mirror X",command =Filtro_MirrorX).place(x=25,y=180,width=100,height=30)
    tkinter.Button(window, text="Mirror Y",command =Filtro_MirrorY).place(x=25,y=260,width=100,height=30)
    tkinter.Button(window, text="Doble Mirror",command =Filtro_DoubleMirror).place(x=25,y=340,width=100,height=30)


    window.mainloop()
