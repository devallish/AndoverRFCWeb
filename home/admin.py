from django.contrib import admin
from home.models import Home, CarouselItem


class HomeAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
    filter_horizontal = ('carousel_items', 'news_articles', 'events', 'fixtures', 'sponsors', )


admin.site.register(Home, HomeAdmin)
admin.site.register(CarouselItem)