from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    today = str(datetime.now().date())
    context = {'today': today}
    return render(request, 'menus/index.html', context=context)