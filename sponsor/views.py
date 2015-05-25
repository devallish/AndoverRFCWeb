from django.template import loader
from django.http import HttpResponse
from sponsor.models import Sponsor, SponsorshipInformation
from sitelevel import context_builder


def index(request):
    sponsors = Sponsor.objects.first()
    sponsorship = SponsorshipInformation.objects.first()
    template = loader.get_template('sponsor/index.html')
    context = context_builder.create_context({'sponsors': sponsors, 'sponsorship': sponsorship})
    return HttpResponse(template.render(context))
