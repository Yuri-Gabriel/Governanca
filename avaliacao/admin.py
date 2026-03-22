from django.contrib import admin

from .models import (
    Avaliacao,
    CategoriaQuestao,
    Empresa,
    LogAuditoriaResposta,
    Profile,
    Questao,
    Resposta,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cnpj", "setor", "criada_em")
    search_fields = ("nome", "cnpj")


@admin.register(CategoriaQuestao)
class CategoriaQuestaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ("id", "categoria", "ativa")
    list_filter = ("categoria", "ativa")


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "empresa", "consultor_responsavel", "status", "criada_em")
    list_filter = ("status", "empresa")


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ("avaliacao", "questao", "resposta", "respondido_por", "atualizado_em")
    list_filter = ("resposta", "avaliacao")


@admin.register(LogAuditoriaResposta)
class LogAuditoriaRespostaAdmin(admin.ModelAdmin):
    list_display = ("resposta_registro", "usuario", "resposta", "criado_em")
    list_filter = ("resposta",)
