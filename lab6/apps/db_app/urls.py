from django.conf.urls import url
from lab6.apps.db_app import views


urlpatterns = [
    url(r'^main/', views.main, name='main_url'),
    url(r'^registration2/', views.registration2, name='reg2_url'),
    url(r'^login/', views.login, name='login_url'),
    url(r'^account/', views.account, name='account_url'),
    url(r'^logout/', views.logout, name='logout_url'),
    url(r'^film/get/(?P<pk>\d+)/$', views.FilmDetailView.as_view(), name='film_url'),
    url(r'^page/(\d+)/$', views.main, name='page_url'),
]
