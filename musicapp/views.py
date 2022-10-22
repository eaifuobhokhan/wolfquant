from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to WolfofQuant's music app! Enjoy Aye by Davido")