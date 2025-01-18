send_mail(
    "Teste de E-mail",
    "Este é um teste do Django para envio de e-mail.",
    "dani.edu.java@gmail.com",  # Altere para o mesmo que EMAIL_HOST_USER
    ["frankvt04@gmail.com"],  # Substitua pelo e-mail de destino
    fail_silently=False,  # Mostra erros caso ocorram
)