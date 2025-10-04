from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from faker import Faker
from .models import Users

# Create your views here.
def home(request):
    return render(request, "app/index.html")


# ---------------------- Login page views ------------------------------

def login(request):
    return render(request, "app/login.html")

class CreatePassphraseView():
    def get(self, request):
        wordlist = []
        fake = Faker()

        for i in range(12):
            wordlist[i] = fake.word()
        
        return JsonResponse({"ok": True, "wordlist": wordlist})
    
class RegisterAccountView():
    def put(self, request):
        username = request.data.get("username")
        
        if Users.objects.filter(username=username).exists():
            return JsonResponse({"ok": False, "error": "Username already exists"}, status=400)
        
        