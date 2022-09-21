from applications.home.models import Home

# Processor para recuperar teléfono y correo de la Página Principal (Home)
# Siempre un context processor va a retornar una función

def home_contact(request):
    # Recupero el primer registro Home, similar a la vsta de Home
    home = Home.objects.latest('created')

    return { ## siempre se retorna un diccionario
        'phone': home.phone,
        'correo': home.contacto_email,
    }