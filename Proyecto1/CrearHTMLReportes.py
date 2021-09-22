from string import Template
import sys
import webbrowser

#lista = [['TITULO', 'titulo', '1'], ['hola', 'cadena', '1'], [';', 'signo', '2']]
lista2 = list('jfhaskdjhfaksdjfaklsdjhf')
def Reporte_Tokens(lista2D):
    lstdatos = lista2D
    print('Buscando Plantilla')
    archivoEntrada1 = open('plantilla_tokens.txt')
    src1 = Template(archivoEntrada1.read())
    try:
        file2 = open('salidaTokens.txt','w')
        file2.write('')
        print('Limpiando lista Tokens')
        print('Guardando')
    except:
        print('FAllO FATAL No se escribio el archivo salida Tokens .txt')
    file2.close()
    for i in range(0, len(lstdatos)):

        tokens = str(lstdatos[i][0])
        lexema = str(lstdatos[i][1])
        linea =  str(lstdatos[i][2])

        D1 = {'token': tokens, 'lexema': lexema, 'linea': linea, }

        res = src1.substitute(D1)

        try:
            file3 = open('salidaTokens.txt', 'a')
            file3.writelines(res)

        except:
            print('FAllO FATAL No se escribio el archivo salida Tokens .txt')
    print('Creando lista Tokens')
    print('Guardando')
    file3.close()

    print('Creando Reportes')

    parte1 = ''' <!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
      <link href = "Estilos.css" rel="stylesheet">
      <title>LFP1 2021</title>
   </head>
   <body>
      <header class="header">
         <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #0A33B2;">
            <div class="container-fluid">
               <a class="navbar-brand" href="1">BAMB</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                     <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="1">Link</a>
                     </li>
                     <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="1" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Dropdown
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                           <li><a class="dropdown-item" href="1">Action</a></li>
                           <li><a class="dropdown-item" href="1">Another action</a></li>
                           <li>
                              <hr class="dropdown-divider">
                           </li>
                           <li><a class="dropdown-item" href="1">Something else here</a></li>
                        </ul>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link disabled" href="1" tabindex="-1" aria-disabled="true">Disabled</a>
                     </li>
                  </ul>
                  <form class="d-flex">
                     <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                     <button class="btn btn-outline-success" type="submit">Search</button>
                  </form>
               </div>
            </div>
         </nav>
         <div class ="text-header d-flex aling-item-center">
            <div class="container">
               <div class="row">

                  <marquee><h4>Bienvenidos!!! Proyecto 1 LFP by: Alexander Mejia  carnet : 201900576</h4></marquee>
                  <center><h1>REPORTE DE TOKENS</h1></center>

                  <div class="card text-white bg-dark ">
                     <div class="card-header text-center">Listado de tokens</div>
                     <div class="card-body">
                        <table class="table table-striped table-dark">
                           <thead>
                              <tr>
                                 <th scope="col"class="text-center">Token</th>
                                 <th scope="col"class="text-center">Lexema</th>
                                 <th scope="col"class="text-center">Linea</th>

                              </tr>
                           </thead>
                           <tbody>'''
    file4 = open('salidaTokens.txt','r+')
    
    parte2 = file4.read()



    parte3 = ''' </tbody>
                        </table>
                     </div>
                  </div>

               </div>
            </div>
         </div>
      </header>
      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
         <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
         -->
   </body>
</html> '''
    htmltokenscompleto = parte1+str(parte2)+parte3
    file5 = open('ReportesHTML/Reporte_Tokens.html','w')
    file5.write(htmltokenscompleto)
    file4.close()
    file5.close()


def Reporte_Errores(lista1D):
    lstdatos = lista1D
    print('Buscando Plantilla')
    archivoEntrada1 = open('plantilla_errores.txt')
    src1 = Template(archivoEntrada1.read())
    try:
        file2 = open('salidaErrores.txt', 'w')
        file2.write('')
        print('Limpiando lista Errores')
        print('Guardando')
    except:
        print('FAllO FATAL No se escribio el archivo salida Tokens .txt')
    file2.close()
    for i in range(0, len(lstdatos)):

        error = str(lstdatos[i])


        D1 = {'error': error, }

        res = src1.substitute(D1)

        try:
            file3 = open('salidaErrores.txt', 'a')
            file3.writelines(res)

        except:
            print('FAllO FATAL No se escribio el archivo salida Tokens .txt')
    print('Creando lista Tokens')
    print('Guardando')
    #file3.close()

    print('Creando Reportes')

    parte1 = ''' <!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
      <link href = "Estilos.css" rel="stylesheet">
      <title>LFP1 2021</title>
   </head>
   <body>
      <header class="header">
         <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #0A33B2;">
            <div class="container-fluid">
               <a class="navbar-brand" href="1">BAMB</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                     <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="1">Link</a>
                     </li>
                     <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="1" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Dropdown
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                           <li><a class="dropdown-item" href="1">Action</a></li>
                           <li><a class="dropdown-item" href="1">Another action</a></li>
                           <li>
                              <hr class="dropdown-divider">
                           </li>
                           <li><a class="dropdown-item" href="1">Something else here</a></li>
                        </ul>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link disabled" href="1" tabindex="-1" aria-disabled="true">Disabled</a>
                     </li>
                  </ul>
                  <form class="d-flex">
                     <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                     <button class="btn btn-outline-success" type="submit">Search</button>
                  </form>
               </div>
            </div>
         </nav>
         <div class ="text-header d-flex aling-item-center">
            <div class="container">
               <div class="row">

                  <marquee><h4>Bienvenidos!!! Proyecto 1 LFP by: Alexander Mejia  carnet : 201900576</h4></marquee>
                  <center><h1>REPORTE DE ERRORES</h1></center>

                  <div class="card text-white bg-dark ">
                     <div class="card-header text-center">Listado de Errores</div>
                     <div class="card-body">
                        <table class="table table-striped table-dark">
                           <thead>
                              <tr>
                                 <th scope="col"class="text-center">ERRORES</th>
                              </tr>
                           </thead>
                           <tbody> '''
    file4 = open('salidaErrores.txt', 'r+')

    parte2 = file4.read()

    parte3 = ''' </tbody>
                            </table>
                         </div>
                      </div>

                   </div>
                </div>
             </div>
          </header>
          <!-- Optional JavaScript; choose one of the two! -->
          <!-- Option 1: Bootstrap Bundle with Popper -->
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
          <!-- Option 2: Separate Popper and Bootstrap JS -->
          <!--
             <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
             <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
             -->
       </body>
    </html> '''
    htmltokenscompleto = parte1 + str(parte2) + parte3
    file5 = open('ReportesHTML/Reporte_Errores.html', 'w')
    file5.write(htmltokenscompleto)
    file4.close()
    file5.close()


#Reporte_Tokens(lista)
#Reporte_Errores(lista2)