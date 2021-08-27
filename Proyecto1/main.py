import tkinter
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox



#Variables Globales
ruta = ''

def Abrir():
    print('Abriendo imagen')


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
    for i in range(0,len(lista_lineas)):
        separacion_Inicial = list(lista_lineas[i])
        print(separacion_Inicial)
        estadoNombre = 0
        estadoAncho = 0
        estadoAlto = 0
        estadoFilas = 0
        estadoColumna = 0
        estadoCeldas = 0
        estadoFiltros = 0
        cacheNombre = ''
        cacheAncho = ''
        cacheAlto = ''
        cacheFilas = ''
        for ancho in range(0,len(separacion_Inicial)):
            # Buscamos Ancho
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

        for alto in range(0,len(separacion_Inicial)):
            # Buscamos el alto
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
                    estadoAlto = 0
                continue


        for filas in range(0,len(separacion_Inicial)):
            # Buscamos el filas
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

        for columnas in range(0,len(separacion_Inicial)):
            # Buscamos columnas
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
            if estadoFilas == 6:
                if str(separacion_Inicial[columnas]) != 'A':
                    estadoFilas = 6
                    cacheFilas = cacheFilas + str(separacion_Inicial[filas])
                if str(separacion_Inicial[filas]) == ';':
                    print('este es el numero de filas',cacheFilas )



        for j in range(0,len(separacion_Inicial)):
            # Buscamos titulo
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






def Analizar():
    dir =  ruta
    print('Se analizara el archivo')
    print(dir)
    primeras_lineas = Abrir_Archivo(dir)
    AFD(primeras_lineas)



def interfaz_grafica():
    window = tkinter.Tk()
    window.title("Bitxelart")
    window.geometry('800x600')
    menubar = tkinter.Menu(window)
    window.config(menu=menubar)
    # Creamos menu
    filemenu = tkinter.Menu(menubar)
    # Creamos File item
    filemenu.add_separator()
    menubar.add_cascade(label='Cargar Archivo',command=Cargar_Archivo)


    #Crear analizar itme
    analizarmenu = tkinter.Menu(menubar)
    analizarmenu.add_separator()
    menubar.add_cascade(label='Analizar',command = Analizar)

    #Crear Reportes
    reportesmenu = tkinter.Menu(menubar)
    # Creamos File item
    reportesmenu.add_separator()

    #Seleccionar Imagen
    seleccionar = tkinter.Menu(menubar)
    menubar.add_cascade(label='Seleccionar Imagenes', command=saludo)
    carpeta = os.listdir('Imagenes')
    for imagenes in range (0,len(carpeta)):
        seleccionar.add_cascade(label=str(carpeta[imagenes]),command=Abrir,menu=seleccionar)



    # Crear Salir items
    reportesmenu = tkinter.Menu(menubar)
    # Creamos Salir item
    reportesmenu.add_separator()
    menubar.add_cascade(label='Salir', command=window.quit)

    tkinter.Button(window, text="Original").pack(side='left')
    tkinter.Button(window, text="Mirror X").pack(side='left')
    tkinter.Button(window, text="Mirror Y").pack(side='left')
    tkinter.Button(window, text="Doble Mirror").pack(side='left')



    #boton1 = tkinter.Button(window, text ='Boton1',command=lambda: saludo("python") )



    window.mainloop()


if __name__ == '__main__':

    print('generano interfaz Bitxelart')
    interfaz_grafica()