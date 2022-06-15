from django.http import HttpResponse #
from django.template import Template, Context #

def inicio( request ):
    doc_externo = open("static/index.html") #declara una variable con el archivo html
    plt = Template(doc_externo.read()) #lee el archivo html
    doc_externo.close() #cierra el archivo
    ctx = Context () #declara una variable de contexto, esta funcionando como python, que pueda reconocer lenguaje python y poder ejecutar codigo
    documento = plt.render(ctx) #renderiza el archivo html
    return HttpResponse(documento) #retorna el archivo html

def productos( request ):
    doc_externo = open("static/productos.html") #declara una variable con el archivo html
    plt = Template(doc_externo.read()) #lee el archivo html
    doc_externo.close() #cierra el archivo
    ctx = Context () #declara una variable de contexto, esta funcionando como python, que pueda reconocer lenguaje python y poder ejecutar codigo
    documento = plt.render(ctx) #renderiza el archivo html
    return HttpResponse(documento) #retorna el archivo html

def CarritoCompra( request ):
    doc_externo = open("static/carritoCompra.html") #CarritoCompra.html
    plt = Template(doc_externo.read()) #lee el archivo html
    doc_externo.close() #cierra el archivo
    ctx = Context () #declara una variable de contexto, esta funcionando como python, que pueda reconocer lenguaje python y poder ejecutar codigo
    documento = plt.render(ctx) #renderiza el archivo html
    return HttpResponse(documento) #retorna el archivo html


def donacion( request ):
    doc_externo = open("static/donacion.html") #CarritoCompra.html
    plt = Template(doc_externo.read()) #lee el archivo html
    doc_externo.close() #cierra el archivo
    ctx = Context () #declara una variable de contexto, esta funcionando como python, que pueda reconocer lenguaje python y poder ejecutar codigo
    documento = plt.render(ctx) #renderiza el archivo html
    return HttpResponse(documento) #retorna el archivo html

def seguimiento( request ):
    doc_externo = open("static/seguimiento.html") #CarritoCompra.html
    plt = Template(doc_externo.read()) #lee el archivo html
    doc_externo.close() #cierra el archivo
    ctx = Context () #declara una variable de contexto, esta funcionando como python, que pueda reconocer lenguaje python y poder ejecutar codigo
    documento = plt.render(ctx) #renderiza el archivo html
    return HttpResponse(documento) #retorna el archivo html