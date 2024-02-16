from django.contrib import admin
from apteka.models import Salesman, Check, Medicament, PositionCheck


class MedicamentAdminInline(admin.TabularInline):
    model = Medicament
    extra = 1

class PositionChecktAdminInline(admin.TabularInline):
    model = PositionCheck
    extra = 1

@admin.register(Medicament)
class AptekaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    # list_filter = ('app_status',)
    ordering = ('name', 'price',)
    list_per_page = 10
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Salesman)
class AptekaAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
    ordering = ('surname', 'name', 'patronymic')
    list_per_page = 10
    search_fields = ('surname', 'name', 'patronymic')
    list_display_links = ('surname', 'name')


@admin.register(Check)
class AptekaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'salesman', 'date_at')
    list_filter = ('salesman',)
    ordering = ('pk', 'salesman', 'date_at')
    list_per_page = 10
    search_fields = ('salesman__name', 'salesman__surname', 'salesman__patronymic', 'pk')
    list_display_links = ('pk', 'salesman')
    inlines = (PositionChecktAdminInline,)


# @admin.register(PositionCheck)
# class AptekaAdmin(admin.ModelAdmin):
#     list_display = ('sale', 'medicament', 'count')
#     ordering = ('sale', 'medicament', 'count')
#     list_per_page = 10
#     search_fields = ('sale', 'medicament')
#     list_display_links = ('sale',)