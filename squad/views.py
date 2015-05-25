from squad.models import Squad
from django.template import loader
from django.http import HttpResponse
from sitelevel import context_builder
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('squad/index.html')


def details(request, squad_id):
    squad = Squad.objects.get(id=squad_id)
    template = loader.get_template('squad/details.html')
    context = context_builder.create_context('squad', squad)
    return HttpResponse(template.render(context))