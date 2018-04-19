from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, White Wolf Player.")

