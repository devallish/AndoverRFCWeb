from django.contrib import admin
from squad.models import Squad, SquadRole, SquadPersonRole, SquadSelection, SquadSelectionItem


class SquadAdmin(admin.ModelAdmin):
    list_display = ('display_name', )
    filter_horizontal = ('news_articles', 'fixtures', 'people', 'sponsors', 'selection',)

admin.site.register(Squad, SquadAdmin)
admin.site.register(SquadRole)
admin.site.register(SquadPersonRole)
admin.site.register(SquadSelection)
admin.site.register(SquadSelectionItem)