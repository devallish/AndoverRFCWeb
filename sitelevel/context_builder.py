from sitelevel.models import SquadMenuItem
from django.template import Context


def get_junior_squad_menu_items():
    junior_squad_menu_items = SquadMenuItem.objects.filter(is_junior=True).order_by('ordinal_position')
    return junior_squad_menu_items.all()


def get_senior_squad_menu_items():
    senior_squad_menu_items = SquadMenuItem.objects.filter(is_junior=False).order_by('ordinal_position')
    return senior_squad_menu_items.all()


def create_context(model_name, model):
    junior_menu_items = get_junior_squad_menu_items()
    senior_menu_items = get_senior_squad_menu_items()
    context = Context({model_name: model, 'junior_menu_items': junior_menu_items, 'senior_menu_items': senior_menu_items})
    return context