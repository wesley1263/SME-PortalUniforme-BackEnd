from django.contrib import admin

from .models import (Proponente, OfertaDeUniforme, Loja, Anexo, ListaNegra)


class UniformesFornecidosInLine(admin.TabularInline):
    model = OfertaDeUniforme
    extra = 1  # Quantidade de linhas que serão exibidas.


class LojasInLine(admin.StackedInline):
    model = Loja
    extra = 1  # Quantidade de linhas que serão exibidas.


class AnexosInLine(admin.TabularInline):
    model = Anexo
    extra = 1  # Quantidade de linhas que serão exibidas.


@admin.register(Proponente)
class ProponenteAdmin(admin.ModelAdmin):
    list_display = ('protocolo',  'cnpj', 'razao_social', 'responsavel', 'telefone', 'email', 'alterado_em')
    ordering = ('-alterado_em',)
    search_fields = ('uuid', 'cnpj', 'razao_social', 'responsavel')
    inlines = [UniformesFornecidosInLine, LojasInLine, AnexosInLine]


@admin.register(OfertaDeUniforme)
class OfertaDeUniformeAdmin(admin.ModelAdmin):
    @staticmethod
    def protocolo(oferta):
        return oferta.proponente.protocolo

    list_display = ('protocolo', 'proponente',  'uniforme', 'preco')
    ordering = ('proponente',)
    search_fields = ('proponente__uuid', 'uniforme__nome',)
    list_filter = ('uniforme', )


@admin.register(ListaNegra)
class ListaNegraAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social')
    ordering = ('razao_social',)
    search_fields = ('cnpj', 'razao_social')
