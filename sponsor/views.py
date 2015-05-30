from django.template import loader
from django.http import HttpResponse
from sponsor.models import Sponsor, SponsorshipInformation, SponsorRow
from sitelevel import context_builder


def index(request):
    club_sponsors = Sponsor.objects.filter(is_club_sponsor=True)
    squad_sponsors = Sponsor.objects.filter(is_squad_sponsor=True)

    club_sponsor_rows = []
    counter = 0
    for sponsor in club_sponsors:
        if counter % 2 == 0:
            current_club_sponsor_row = SponsorRow(sponsor)
            club_sponsor_rows.append(current_club_sponsor_row)
        else:
            current_club_sponsor_row = club_sponsor_rows[-1]
            current_club_sponsor_row.right = sponsor
        counter += 1

    squad_sponsor_rows = []
    counter = 0
    for sponsor in squad_sponsors:
        if counter % 2 == 0:
            current_squad_sponsor_row = SponsorRow(sponsor)
            squad_sponsor_rows.append(current_squad_sponsor_row)
        else:
            current_squad_sponsor_row = squad_sponsor_rows[-1]
            current_squad_sponsor_row.right = sponsor
        counter += 1

    sponsorship = SponsorshipInformation.objects.first()

    context = context_builder.create_context({'club_sponsors': club_sponsor_rows,
                                              'squad_sponsors': squad_sponsor_rows,
                                              'sponsorship': sponsorship})
    template = loader.get_template('sponsor/index.html')

    return HttpResponse(template.render(context))