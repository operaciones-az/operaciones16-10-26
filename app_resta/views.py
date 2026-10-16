from django.shortcuts import render
from app_resta.resta_logic import restar

def resta_view(request):
    num1 = 10
    num2 = 4
    resultado = restar(num1, num2)
    
    contexto = {
        'num1': num1,
        'num2': num2,
        'resultado': resultado
    }
    return render(request, 'index.html', contexto)