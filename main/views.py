from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306222765',
        'name': 'Ardi Syahputra Amin',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
