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
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                else:
                    estadoNombre = 0
                continue
            if estadoNombre == 1:
                if str(separarLineas[separacion]) == 'I':
                    estadoNombre = 2
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                else:
                    estadoNombre = 0
                continue
            if estadoNombre == 2:
                if str(separarLineas[separacion]) == 'T':
                    estadoNombre = 3
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                else:
                    estadoNombre = 0
                continue
            if estadoNombre == 3:
                if str(separarLineas[separacion]) == 'U':
                    estadoNombre = 4
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                else:
                    estadoNombre = 0
                continue
            if estadoNombre == 4:
                if str( separarLineas[separacion]) == 'L':
                    estadoNombre = 5
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                else:
                    estadoNombre = 0
                continue
            if estadoNombre == 5:
                if str(separarLineas[separacion]) == 'O':
                    estadoNombre = 6
                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                    tokens[0] = str(tokensPrincipal)
                    tokens[1] = 'titulo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens=['','','']
                else:
                    estadoNombre = 0
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
                    estadoNombre = 0
                    errores.append('Error encontrado '+str(separarLineas[separacion])+' en la linea'+str(lineas))
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
                    errores.append('Error encontrado ' + str(separarLineas[separacion]) + ' en la linea' + str(lineas))

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

                    tokensPrincipal = tokensPrincipal + str(separarLineas[separacion])
                    tokens[0] = '"'
                    tokens[1] = 'signo'
                    tokens[2] = lineas
                    listadetokens.append(tokens)
                    tokens = ['', '', '']
                else:
                    errores.append('Error encontrado ' + str(separarLineas[separacion]) + ' en la linea' + str(lineas))
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
                continue

    print(listadetokens)
    print(errores)





