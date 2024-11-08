from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Kategoria
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import tranzakcje
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import KategoriaForm,PodkategoriaForm,KategoriaForm2,KategoriaForm3
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.utils import timezone

#views dla kategroii
def kategorie_view(request):
    kategorie = Kategoria.objects.prefetch_related('tranzakcje').filter(user=request.user)
    return render(request, 'kategorie_tranzakcje.html', {'kategorie': kategorie})

@login_required
def kategorie_tranzakcje(request):
    # Pobieramy kategorie przypisane do aktualnego użytkownika
    kategorie = Kategoria.objects.filter(user=request.user)
    return render(request, 'kategorie_tranzakcje.html', {'kategorie': kategorie})

@csrf_exempt  # Dodaj to tylko, jeśli masz problemy z CSRF
def update_realization(request, tranzakcja_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        realization = data.get('realization')

        try:
            # Zakładając, że masz model Transaction
            transaction = tranzakcje.objects.get(id=tranzakcja_id)
            transaction.realizacja = realization
            transaction.save()

            return JsonResponse({'status': 'success'})
        except tranzakcje.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Transaction not found'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# koniec

def user_login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')  
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)  
            return redirect('kategorie_view')  
        else:
            return HttpResponse("Hasło lub Login jest nie poprawny!!!")

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')

@login_required(login_url='login')
def dodaj_kategorie(request):
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            kategoria = form.save(commit=False)
            kategoria.user = request.user  # Automatycznie przypisujemy użytkownika
            kategoria.save()
            return redirect('kategorie_view')  # Po zapisaniu przekierowujemy do listy kategorii
    else:
        form = KategoriaForm()

    return render(request, 'dodaj_kategorie.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'html.html')  

def dodaj_podkategorie(request):
    # Pobieramy wszystkie kategorie użytkownika
    kategorie = Kategoria.objects.filter(user=request.user)

    if request.method == 'POST':
        form = PodkategoriaForm(request.POST)
        if form.is_valid():
            podkategoria = form.save(commit=False)
            podkategoria.user = request.user  # Automatycznie przypisujemy użytkownika
            podkategoria.save()
            return redirect('kategorie_view')  # Przekierowanie do strony z kategoriami
    else:
        form = PodkategoriaForm()

    return render(request, 'dodaj_podkategorie.html', {'form': form, 'kategorie': kategorie})

def edytuj_kategorie(request, kategoria_id):
    kategoria = get_object_or_404(Kategoria, id=kategoria_id)  # Pobierz kategorię
    if request.method == 'POST':
        form = KategoriaForm2(request.POST, instance=kategoria)
        if form.is_valid():
            form.save()  # Zapisz zmiany w kategorii
            return redirect('kategorie_view')  # Przekierowanie po zapisaniu
    else:
        form = KategoriaForm2(instance=kategoria)  # Wypełnij formularz aktualnymi danymi

    return render(request, 'edytuj_kategorie.html', {'form': form, 'kategoria': kategoria})

def edytuj_podkategorie(request, tranzakcja_id):
    tranzakcje = get_object_or_404(tranzakcje, id=tranzakcja_id)  # Pobierz kategorię
    if request.method == 'POST':
        form = KategoriaForm3(request.POST, instance=tranzakcje)
        if form.is_valid():
            form.save()  # Zapisz zmiany w kategorii
            return redirect('kategorie_view')  # Przekierowanie po zapisaniu
    else:
        form = KategoriaForm3(instance=tranzakcje)  # Wypełnij formularz aktualnymi danymi

    return render(request, 'edytuj_podkategorie.html', {'form': form, 'tranzakcje': tranzakcje})
from django.views.decorators.http import require_POST

@csrf_exempt
def update_realization(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tranzakcja_id = data.get('tranzakcja_id')
        plan = float(data.get('plan', 0))  # Konwersja na float
        
        try:
            # Pobieramy transakcję i aktualizujemy pole realizacja
            tranzakcja = tranzakcje.objects.get(id=tranzakcja_id)
            tranzakcja.realizacja = plan  # Zapisujemy jako float
            tranzakcja.save()
            
            return JsonResponse({'status': 'success', 'realizacja': f"{tranzakcja.realizacja:.2f}"})
        except tranzakcje.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Nie znaleziono transakcji.'})
    return JsonResponse({'status': 'error', 'message': 'Błędne żądanie.'})
from django.http import HttpResponseForbidden

@login_required
def edytuj_podkategorie(request, tranzakcja_id):
    # Pobieramy transakcję po ID
    tranzakcja = get_object_or_404(tranzakcje, id=tranzakcja_id)

    # Sprawdzamy, czy użytkownik jest właścicielem tej transakcji
    if tranzakcja.user != request.user:
        return HttpResponseForbidden("Nie masz uprawnień do edycji tej transakcji.")

    # Obsługa formularza po POST
    if request.method == 'POST':
        form = KategoriaForm3(request.POST, instance=tranzakcja)
        if form.is_valid():
            form.save()  # Zapisz zmiany w transakcji
            return redirect('kategorie_view')  # Przekierowanie po zapisaniu
    else:
        form = KategoriaForm3(instance=tranzakcja)  # Wypełnij formularz aktualnymi danymi

    return render(request, 'edytuj_podkategorie.html', {'form': form, 'tranzakcja': tranzakcja})

def usun_podkategorie(request, tranzakcja_id):
    tranzakcja = get_object_or_404(tranzakcje, id=tranzakcja_id)
    tranzakcja.delete()  # Usuwa podkategorię z bazy danych
    return redirect('kategorie_view')  # Po usunięciu przekierowanie do widoku kategorii

def usun_kategorie(request, kategoria_id):
    kategoria = get_object_or_404(Kategoria, id=kategoria_id)
    kategoria.delete()  # Usuwa kategorię z bazy danych
    return redirect('kategorie_view')  # Po usunięciu przekierowanie do widoku kategorii

def roczny_wykres(request):
    # Pobieramy wszystkie kategorie i sumujemy plan i realizację dla każdego miesiąca
    kategorie = Kategoria.objects.all()

    # Przygotowanie danych do wykresu
    miesiace = [i for i in range(1, 13)]  # Miesiące w roku (1-12)
    plany = [0] * 12  # Lista do przechowywania sum planów dla każdego miesiąca
    realizacje = [0] * 12  # Lista do przechowywania sum realizacji dla każdego miesiąca

    for kategoria in kategorie:
        for tranzakcja in kategoria.tranzakcje.all():
            miesiac = tranzakcja.miesiac - 1  # Indeks miesiąca (0-11)
            plany[miesiac] += tranzakcja.plan
            realizacje[miesiac] += tranzakcja.realizacja

    # Przekazanie danych do szablonu
    context = {
        'miesiace': miesiace,
        'plany': plany,
        'realizacje': realizacje
    }

    return render(request, 'wykres.html', context)