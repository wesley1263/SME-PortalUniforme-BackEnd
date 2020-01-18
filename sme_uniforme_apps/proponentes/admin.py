from django.contrib import admin

from .models import (Proponente, OfertaDeUniforme)


class UniformesFornecidosInLine(admin.TabularInline):
    model = OfertaDeUniforme
    extra = 1  # Quantidade de linhas que serão exibidas.


@admin.register(Proponente)
class ProponenteAdmin(admin.ModelAdmin):
    list_display = ('protocolo',  'cnpj', 'razao_social', 'responsavel', 'telefone', 'email', 'alterado_em')
    ordering = ('-alterado_em',)
    search_fields = ('uuid', 'cnpj', 'razao_social', 'responsavel')
    inlines = [UniformesFornecidosInLine]
