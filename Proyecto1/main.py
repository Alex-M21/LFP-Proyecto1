import tkinter
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from PIL import Image, ImageTk


#Variables Globales
ruta = ''




def saludo():
    print('hola mundo')
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
        print(primera_lectura)
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
            elif str(primeros_caracteres[i]) == '\n':
                primeras_lineas.append(cache)
                cache = ''

        return primeras_lineas

def AFD(lista_lineas):
    print('Iniciando Automata')
    lista_lineas = lista_lineas
    lista_informacion_filtrada = []
    lista2D = []
    for i in range(0,len(lista_lineas)):
        separacion_Inicial = list(lista_lineas[i])
        print(separacion_Inicial)
        #Estados
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

        # Buscamos titulo
        for j in range(0, len(separacion_Inicial)):

            if estadoNombre == 0:
                if str(separacion_Inicial[j]) == 'T':
                    estadoNombre = 1
                continue
            if estadoNombre == 1:
                if str(separacion_Inicial[j]) == 'I':
                    estadoNombre = 2
                continue
            if estadoNombre == 2:
                if str(separacion_Inicial[j]) == 'T':
                    estadoNombre = 3
                continue
            if estadoNombre == 3:
                if str(separacion_Inicial[j]) == 'U':
                    estadoNombre = 4
                continue
            if estadoNombre == 4:
                if str(separacion_Inicial[j]) == 'L':
                    estadoNombre = 5
                continue
            if estadoNombre == 5:
                if str(separacion_Inicial[j]) == 'O':
                    estadoNombre = 6
                continue
            if estadoNombre == 6:
                if str(separacion_Inicial[j]) == '=':
                    estadoNombre = 7
                continue
            if estadoNombre == 7:
                if str(separacion_Inicial[j]) == '"':
                    estadoNombre = 8
                continue
            if estadoNombre == 8:
                if str(separacion_Inicial[j]) != '"':
                    cacheNombre = cacheNombre + str(separacion_Inicial[j])
                    estadoNombre = 8
                if str(separacion_Inicial[j]) == '"':
                    estadoNombre = 9
                continue
            if estadoNombre == 9:
                if str(separacion_Inicial[j]) == ';':
                    print('este es el cache Nombre', cacheNombre)
                    lista_informacion_filtrada.append(cacheNombre)
        # Buscamos Ancho
        for ancho in range(0,len(separacion_Inicial)):

            if estadoAncho == 0:
                if str(separacion_Inicial[ancho]) == 'A':
                    estadoAncho = 1
                continue
            if estadoAncho == 1:
                if str(separacion_Inicial[ancho]) == 'N':
                    estadoAncho = 2
                continue
            if estadoAncho == 2:
                if str(separacion_Inicial[ancho]) == 'C':
                    estadoAncho = 3
                continue
            if estadoAncho == 3:
                if str(separacion_Inicial[ancho]) == 'H':
                    estadoAncho = 4
                continue
            if estadoAncho == 4:
                if str(separacion_Inicial[ancho]) == 'O':
                    estadoAncho = 5
                continue
            if estadoAncho == 5:
                if str(separacion_Inicial[ancho]) == '=':
                    estadoAncho = 6
                continue
            if estadoAncho == 6:
                if str(separacion_Inicial[ancho]) != ';':
                    estadoAncho = 6
                    cacheAncho = cacheAncho + str(separacion_Inicial[ancho])
                if str(separacion_Inicial[ancho]) == ';':
                    print('este es el ancho', cacheAncho)
                    lista_informacion_filtrada.append(cacheAncho)
        # Buscamos el alto
        for alto in range(0,len(separacion_Inicial)):

            if estadoAlto == 0:
                if str(separacion_Inicial[alto]) == 'A':
                    estadoAlto = 1
                continue
            if estadoAlto == 1:
                if str(separacion_Inicial[alto]) == 'L':
                    estadoAlto = 2
                continue
            if estadoAlto == 2:
                if str(separacion_Inicial[alto]) == 'T':
                    estadoAlto = 3
                continue
            if estadoAlto == 3:
                if str(separacion_Inicial[alto]) == 'O':
                    estadoAlto = 4
                continue
            if estadoAlto == 4:
                if str(separacion_Inicial[alto]) == '=':
                    estadoAlto = 5
                continue
            if estadoAlto == 5:
                if str(separacion_Inicial[alto]) != ';':
                    estadoAlto = 5
                    cacheAlto = cacheAlto + str(separacion_Inicial[alto])
                if str(separacion_Inicial[alto]) == ';':
                    print('este es el cache Alto', cacheAlto)
                    lista_informacion_filtrada.append(cacheAlto)
        # Buscamos el filas
        for filas in range(0,len(separacion_Inicial)):
            if estadoFilas == 0:
                if str(separacion_Inicial[filas]) == 'F':
                    estadoFilas = 1
                continue
            if estadoFilas == 1:
                if str(separacion_Inicial[filas]) == 'I':
                    estadoFilas = 2
                continue
            if estadoFilas == 2:
                if str(separacion_Inicial[filas]) == 'L':
                    estadoFilas = 3
                continue
            if estadoFilas == 3:
                if str(separacion_Inicial[filas]) == 'A':
                    estadoFilas = 4
                continue
            if estadoFilas == 4:
                if str(separacion_Inicial[filas]) == 'S':
                    estadoFilas = 5
                continue
            if estadoFilas == 5:
                if str(separacion_Inicial[filas]) == '=':
                    estadoFilas = 6
                continue
            if estadoFilas == 6:
                if str(separacion_Inicial[filas]) != ';':
                    estadoFilas = 6
                    cacheFilas = cacheFilas + str(separacion_Inicial[filas])
                if str(separacion_Inicial[filas]) == ';':
                    print('este es el numero de filas',cacheFilas )
                    lista_informacion_filtrada.append(cacheFilas)
                continue
        # Buscamos columnas
        for columnas in range(0,len(separacion_Inicial)):

            if estadoColumna == 0:
                if str(separacion_Inicial[columnas]) == 'C':
                    estadoColumna = 1

                continue
            if estadoColumna == 1:
                if str(separacion_Inicial[columnas]) == 'O':
                    estadoColumna = 2
                continue
            if estadoColumna == 2:
                if str(separacion_Inicial[columnas]) == 'L':
                    estadoColumna = 3
                continue
            if estadoColumna == 3:
                if str(separacion_Inicial[columnas]) == 'U':
                    estadoColumna = 4
                continue
            if estadoColumna == 4:
                if str(separacion_Inicial[columnas]) == 'M':
                    estadoColumna = 5

                continue
            if estadoColumna == 5:
                if str(separacion_Inicial[columnas]) == 'N':
                    estadoColumna = 6

                continue
            if estadoColumna == 6:
                if str(separacion_Inicial[columnas]) == 'A':
                    estadoColumna = 7

                continue
            if estadoColumna == 7:
                if str(separacion_Inicial[columnas]) == 'S':
                    estadoColumna = 8

                continue
            if estadoColumna == 8:
                if str(separacion_Inicial[columnas]) == '=':
                    estadoColumna = 9

                continue
            if estadoColumna == 9:
                if str(separacion_Inicial[columnas]) != ';':
                    estadoColumna = 9
                    cacheColumna = cacheColumna + str(separacion_Inicial[columnas])
                    print('Este es el cache columnas',cacheColumna)
                    lista_informacion_filtrada.append(cacheColumna)
        # Buscamos celdas
        for celda in range(0,len(separacion_Inicial)):

            if estadoCelda == 0:
                if str(separacion_Inicial[celda]) == 'C':
                    estadoCelda = 1
                continue
            if estadoCelda == 1:
                if str(separacion_Inicial[celda]) == 'E':
                    estadoCelda = 2
                continue
            if estadoCelda == 2:
                if str(separacion_Inicial[celda]) == 'L':
                    estadoCelda = 3
                continue
            if estadoCelda == 3:
                if str(separacion_Inicial[celda]) == 'D':
                    estadoCelda = 4
                continue
            if estadoCelda == 4:
                if str(separacion_Inicial[celda]) == 'A':
                    estadoCelda = 5
                continue
            if estadoCelda == 5:
                if str(separacion_Inicial[celda]) == 'S':
                    estadoCelda = 6
                continue
            if estadoCelda == 6:
                if str(separacion_Inicial[celda]) == ' ':
                    estadoCelda = 6
                if str(separacion_Inicial[celda]) == '=':
                    estadoCelda = 7
                continue
            if estadoCelda == 7:
                if str(separacion_Inicial[celda]) == ' ':
                    estadoCelda = 7
                if str(separacion_Inicial[celda]) == '{':
                    estadoCelda = 8
                    lista_informacion_filtrada.append('celda')
        # Buscamos filtro
        for filtro in range(0,len(separacion_Inicial)):

            if estadoFiltro == 0:
                if str(separacion_Inicial[filtro]) == 'F':
                    estadoFiltro = 1
                continue
            if estadoFiltro == 1:
                if str(separacion_Inicial[filtro]) == 'I':
                    estadoFiltro = 2
                continue
            if estadoFiltro == 2:
                if str(separacion_Inicial[filtro]) == 'L':
                    estadoFiltro = 3
                continue
            if estadoFiltro == 3:
                if str(separacion_Inicial[filtro]) == 'T':
                    estadoFiltro = 4
                continue
            if estadoFiltro == 4:
                if str(separacion_Inicial[filtro]) == 'R':
                    estadoFiltro = 5
                continue
            if estadoFiltro == 5:
                if str(separacion_Inicial[filtro]) == 'O':
                    estadoFiltro = 6
                continue
            if estadoFiltro == 6:
                if str(separacion_Inicial[filtro]) == 'S':
                    estadoFiltro = 7
                continue
            if estadoFiltro == 7:

                if str(separacion_Inicial[filtro]) == ' ':
                    estadoFiltro = 7
                if str(separacion_Inicial[filtro]) == '=':
                    estadoFiltro = 8
                continue
            if estadoFiltro == 8:
                if str(separacion_Inicial[filtro]) == ' ':
                    estadoFiltro = 8
                if str(separacion_Inicial[filtro]) != ';':
                    estadoFiltro = 8
                    cacheFiltro = cacheFiltro + str(separacion_Inicial[filtro])
                if str(separacion_Inicial[filtro]) ==';':
                    print('estos son los filtros: ',cacheFiltro)
                    lista_informacion_filtrada.append(cacheFiltro)


        for separado in range(0, len(separacion_Inicial)):
            if estadoSeparador == 0:
                if str(separacion_Inicial[separado]) == '@':
                    estadoSeparador = 1
                continue
            if estadoSeparador == 1:
                if str(separacion_Inicial[separado]) == '@':
                    estadoSeparador = 2
                continue
            if estadoSeparador == 2:
                if str(separacion_Inicial[separado]) == '@':
                    estadoSeparador = 3
                continue
            if estadoSeparador == 3:
                if str(separacion_Inicial[separado]) == '@':
                    lista2D.append(lista_informacion_filtrada)
    print('lista de listas', lista2D)

def Analizar():
    dir =  ruta
    print('Se analizara el archivo')
    print(dir)
    primeras_lineas = Abrir_Archivo(dir)
    AFD(primeras_lineas)

def Abrir():
    new = Toplevel(window)
    new.geometry("500x500")
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
    my_button = Button(new,text='Delete')
    my_button.pack(pady=10)

    my_button2 = Button(new,text='Select',command = select)
    my_button2.pack(pady=10)

    global my_label
    my_label = Label(new,text='')
    my_label.pack(pady=5)

def delete():
    my_listbox.delete(ANCHOR)
def select():
    my_label.config(text=my_listbox.get(ANCHOR))
    nombreImagen = my_listbox.get(ANCHOR)
    print(nombreImagen)
    return nombreImagen
def Ver_Imagen():
    try:
        ruta = 'Imagenes/'+str(select())
        print(ruta)
        imagen = Image.open(ruta)
        photo = ImageTk.PhotoImage(imagen)
        etiquetaFoto = tkinter.Label(window,image=photo).place(x=250,y=50,width=450,height=600)
    except:
        print('Error en funcion selecto no ha seleccionado nada')







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
    try:
        global imagen
        imagen = Image.open('Imagenes/Cara.png')
        global photo
        photo = ImageTk.PhotoImage(imagen)
        global etiquetaFoto
        etiquetaFoto = tkinter.Label(window,image=photo).place(x=250,y=50,width=450,height=600)
    except:
        print('Error en funcion selecto no ha seleccionado nada')

    window.mainloop()
