from django.shortcuts import render


# asdasd
def index(request):
    return render(request, 'splash/index.html')
