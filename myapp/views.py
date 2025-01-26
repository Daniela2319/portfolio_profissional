from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contato


# Create your views here.
def index(request):
    return render(request, "base.html")


def home_view(request):
    return render(request, "myapp/home.html")


def sobre_view(request):
    return render(request, "myapp/sobre.html")


def projeto_view(request):
    return render(request, "myapp/projeto.html")


# def contato_view(request):
#     return render(request, "myapp/contato.html")


@csrf_exempt
def contato_view(request):
    mensagem = None
    estilo = None

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem_texto = request.POST.get("mensagem")

        if not nome or not email or not mensagem_texto:
            mensagem = "Todos os campos são obrigatórios!"
            estilo = "error"
        else:
            # Enviar o e-mail
            assunto = f"Novo contato de {nome}"
            mensagem_completa = (
                f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{mensagem_texto}"
            )
            destinatario = "dani.edu.java@gmail.com"

            try:
                send_mail(
                    assunto,
                    mensagem_completa,
                    "dani.edu.java@gmail.com",
                    [destinatario],
                )
                mensagem = "E-mail enviado com sucesso!"
                estilo = "success"
            except Exception as e:
                print(f"Erro ao enviar e-mail: {e}")
                mensagem = "Erro ao enviar o e-mail."
                estilo = "error"

    return render(
        request, "myapp/contato.html", {"mensagem": mensagem, "estilo": estilo}
    )
