from django.http import HttpResponse

def mostrar_cadena(request, cadena):
    return HttpResponse(f"El username es: {cadena}")
