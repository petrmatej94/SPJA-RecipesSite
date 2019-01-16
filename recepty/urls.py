from django.conf.urls import url, include
from . import views


app_name = 'recepty'


urlpatterns = [
    # /recepty/
    url(r'^$', views.index, name='index'),

    # /recepty/kuchari/
    url(r'kuchari/$', views.kuchari, name='kuchari'),

    # /recepty/kuchari/<kuchar_id>/
    url(r'^kuchari/(?P<kuchar_id>[0-9]+)/$', views.detailKuchare, name='detailkuchare'),

    # /recepty/svetovakuchyne/
    url(r'svetovekuchyne/$', views.svetoveKuchyne, name='svetovekuchyne'),

    # /recepty/svetovakuchyne/<svetovakuchyne_id>/
    url(r'^svetovakuchyne/(?P<kuchyne_id>[0-9]+)/$', views.detailKuchyne, name='detailkuchyne'),

    # /recepty/recepty/
    url(r'recepty/$', views.recepty, name='recepty'),

    # /recepty/zprava/
    url(r'zprava/$', views.zprava, name='zprava'),

    # /recepty/recepty/<recept_id>/
    url(r'^recepty/(?P<recept_id>[0-9]+)/$', views.detailReceptu, name='detailreceptu'),

    # /recepty/pridatrecept/
    url(r'pridatrecept/$', views.pridatRecept, name='pridatrecept'),

    # /recepty/registrace/
    url(r'registrace/$', views.novyUzivatel, name='novyuzivatel'),

    # /recepty/users
    url(r'users/', include('django.contrib.auth.urls'), name='login'),

    # /recepty/users/<uzivatel_id>/
    url(r'^users/(?P<uzivatel_id>[0-9]+)/$', views.profil, name='profil'),

    # /recepty/hledani/
    url(r'hledani/$', views.hledani, name='hledani'),

    # /recepty/clanky/
    url(r'clanky/$', views.clanky, name='clanky'),

    # /recepty/clanky/<clanek_id>/
    url(r'^clanky/(?P<clanek_id>[0-9]+)/$', views.detailClanku, name='detailclanku'),

    # /recepty/pridatclanek/
    url(r'pridatclanek/$', views.pridatClanek, name='pridatclanek'),

    # /recepty/chody/
    url(r'chody/$', views.chody, name='chody'),

    # /recepty/chody/<chod_id>/
    url(r'^chody/(?P<chod_id>[0-9]+)/$', views.detailChodu, name='detailchodu'),

]
