from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "member/index.html")

def htoo(request):
    return render(request, "member/htoo.html")

def shin(request):
    return render(request, "member/shin.html")

def zin(request):
    return render(request, "member/zin.html")

def yoe(request):
    return render(request, "member/yoe.html")

def kyaw(request):
    return render(request, "member/kyaw.html")

def zar(request):
    return render(request, "member/zar.html")