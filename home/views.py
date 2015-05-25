from django.template import loader, Context
from django.http import HttpResponse
from home.models import Home
from sitelevel import context_builder

def index(request):
    home = Home.objects.all().first()
    template = loader.get_template('home/index.html')
    context = context_builder.create_context('home', home)
    return HttpResponse(template.render(context))


def test(request):
    template = loader.get_template('test/test.html')
    context = Context({'message': 'Hello Test'})
    return HttpResponse(template.render(context))
