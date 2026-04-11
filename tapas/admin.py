from django.contrib import admin

from .models import Tapa, Color, TapaImage, Caracteristica, Loza, Texto


class TapaImageInlineAdmin(admin.TabularInline):
    model = TapaImage

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


@admin.register(Tapa)
class TapaAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'linea')
    search_fields = ('id', 'modelo', 'linea')
    list_filter = ('linea',)
    inlines = (TapaImageInlineAdmin,)
    filter_horizontal = ('caracteristica',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'color')
    search_fields = ('id', 'codigo', 'color',)


@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'caracteristica')
    search_fields = ('id, caracteristica',)


@admin.register(Loza)
class LozaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen')
    search_fields = ('id',)


@admin.register(Texto)
class TextoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'texto')
    search_fields = ('id', 'codigo', 'texto',)
