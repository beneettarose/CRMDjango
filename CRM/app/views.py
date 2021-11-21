from django.shortcuts import redirect, render

# Create your views here.

def adminDashboard(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username=='admin' and password=='admin'):
            return redirect('adminDashboard')
    
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def client(request):
    return render(request, 'client.html')

def quotation(request):
    return render(request, 'quotation.html')

