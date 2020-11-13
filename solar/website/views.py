from django.shortcuts import render
 
def hello_solar (request):
    return render(request, "index.html")

