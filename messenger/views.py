from django.shortcuts import render


def messenger(request):
    return render(request, 'lvlup/messenger.html')
