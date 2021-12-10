
from django.contrib import admin
from django.urls import path
#importar a vies e dando nome de  auth_views
from django.contrib.auth import views as auth_views

from dashboard.views import index

from visitantes.views import(
    finalizar_visita, registar_visitante, informacoes_visitantes,
) 

#IMPORTAR AS VIEWS PARA ESTA URL


#colocar aspas duplas
urlpatterns = [
    path("admin/", admin.site.urls),

    #url de login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name = "login.html"
        ),
        name = "login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name = "logout.html"
        ),
        name = "logout"
    ),

    path(
        "",
        index,
        name="index"
    ),

    path(
        "registrar-visitante/",
        registar_visitante,
        name="registrar_visitante"
    ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitantes,
        name="informacoes_visitantes",
    ),

    path(
        "visitantes/<int:id>/finalizar-visita/",
        finalizar_visita,
        name="finalizar_visita",
    ),

]

