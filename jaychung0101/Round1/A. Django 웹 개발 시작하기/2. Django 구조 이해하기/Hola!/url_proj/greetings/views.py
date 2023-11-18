from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse('<h1>Hola! :)</h1>')
