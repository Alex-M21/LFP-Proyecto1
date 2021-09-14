import tkinter
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from PIL import Image, ImageTk
import imgkit

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
    cache = ''
    print('Abriendo Archivo para lectura')
    try:
        file_entrada = open(Dir,'r')
        primera_lectura = file_entrada.read()
        ##print(primera_lectura)
    except:
        print('Error al intentar abrir el archivo')
        messagebox.showwarning(message="ERROR al intentar abrir archivo de entrada ", title="ERROR")
    else:
        print('Se logro abrir archivo de entrada con exito')
        messagebox.showinfo(message="Se logro abrir el archivo de entrada", title="CONFIRMACION")
        primeros_caracteres = list(primera_lectura)


        for i in range(0,len(primeros_caracteres)):
            if str(primeros_caracteres[i]) != '\n' and str(primeros_caracteres[i]) != '\t':
                cache = cache + str(primeros_caracteres[i])
            if str(primeros_caracteres[i]) == '\n' or str(primeros_caracteres[i]==''):
                primeras_lineas.append(cache)
                cache = ''

        return primeras_lineas
def Analizar():
    #try:
    dir = ruta
    print('Se analizara el archivo')
    print(dir)
    primeras_lineas = Abrir_Archivo(dir)
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
    print('Conjunto de Caracteres:',end='\n')
    print(LineaUnica)

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
    tamañoXpixel = 0
    tamañoYpixel = 0
    print('este es filtro 2')
    #fila,columna,valicion,color
    listaCelda = ['','','','']
    listaCelda2D =[]
    state = 0
    cacheF=''
    cacheC=''
    cacheV =''
    cacheCol = ''
    for i in range(0,len(lista_2D)):
        nombre = str(lista_2D[i][0])
        Tx = int(lista_2D[i][1])
        Ty = int(lista_2D[i][2])
        NC = int(lista_2D[i][3])
        NF = int(lista_2D[i][4])
        tamañoXpixel = int(Tx/NC)
        tamañoYpixel = int(Ty/NF)

        print(tamañoXpixel,',',tamañoYpixel)


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
                if str(cadenaCelda[letra]) == ',':
                    state = 2
                    listaCelda[0]=int(cacheF)*tamañoXpixel
                continue
            if state == 2:
                if str(cadenaCelda[letra]) != ',':
                    cacheC = cacheC + str(cadenaCelda[letra])
                    state = 2
                if str(cadenaCelda[letra]) == ',':
                    state = 3
                    listaCelda[1] = int(cacheC)*tamañoYpixel
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
                    listaCelda2D.append(listaCelda)
                    cacheF = ''
                    cacheC = ''
                    cacheV = ''
                    cacheCol = ''
                    listaCelda = ['','','','']
                    state = 0
        #print(listaCelda2D)
        print('esta es la imagen', i)
        pixel = ''
        for l in range(0,len(listaCelda2D)):
            if str(listaCelda2D[l][2]) == 'TRUE':
                #if l <= len(listaCelda2D)-2:
                pixel = pixel + ' ' + str(listaCelda2D[l][0])+'px '+str(listaCelda2D[l][1])+'px '+str(listaCelda2D[l][3])+','

        quitarCaracterFinal = list(pixel)
        Tcadena = len(quitarCaracterFinal)
        quitarCaracterFinal[Tcadena-1] = '}'
        pixelRefinado = ''
        for j in range(0,len(quitarCaracterFinal)):
            pixelRefinado = pixelRefinado +  str(quitarCaracterFinal[j])

        print('Crear HTML')
        FSalidaH = open('HTML y CSS/'+nombre+'.html','w')
        contenidoH = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>'''+nombre+'''</title>
  <link rel="stylesheet" href="'''+nombre+'''.css">
</head>
<body>
  <div class="pixel-art"></div>
</body>
</html>'''
        FSalidaH.write(contenidoH)
        FSalidaH.close()

        FSalidaC = open('HTML y CSS/'+nombre+'.css','w')
        contenidoC = '''body {
  background-color: white;
}

.pixel-art {
  '''+'width:'+str(tamañoXpixel)+'px;'+ 'height:' +str(tamañoYpixel)+'px;'+'margin: 50px;transform: scale(1);box-shadow:'+pixelRefinado
        FSalidaC.write(contenidoC)
        FSalidaC.close()

        imgkit.from_file('HTML y CSS/Pokebola.html','out.jpg')

        listaCelda2D = []













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
    ver = tkinter.Menu(menubar)
    menubar.add_cascade(label='Ver Imagen', command=Ver_Imagen)

    # Crear Salir items
    reportesmenu = tkinter.Menu(menubar)
    # Creamos Salir item
    reportesmenu.add_separator()
    menubar.add_cascade(label='Salir', command=window.quit)

    tkinter.Button(window, text="Original").place(x=25,y=100,width=100,height=30)
    tkinter.Button(window, text="Mirror X").place(x=25,y=180,width=100,height=30)
    tkinter.Button(window, text="Mirror Y").place(x=25,y=260,width=100,height=30)
    tkinter.Button(window, text="Doble Mirror").place(x=25,y=340,width=100,height=30)


    window.mainloop()
