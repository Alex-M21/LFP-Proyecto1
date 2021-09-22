from CrearHTMLReportes import *
def validarNumero(caracter):
    correcto = False
    try:
        vNumero = int(caracter)
        correcto  = True
    except:
        correcto  = False
    return correcto

def AFD_ERRORES(lista_lineas):
    print('Iniciando Automata ERRORES')

    lista_lineas = lista_lineas

    tokensPrincipal = ''
    tokens = ['','','']
    listadetokens = []

    errores = []

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
    estadoImagen = 0
    # inicializamos cache
    cacheNombre = ''
    cacheAncho = ''
    cacheAlto = ''
    cacheFilas = ''
    cacheColumna = ''
    cacheCelda = ''
    cacheFiltro = ''
    cacheImagen = ''
    print(lista_lineas)
    for lineas in range(0,len(lista_lineas)):

        separarLineas = list(lista_lineas[lineas])
        for separacion in range(0, len(separarLineas)):
            if estadoNombre == 0:
                if str(separarLineas[separacion]) == 'T':
                    estadoNombre = 1

                else:
                    estadoNombre = 0

                continue
            if estadoNombre == 1:
                if str(separarLineas[separacion]) == 'I':
                    estadoNombre = 2

                else:
                    estadoNombre = 0

                continue
            if estadoNombre == 2:
                if str(separarLineas[separacion]) == 'T':
                    estadoNombre = 3

                else:
                    estadoNombre = 0

                continue
            if estadoNombre == 3:
                if str(separarLineas[separacion]) == 'U':
                    estadoNombre = 4

                else:
                    estadoNombre = 0

                continue
            if estadoNombre == 4:
                if str( separarLineas[separacion]) == 'L':
                    estadoNombre = 5

                else:
                    estadoNombre = 0

                continue
            if estadoNombre == 5:
                if str(separarLineas[separacion]) == 'O':
                    estadoNombre = 6

                    tokens[0] = 'TITULO'
                    tokens[1] = 'titulo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens=['','','']
                else:
                    estadoNombre = 0
                    errores.append('Error token TITULO no encontrado en columna '+str(separacion)+ 'y  la linea' + str(lineas))
                continue
            if estadoNombre == 6:
                if str(separarLineas[separacion]) == '=':
                    estadoNombre = 7
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:

                    errores.append('Error encontrado ' + str(separarLineas[separacion]) + ' en la columna' + str(
                        separacion) + ' en la linea' + str(lineas))
                continue
            if estadoNombre == 7:
                if str( separarLineas[separacion]) == '"':
                    estadoNombre = 8

                    tokens[0] = '"'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    estadoNombre = 0
                    errores.append('Error encontrado' + str(separarLineas[separacion]) + 'en la columna' + str(
                        separacion) + ' en la linea' + str(lineas))

                continue
            if estadoNombre == 8:
                if str( separarLineas[separacion]) != '"':
                    cacheNombre = cacheNombre + str( separarLineas[separacion])
                    estadoNombre = 8

                if str( separarLineas[separacion]) == '"':
                    estadoNombre = 9

                    tokens[0] = cacheNombre
                    tokens[1] = 'cadena'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']


                    tokens[0] = '"'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']

                    tokensPrincipal = ''

                continue
            if estadoNombre == 9:
                if str( separarLineas[separacion]) == ';':
                    cacheNombre = ''
                    tokens[0] = ';'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoNombre = 0
                else:
                    errores.append('Error encontrado ' + str(separarLineas[separacion]) + ' en la columna ' + str(
                        separacion) + ' en la linea ' + str(lineas))
                continue
        for ancho in range(0, len(separarLineas)):
            if estadoAncho == 0:
                if str(separarLineas[ancho]) == 'A':
                    estadoAncho = 1

                else:
                    estadoAncho = 0
                continue
            if estadoAncho == 1:
                if str(separarLineas[ancho]) == 'N':
                    estadoAncho = 2

                else:
                    estadoAncho = 0

                continue
            if estadoAncho == 2:
                if str(separarLineas[ancho]) == 'C':
                    estadoAncho = 3

                else:
                    estadoAncho = 0
                continue
            if estadoAncho == 3:
                if str(separarLineas[ancho]) == 'H':
                    estadoAncho = 4

                else:
                    estadoAncho = 0
                continue
            if estadoAncho == 4:
                if str(separarLineas[ancho]) == 'O':
                    estadoAncho = 5

                else:
                    estadoAncho = 0
                    errores.append('Error token ANCHO no encontrado en columna '+str(ancho)+ '  y  la linea  ' + str(lineas))

                continue
            if estadoAncho == 5:
                if str(separarLineas[ancho]) == '=':
                    estadoAncho = 6
                    tokens[0] = str(tokensPrincipal)
                    tokens[1] = 'ancho'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokensPrincipal = ''
                    tokens = ['', '', '']
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokensPrincipal = ''
                else:
                    errores.append('Error encontrado  ' + str(separarLineas[ancho]) +'  en la columna  '+str(ancho)+ ' en la linea  ' + str(lineas))
                continue
            if estadoAncho == 6:
                if str(separarLineas[ancho]) != ';':
                    estadoAncho = 6
                    cacheAncho = cacheAncho + str(separarLineas[ancho])
                if str(separarLineas[ancho]) == ';':
                    tokens[0] = cacheAncho
                    tokens[1] = 'cadena'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']

                    tokens[0] = ';'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoAncho = 0

                    cacheAncho = ''

        for alto in range(0, len(separarLineas)):
            if estadoAlto == 0:
                if str(separarLineas[alto]) == 'A':
                    estadoAlto = 1

                else:
                    estadoAlto = 0
                    tokensPrincipal = ''
                continue
            if estadoAlto == 1:
                if str(separarLineas[alto]) == 'L':
                    estadoAlto = 2

                else:
                    estadoAlto = 0
                    tokensPrincipal = ''
                continue

            if estadoAlto == 2:
                if str(separarLineas[alto]) == 'T':
                    estadoAlto = 3

                else:
                    estadoAlto = 0
                    tokensPrincipal = ''
                continue
            if estadoAlto == 3:
                if str(separarLineas[alto]) == 'O':
                    estadoAlto = 4

                else:
                    estadoAlto = 0
                    errores.append('Error token ALTO no encontrado en columna ' + str(alto) + 'y  la linea' + str(lineas))
                    tokensPrincipal = ''
                continue
            if estadoAlto == 4:
                if str(separarLineas[alto]) == '=':
                    estadoAlto = 5
                    tokens[0] = 'ALTO'
                    tokens[1] = 'alto'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokensPrincipal = ''
                    tokens = ['', '', '']
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append('Error encontrado' + str(separarLineas[alto]) +'en la columna'+str(alto)+ ' en la linea' + str(lineas))
                    estadoAlto = 0

                continue
            if estadoAlto == 5:
                if str(separarLineas[alto]) != ';':

                    cacheAlto = cacheAlto + str(separarLineas[alto])

                if str(separarLineas[alto]) == ';':
                    correcto = validarNumero(cacheAlto)
                    if correcto == True:
                        tokens[0] = cacheAlto
                        tokens[1] = 'cadena'
                        tokens[2] = lineas
                        listadetokens.append(tokens)
                        tokens = ['', '', '']
                        tokens[0] = ';'
                        tokens[1] = 'signo'
                        tokens[2] = lineas
                        listadetokens.append(tokens)
                        tokens = ['', '', '']
                        cacheAlto = ''
                        tokensPrincipal = ''
                        estadoAlto = 0
                continue
        for filas in range(0, len(separarLineas)):
            if estadoFilas == 0:
                if str(separarLineas[filas]) == 'F':
                    estadoFilas = 1
                continue
            if estadoFilas == 1:
                if str(separarLineas[filas]) == 'I':
                    estadoFilas = 2
                continue
            if estadoFilas == 2:
                if str(separarLineas[filas]) == 'L':
                    estadoFilas = 3
                continue
            if estadoFilas == 3:
                if str(separarLineas[filas]) == 'A':
                    estadoFilas = 4
                continue
            if estadoFilas == 4:
                if str(separarLineas[filas]) == 'S':
                    estadoFilas = 5
                    tokens[0] = 'FILAS'
                    tokens[1] = 'filas'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append(
                        'Error token FILAS no encontrado en columna ' + str(filas) + 'y  la linea' + str(lineas))
                continue
            if estadoFilas == 5:
                if str(separarLineas[filas]) == '=':
                    estadoFilas = 6
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append('Error encontrado' + str(separarLineas[filas]) + 'en la columna' + str(
                        filas) + ' en la linea' + str(lineas))
                continue
            if estadoFilas == 6:
                if str(separarLineas[filas]) != ';':
                    estadoFilas = 6
                    cacheFilas = cacheFilas + str(separarLineas[filas])
                if str(separarLineas[filas]) == ';':
                    tokens[0] = cacheFilas
                    tokens[1] = 'cadena'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokens[0] = ';'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    cacheFilas = ''
                    estadoFilas = 0
        for columnas in range(0, len(separarLineas)):

            if estadoColumna == 0:
                if str(separarLineas[columnas]) == 'C':
                    estadoColumna = 1
                else:
                    estadoColumna = 0

                continue
            if estadoColumna == 1:
                if str(separarLineas[columnas]) == 'O':
                    estadoColumna = 2
                else:
                    estadoColumna = 0
                continue
            if estadoColumna == 2:
                if str(separarLineas[columnas]) == 'L':
                    estadoColumna = 3
                else:
                    estadoColumna = 0
                continue
            if estadoColumna == 3:
                if str(separarLineas[columnas]) == 'U':
                    estadoColumna = 4
                else:
                    estadoColumna = 0
                continue
            if estadoColumna == 4:
                if str(separarLineas[columnas]) == 'M':
                    estadoColumna = 5
                else:
                    estadoColumna = 0

                continue
            if estadoColumna == 5:
                if str(separarLineas[columnas]) == 'N':
                    estadoColumna = 6
                else:
                    estadoColumna = 0

                continue
            if estadoColumna == 6:
                if str(separarLineas[columnas]) == 'A':
                    estadoColumna = 7
                else:
                    estadoColumna = 0

                continue
            if estadoColumna == 7:
                if str(separarLineas[columnas]) == 'S':
                    estadoColumna = 8
                else:
                    estadoColumna = 0
                    errores.append('Error token COLUMNAS no encontrado en columna ' + str(columnas) + 'y  la linea' + str(lineas))

                continue
            if estadoColumna == 8:
                if str(separarLineas[columnas]) == '=':
                    tokens[0] = 'COLUMNAS'
                    tokens[1] = 'columna'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoColumna = 9
                else:
                    errores.append('Error encontrado' + str(separarLineas[columnas]) + 'en la columna' + str(
                    columnas) + ' en la linea' + str(lineas))

                continue
            if estadoColumna == 9:
                if str(separarLineas[columnas]) != ';':
                    estadoColumna = 9
                    cacheColumna = cacheColumna + str(separarLineas[columnas])
                if str(separarLineas[columnas]) == ';':
                    tokens[0] = cacheColumna
                    tokens[1] = 'cadena'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokens[0] = ';'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']

                    cacheColumna = ''
                    estadoColumna = 0
        for celda in range(0, len(separarLineas)):

            if estadoCelda == 0:
                if str(separarLineas[celda]) == 'C':
                    estadoCelda = 1
                else:
                    estadoCelda = 0
                continue
            if estadoCelda == 1:
                if str(separarLineas[celda]) == 'E':
                    estadoCelda = 2
                else:
                    estadoCelda = 0
                continue
            if estadoCelda == 2:
                if str(separarLineas[celda]) == 'L':
                    estadoCelda = 3
                else:
                    estadoCelda = 0
                continue
            if estadoCelda == 3:
                if str(separarLineas[celda]) == 'D':
                    estadoCelda = 4
                else:
                    estadoCelda = 0
                continue
            if estadoCelda == 4:
                if str(separarLineas[celda]) == 'A':
                    estadoCelda = 5
                else:
                    estadoCelda = 0
                continue
            if estadoCelda == 5:
                if str(separarLineas[celda]) == 'S':
                    estadoCelda = 6
                else:
                    errores.append('Error token CELDAS no encontrado en columna ' + str(columnas) + 'y  la linea' + str(lineas))
                    estadoCelda = 0
                continue
            if estadoCelda == 6:

                if str(separarLineas[celda]) == '=':
                    estadoCelda = 7
                    tokens[0] = 'CELDAS'
                    tokens[1] = 'celdas'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append('Error encontrado' + str(separarLineas[celda]) + 'en la columna' + str(
                        celda) + ' en la linea' + str(lineas))
                continue
            if estadoCelda == 7:
                if str(separarLineas[celda]) == '{':
                    tokens[0] = '{'
                    tokens[1] = 'agrupacion'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoCelda = 0
                else:
                    errores.append('Error encontrado' + str(separarLineas[celda]) + 'en la columna' + str(
                        celda) + ' en la linea' + str(lineas))
                continue


        for matriz in range(0, len(separarLineas)):
            if estadoImagen == 0:
                if separarLineas[matriz] == '[':
                    estadoImagen = 1
                    tokens[0] = '['
                    tokens[1] = 'agrupacion'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                #else:

                #    errores.append('Error encontrado' + str(separarLineas[matriz]) + 'en la columna' + str(
                #        matriz) + ' en la linea' + str(lineas))
                continue
            if estadoImagen == 1:
                if separarLineas[matriz] != ',':
                    cacheImagen = cacheImagen + str(separarLineas[matriz])
                    estadoImagen = 1
                if separarLineas[matriz] == ',':
                    tokens[0] = cacheImagen
                    tokens[1] = 'posicion x'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    cacheImagen = ''
                    tokens = ['', '', '']
                    tokens[0] = ','
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoImagen = 2

                continue
            if estadoImagen == 2:
                if separarLineas[matriz] != ',':
                    cacheImagen = cacheImagen + str(separarLineas[matriz])
                    estadoImagen = 2
                if separarLineas[matriz] == ',':
                    tokens[0] = cacheImagen
                    tokens[1] = 'posicion y'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    cacheImagen = ''
                    tokens = ['', '', '']
                    tokens[0] = ','
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoImagen = 3

                continue
            if estadoImagen == 3:
                if separarLineas[matriz] != ',':
                    cacheImagen = cacheImagen + str(separarLineas[matriz])
                    estadoImagen = 3
                if separarLineas[matriz] == ',':
                    tokens[0] = cacheImagen
                    tokens[1] = 'logico'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    cacheImagen = ''
                    tokens = ['', '', '']
                    tokens[0] = ','
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoImagen = 4
                continue
            if estadoImagen == 4:
                if separarLineas[matriz] != ']':
                    cacheImagen = cacheImagen + str(separarLineas[matriz])
                    estadoImagen = 4
                if separarLineas[matriz] == ']':
                    tokens[0] = cacheImagen
                    tokens[1] = 'color'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    cacheImagen = ''
                    tokens = ['', '', '']
                    tokens[0] = ']'
                    tokens[1] = 'agrupacion'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoImagen = 5
                continue
            if estadoImagen == 5:
                if separarLineas[matriz] != ',':
                    tokens[0] = ','
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoImagen = 0


        for filtro in range(0, len(separarLineas)):
            if estadoFiltro == 0:
                if str(separarLineas[filtro]) == 'F':
                    estadoFiltro = 1
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 1:
                if str(separarLineas[filtro]) == 'I':
                    estadoFiltro = 2
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 2:
                if str(separarLineas[filtro]) == 'L':
                    estadoFiltro = 3
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 3:
                if str(separarLineas[filtro]) == 'T':
                    estadoFiltro = 4
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 4:
                if str(separarLineas[filtro]) == 'R':
                    estadoFiltro = 5
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 5:
                if str(separarLineas[filtro]) == 'O':
                    estadoFiltro = 6
                else:
                    estadoFiltro = 0
                continue
            if estadoFiltro == 6:
                if str(separarLineas[filtro]) == 'S':
                    estadoFiltro = 7
                else:
                    errores.append(
                        'Error token FILTROS no encontrado en columna ' + str(filtro) + 'y  la linea' + str(lineas))
                    estadoFiltro = 0
                continue
            if estadoFiltro == 7:

                if str(separarLineas[filtro]) == '=':
                    estadoFiltro = 8
                    tokens[0] = 'FILTROS'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    tokens[0] = '='
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append('Error encontrado' + str(separarLineas[filtro]) + 'en la columna' + str(
                        filtro) + ' en la linea' + str(lineas))
                continue
            if estadoFiltro == 8:

                if str(separarLineas[filtro]) != ','or str(separarLineas[filtro]) != ';':
                    cacheFiltro = cacheFiltro + str(separarLineas[filtro])
                    estadoFiltro = 8
                if str(separarLineas[filtro]) == ',' or str(separarLineas[filtro]) == ';':
                    tokens[0] = cacheFiltro
                    tokens[1] = 'cadena'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    if str(separarLineas[filtro]) == ',':
                        tokens[0] = ','
                    else:
                        tokens[0] = ';'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    cacheFiltro = ''
                    estadoFiltro = 0
        for separador in range(0, len(separarLineas)):
            if estadoSeparador == 0:
                if str(separarLineas[separador]) == '@':
                    tokens[0] = '@'
                    tokens[1] = 'separador'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                    estadoSeparador =1

                continue
            if estadoSeparador == 1:
                if str(separarLineas[separador]) == '@':
                    estadoSeparador =2
                    tokens[0] = '@'
                    tokens[1] = 'separador'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                continue
            if estadoSeparador == 2:
                if str(separarLineas[separador]) == '@':
                    estadoSeparador =3
                    tokens[0] = '@'
                    tokens[1] = 'separador'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                continue
            if estadoSeparador == 3:
                if str(separarLineas[separador]) == '@':
                    estadoSeparador =0
                    tokens[0] = '@'
                    tokens[1] = 'separador'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append(
                        'Error token @@@@ no encontrado en columna ' + str(columnas) + 'y  la linea' + str(lineas))









    Reporte_Tokens(listadetokens)
    Reporte_Errores(errores)






