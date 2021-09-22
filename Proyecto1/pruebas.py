#import imgkit
#imgkit.from_string('Hello!', 'out2.jpg')
#css = 'HTML Y CSS/Pokebola.css'
#options = {
#    'format': 'jpg',
#    'encoding': "UTF-8",
#    'enable-local-file-access': ''
#}

#imgkit.from_file('HTML y CSS/Pokebola.html','output.jpg',css=css,options=options)

#from html2image import Html2Image
#hti = Html2Image()
#html = 'HTML y CSS/Pokebola.html'
#css = 'HTML y CSS/Pokebola.css'

#hti.screenshot(
#    html_file=html, css_file=css,
#    size=(400, 400),
#    save_as='blue_page.png'

#)

lista1 = []
lista2 = []
tamañoF = 3
tamañoC = 3
for i in range(0,tamañoF):
    for j in range(0,tamañoC):
        lista1.append(str(i+1)+str(j+1))
    lista2.append(lista1)
    lista1 = []
print(lista2)


for xi in range(0,tamañoF):
    for yi in range(0,tamañoC):
        print('Recorrido Normal',lista2[xi][yi])
for hi in range(tamañoF-1,-1,-1):
    for ki in range(tamañoC-1,-1,-1):
        print('Recorrido DobleMirror',lista2[hi][ki])
for li in range(0,tamañoF):
    for mi in range(tamañoC-1,-1,-1):
        print('Recorrido Espejo en x',lista2[li][mi])
for oi in range(tamañoF-1,-1,-1):
    for pi in range(0,tamañoC):
        print('Recorrido Espejo en y',lista2[oi][pi])



