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

import cv2
nombre = 'jade'
direccion = 'Imagenes/'+nombre+'jpg'
img = cv2.imread('Imagenes/Cara')


