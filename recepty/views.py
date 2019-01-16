from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.contrib.auth import logout


def index(request):
    return render(request, 'recepty/index.html')
    #vypise nejake menu - treba Recepty, Kuchari, Svetova kuchyne


def recepty(request):
    rec = Recept()
    all_recepty = Recept.objects.all()
    context = {'all_recepty': all_recepty}
    return render(request, 'recepty/recepty.html', context)


def detailReceptu(request, recept_id):
    if request.method == "POST":
        if 'funkce_1' in request.POST:
            form = PridatKomentar(request.POST)
            if form.is_valid():
                komentar = form.save(commit=False)
                komentar.autor = request.user
                komentar.komentovany_recept = Recept.objects.get(id=recept_id)
                komentar.save()
                return redirect('recepty:detailreceptu', recept_id)

        if 'funkce_2' in request.POST:
            form = HodnoceniReceptu(request.POST)
            if form.is_valid():
                recept = Recept.objects.get(id=recept_id)
                recept.hodnotit(form.cleaned_data.get('hodnoceni'))
                recept.save()
                return redirect('recepty:detailreceptu', recept_id)
            return redirect('recepty:detailreceptu', recept_id)
    else:
        form1 = PridatKomentar()
        form2 = HodnoceniReceptu()
        recept = get_object_or_404(Recept, pk=recept_id)
        all_komentare = Komentar.objects.filter(komentovany_recept=recept_id).order_by("publikovano")[:2]
        return render(request, 'recepty/detailreceptu.html', {'recept': recept, 'all_komentare': all_komentare,
                                                              'form1': form1, 'form2': form2})
        # vypise detaily zvoleneho receptu - postup, ingredience...


def detailKuchyne(request, kuchyne_id):
    kuchyne = get_object_or_404(SvetovaKuchyne, pk=kuchyne_id)
    all_recepty = Recept.objects.filter(svetova_kuchyne=kuchyne_id)
    return render(request, 'recepty/detailkuchyne.html', {'kuchyne': kuchyne, 'all_recepty': all_recepty})
    #vypise recepty z dane kuchyne


def svetoveKuchyne(request):
    all_kuchyne = SvetovaKuchyne.objects.all()
    context = {'all_kuchyne': all_kuchyne}
    return render(request, 'recepty/svetovekuchyne.html', context)
    #Italska, ceska, ...


def kuchari(request):
    all_kuchari = User.objects.all()
    context = {'all_kuchari': all_kuchari}
    return render(request, 'recepty/kuchari.html', context)
    #vypise jmena kucharu


def detailKuchare(request, kuchar_id):
    kuchar = get_object_or_404(User, pk=kuchar_id)
    all_recepty = Recept.objects.filter(autor=kuchar_id)



    celkoveHodnoceni = Recept.celkoveHodnoceni(kuchar_id)

    return render(request, 'recepty/detailkuchare.html', {'kuchar': kuchar, 'all_recepty': all_recepty, 'celkoveHodnoceni': celkoveHodnoceni})
    #vypise detail kuchare - jeho recepty + svetovou kuchyni


def profil(request, uzivatel_id):
    uzivatel = get_object_or_404(User, pk=uzivatel_id)
    all_recepty = Recept.objects.filter(autor=uzivatel_id)
    return render(request, 'recepty/profil.html', {'uzivatel': uzivatel, 'all_recepty': all_recepty})


def pridatRecept(request):
    if request.method == "POST":
        form = PridatRecept(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #recept = Recept.objects.get(pk=course_id)
            post.autor = request.user
           # fotogalerie.fotka = form.cleaned_data['fotka']
            post.save()
            return redirect('recepty:detailreceptu', post.pk)
    else:
        form = PridatRecept()
        return render(request, 'recepty/pridatrecept.html', {'form': form})


def novyUzivatel(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('recepty:index')
            return redirect('recepty:registrace')
        return redirect('recepty:registrace')
    else:
        form = UserCreationForm
        return render(request, 'recepty/registrace.html', {'form': form})


def zprava(request):
    if request.method == "POST":
        form = OdeslatZpravu(request.POST)
        if form.is_valid():
            form.save()
            nadpis = form.cleaned_data['nadpis']
            text = form.cleaned_data['text']
            odesilatel = form.cleaned_data['odesilatel']
            #send_mail(nadpis, text, odesilatel, ['django.server@seznam.cz'], fail_silently=False,)
            return redirect('recepty:index')
    else:
        form = OdeslatZpravu()
        return render(request, 'recepty/zprava.html', {'form': form})


def hledani(request):
    hledany_vyraz = request.GET.get('hledej_recept')

    if hledany_vyraz is not None:
        recepty = Recept.objects.filter(jmeno__icontains=hledany_vyraz)
    else:
        recepty = None

    return render(request, 'recepty/hledani.html', {'hledany_vyraz': hledany_vyraz, 'recepty': recepty})


def clanky(request):
    all_clanky = Clanek.objects.all().order_by("-publikovano")[:10]
    return render(request, 'recepty/clanky.html', {'all_clanky': all_clanky})


def detailClanku(request, clanek_id):
    clanek = get_object_or_404(Clanek, pk=clanek_id)
    return render(request, 'recepty/detailclanku.html', {'clanek': clanek})


def pridatClanek(request):
    if request.method == "POST":
        form = PridatClanek(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('recepty:detailclanku', post.pk)
    else:
        form = PridatClanek()
        return render(request, 'recepty/pridatclanek.html', {'form': form})


def chody(request):
    all_chody = Chod.objects.all()
    return render(request, 'recepty/chody.html', {'all_chody': all_chody})


def detailChodu(request, chod_id):
    chod = get_object_or_404(Chod, pk=chod_id)
    all_recepty = Recept.objects.filter(chod=chod_id)
    return render(request, 'recepty/detailchodu.html', {'chod': chod, 'all_recepty': all_recepty})


def menu(request):
    pass
    #vypise tip na dnesni menu - nejake nahodne recepty?








