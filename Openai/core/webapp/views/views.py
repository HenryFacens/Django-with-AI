from django.shortcuts import render

def correcao(request):
    return render(request,"correcao.html",{"teste":"teste123"})