from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from pizzeria.models import Lokal, Uzytkownicy, Pizzza, LokalPizzzaLaczaca, Zamowienia

def index(request):
    if 'zalogowany' in request.session and request.session['zalogowany']:
        return render(request, 'pizzeria/index2.html')
    return render(request, 'pizzeria/index.html')

def admin(request):
    return render(request, 'pizzeria/admin.html')

def index2(request):
    return render(request, 'pizzeria/index2.html')

@csrf_exempt
def zaloguj(request):
    if 'loginLogowanie' not in request.POST or 'hasloLogowanie' not in request.POST:
        return render(request, 'pizzeria/index.html')
    login = request.POST.get('loginLogowanie')
    haslo = request.POST.get('hasloLogowanie')
    request.session.zleDane = "Nieprawidłowy login lub hasło"
    print('jestem Tu nie wszedłem jeszcze')
    iluUserow = Uzytkownicy.objects.filter(user = login, pass_field = haslo)
    if len(iluUserow) > 0:
        print('Udalo sie wejsc')
        request.session.id = iluUserow[0].id
        request.session.user = iluUserow[0].user
        request.session.emailLogowanie = iluUserow[0].email
        request.session.rola = iluUserow[0].rola
        request.session.zleDane = ""
    else:
        request.session.zleDane = 'Nieprawidłowy login lub hasło'
    return JsonResponse({'id':request.session.id, 'user': request.session.user, 'emailLogowanie': request.session.emailLogowanie, 'rola': request.session.rola, 'zleDane': request.session.zleDane})





@csrf_exempt
def ajax(request):
    # Zakładamy ze wszystko jest dobrze
    wszystko_OK = True
    #Sprawdzamy Nick
    nick = request.POST.get('login')
    if len(nick) < 3 or len(nick) > 20:
            print("Wszedłem tutaj")
            wszystko_OK = False
            request.session.e_nick = "Nick musi posiadac od 3 do 20 znakow"
    else:
        request.session.e_nick = ""
    #Sprawdzamy mail
    email = request.POST.get('email')
    if email == "":
        wszystko_OK = False
        request.session.e_email = "Zly mail"
    else:
        request.session.e_email = ""
    #Sprawdzamy haslo
    haslo1 = request.POST.get('haslo1')
    haslo2 = request.POST.get('haslo2')

    if len(haslo1) < 8 or len(haslo1) > 20:
        wszystko_OK = False
        request.session.e_haslo = "Hasło musi posiadać od 8 do 20 znaków"
    else:
        request.session.e_haslo = ""

    if haslo1 != haslo2:
        wszystko_OK = False
        request.session.e_hasloRowne = "Podane hasła nie są takie same"
    else:
        request.session.e_hasloRowne = ""

    #Zapamietaj wprowadzone dane
    request.session.fr_nick = nick
    request.session.fr_email = email
    request.session.fr_haslo1 = haslo1
    request.session.fr_haslo2 = haslo2

    print(len(Uzytkownicy.objects.filter(email = email)))

    if len(Uzytkownicy.objects.filter(email = email))>0:
        wszystko_OK = False
        request.session.e_email = "Istnieje juz użytkownik z takim mailem"
    if len(Uzytkownicy.objects.filter(user = nick)) >0:
        wszystko_OK = False
        request.session.e_nick = "Istnieje już konto o takim nicku"
    if wszystko_OK:
        user = Uzytkownicy(user = nick, pass_field = haslo1, zamowienia = None, email = email, rola='USER')
        user.save()
        request.session.udanarejestracja = True
        return JsonResponse({'e_nick': request.session.e_nick, 'e_email': request.session.e_email, 'e_haslo':request.session.e_haslo, 'e_hasloRowne':request.session.e_hasloRowne})
    return JsonResponse({'e_nick': request.session.e_nick, 'e_email': request.session.e_email, 'e_haslo': request.session.e_haslo, 'e_hasloRowne': request.session.e_hasloRowne})




