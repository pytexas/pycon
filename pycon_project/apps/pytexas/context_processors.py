from django.conf import settings


def pytexas_contexts(request):
    context = {}
    context.update({
        'PYCON_YEAR': settings.PYCON_YEAR
    })
    return context
