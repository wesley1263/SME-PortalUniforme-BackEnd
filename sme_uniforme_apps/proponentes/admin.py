from django.contrib import admin

from .models import (Proponente)


@admin.register(Proponente)
class ProponenteAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'responsavel', 'telefone', 'email', 'alterado_em')
    ordering = ('-alterado_em',)
    search_fields = ('cnpj', 'razao_social', 'responsavel')
